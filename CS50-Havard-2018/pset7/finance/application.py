import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Ensure environment variable is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


# Configure application
app = Flask(__name__)


# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # get cash
    cash = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
    # format
    cash_ = usd(cash[0]["cash"])
    totalsum = cash[0]["cash"]

    stocks = db.execute("SELECT symbol, shares FROM portfolio WHERE id=:id", id=session["user_id"])
    # aggregate can also be done by having
    for stock in stocks:
        symbol = str(stock["symbol"])
        shares = int(stock["shares"])
        name = ""
        price = ""
        total = ""
        quote = lookup(symbol)
        stock["symbol"] = quote["symbol"]
#       stock["price"] = "{:.2f}".format(quote["price"])
#       stock["total"] = "{:.2f}".format(quote["price"] * shares)
        stock["price"] = usd(quote["price"])
        stock["total"] = usd(quote["price"] * shares)
        stock["totalsum"] = quote["price"] * shares
        totalsum += quote["price"] * shares

    # format
    # totalsum = "{:.2f}".format(totalsum)
    totalsum = usd(totalsum)
    # direct to display
    return render_template("index.html", stocks=stocks, cash=cash_, totalsum=totalsum)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        if not request.form.get("symbol") or not request.form.get("shares"):
            return apology("please provide valid symbols and shares")

        # look and check quote
        quote = lookup(request.form.get("symbol"))
        if quote == None:
            return apology("invalid symbol")
        # look and check shares
        if not request.form.get("shares").isdigit():
            return apology("shares should be a positive integer")
        shares = int(request.form.get("shares"))
        price = round(float(quote["price"]), 2)
        if shares < 1:
            return apology("shares should be a positive integer")

         # get cash
        cash = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
        cost = round(float(shares * price), 2)

        # check if enough money
        if cost > cash[0]["cash"]:
            return apology("insufficient cash")
        else:
            # buy the stock and record
            db.execute("UPDATE users SET cash = cash - :cost WHERE id = :id", cost=cost, id=session["user_id"])
            db.execute("UPDATE portfolio SET shares = shares + :shares WHERE id = :id AND symbol = :symbol",
                       id=session["user_id"], symbol=quote["symbol"], shares=shares)
            db.execute("INSERT OR IGNORE INTO portfolio (id,symbol,shares) VALUES (:id,:symbol,:shares)",
                       id=session["user_id"], symbol=quote["symbol"], shares=shares)
            db.execute("INSERT INTO history (id,symbol,shares,price,date) VALUES (:id,:symbol,:shares,:price,datetime('now'))",
                       id=session["user_id"], symbol=quote["symbol"], shares=shares, price=price)
            flash("Purchase Successful!")
        return redirect("/")
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # obtain stock info from portfolio database
    history = db.execute("SELECT symbol, shares, price, date FROM history WHERE id = :id ORDER BY date DESC", id=session["user_id"])

    # for every stock in the user's portfolio, assign dict key/values for use in html/jinja
    for transaction in history:
        symbol = transaction["symbol"]
        shares = transaction["shares"]
        price = transaction["price"]
        date = transaction["date"]

    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # if the user reached via GET, return quote page
    if request.method == "GET":
        return render_template("quote.html")

    elif request.method == "POST":
        if not request.form.get("symbol"):
            return apology("Please provide a valid symbol")

        quote = lookup(request.form.get("symbol"))

        if quote == None:
            return apology("Please procide a valid symbol")
        else:
            return render_template("quoted.html", symbol=quote["symbol"], price=usd(quote["price"]))


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        # check user name
        if not request.form.get("username"):
            return apology("please provide a user name")

        # check password
        if not request.form.get("password"):
            return apology("please provide a password")

        # confirm password
        if not request.form.get("confirmation"):
            return apology("please confirm your password")

        # check password match
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("password does not match")

        # inject the hash value into the database
        password = request.form.get("password")
        hash_value = generate_password_hash(password)

        result = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)",
                            username=request.form.get("username"), hash=hash_value)
        # check if successful
        if not result:
            return apology("User name used!")
        # store their id in session to log in
        user_id = db.execute("SELECT id FROM users WHERE username is :username", username=request.form.get("username"))
        session['user_id'] = user_id[0]['id']

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        if not request.form.get("symbol") or not request.form.get("shares"):
            return apology("please provide valid symbols and shares")

        # look and check quote
        quote = lookup(request.form.get("symbol"))
        if quote == None:
            return apology("invalid symbol")
        # look and check shares
        if not request.form.get("shares").isdigit():
            return apology("shares should be a positive integer")

        # get shares
        shares = int(request.form.get("shares"))
        # get stocks by symbol
        stocks = []
        stocks = db.execute("SELECT shares FROM portfolio WHERE id=:id AND symbol =:symbol",
                            id=session["user_id"], symbol=quote["symbol"])
        if stocks == []:
            return apology("you don't own any of this stock")
        if shares > stocks[0]["shares"]:
            return apology("shares exceeds the shares you own")

        price = round(float(quote["price"]), 2)
        proceed = round(float(shares * price), 2)

        # update to cash
        db.execute("UPDATE users SET cash = cash + :proceed WHERE id = :id", proceed=proceed, id=session["user_id"])

        # update shares
        if shares == stocks[0]["shares"]:
            db.execute("DELETE FROM portfolio WHERE id = :id AND symbol = :symbol", id=session["user_id"], symbol=quote["symbol"])
        else:
            db.execute("UPDATE portfolio SET shares = shares - :shares WHERE id = :id AND symbol = :symbol",
                       id=session["user_id"], shares=shares, symbol=quote["symbol"])

        db.execute("INSERT INTO history (id,symbol,shares,price,date) VALUES (:id,:symbol,:shares,:price,datetime('now'))",
                   id=session["user_id"], symbol=quote["symbol"], shares=-shares, price=price)
        return redirect("/")
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        symbols = db.execute("SELECT symbol FROM portfolio WHERE id=:id", id=session["user_id"])
        return render_template("sell.html", symbols=symbols)


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

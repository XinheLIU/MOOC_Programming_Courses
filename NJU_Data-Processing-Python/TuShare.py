# "TuShare is a free, open source python financial data interface package. It extends its function from data retrieval, cleaning and processing to the data storage of 
# stocks and other financial data, and is able to provide financial analysts with fast, neat, and diverse data to facilitate their analysis. It greatly reduces their 
# workload in data acquisition and allows them to put more focus on the research and implementation of strategy and model. As Python pandas package has demonstrated 
# great advantages in financial quantitative analysis, most of the data formats returned by TuShare are the pandas DataFrame, which is very convenient for the 
# pandas/NumPy/Matplotlib to do data analysis and visualization. Of course, if you're used to doing analysis with Excel or relational databases, you can save the data 
# locally via TuShare's data storage function and analyze it later. This is a description of TuShare on the official TuShare website (http://tushare.org/index.html), 
# which provides a simple and fast interface to various financial data and news etc.
# For example, if you want to obtain the historical data of the stock coded 600848 between the date March 1 and March 10, 2018, you can simply use the following code:

import tushare as ts
ts.get_hist_data('600848',start='2018-03-01',end='2018-03-10')
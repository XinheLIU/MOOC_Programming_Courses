#include <stdio.h>
#include <cs50.h>

// To check whether your credit card is valid or not

int main (void)
{
    long long card_num, x2;
    int addsum, x2prod, sum = 0;
    // prompt user to enter the credit card number
    do
    {
        printf("Number:");
        card_num = get_long_long();
    }
    while ( card_num < 0 );

    long long xadd = card_num;
    // step 1: sum every other digit starting w/ last digit
    for ( addsum  = 0; xadd > 0; xadd /= 100 )
        addsum += xadd % 10;

    // double every other digit starting w/ 2nd to last
    // then sum the individual digits of these products
    for ( x2 = card_num / 10, x2prod = 0; x2 > 0; x2 /= 100 )
    {
        if ( 2 * (x2 % 10) > 9 )        // two digits number yield
        {
            x2prod += (2 * (x2 % 10)) / 10;  // add 10th digit
            x2prod += (2 * (x2 % 10)) % 10;  // add unit digit
        }
        else
            x2prod += 2 * (x2 % 10);
    }

    sum = addsum + x2prod;

    // check to see if the CC number is in the appropriate range
    if ( sum % 10 == 0 )
    {
        if ( (card_num >= 340000000000000 && card_num < 350000000000000) || (card_num >= 370000000000000 && card_num < 380000000000000) )
            printf("AMEX\n");
        else if ( card_num >= 5100000000000000 && card_num < 5600000000000000 )
            printf("MASTERCARD\n");
        else if ( (card_num >= 4000000000000 && card_num < 5000000000000) || (card_num >= 4000000000000000 && card_num < 5000000000000000) )
            printf("VISA\n");
        else
            printf("INVALID\n");
    }
    else
        printf("INVALID\n");

    return 0;
}
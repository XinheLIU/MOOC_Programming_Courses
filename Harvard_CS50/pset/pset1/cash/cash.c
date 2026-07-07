#include <stdio.h>
#include <cs50.h>
#include <math.h>
/* This question aims to calculuate the mimimum number of coins to change
by using greedy algorithm. Four types of coins are used: quarter, dime, nickel
and penny
*/

int main(void)
{
    float dollars;
    do
    {
        printf("Change owed: ");
        dollars = get_float();
    }
    while (dollars < 0);
    // dollars to cents and round
    unsigned cents = round(dollars * 100);
    unsigned coin_count = 0;
    unsigned coins[4] = {25, 10, 5, 1};
    // loop over 4 types of coins and add to toal coin count
    for (int i = 0; i < 4; ++i)
    {
        coin_count += cents / coins[i];
        cents %= coins[i];
    }
    // print the result
    printf("%i\n", coin_count);
    return 0;
}

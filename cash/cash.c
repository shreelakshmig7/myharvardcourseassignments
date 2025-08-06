#include <cs50.h>
#include <math.h>
#include <stdio.h>

int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);

int main(void)
{
    // Prompt the user for change owed, in cents
    int cents;
    do
    {
        cents = get_int("Change owed (in cents): ");
    }
    while (cents < 0);

    int coins;
    if (cents == 0)
    {
        coins = 0;
    }
    else
    {
        int change = cents;
        int quarters = 0, dimes = 0, nickels = 0, pennies = 0;
        while (change > 0)
        {
            if (change >= 25)
            {
                // Calculates the number of quarters to give the customer
                quarters = calculate_quarters(change);
                change = change - (quarters * 25);
            }
            else if (change >= 10)
            {
                // Calculates the number of dimes to give the customer
                dimes = calculate_dimes(change);
                change = change - (dimes * 10);
            }
            else if (change >= 5)
            {
                // Calculates the number of nickels to give the customer
                nickels = calculate_nickels(change);
                change = change - (nickels * 5);
            }
            else
            {
                // Calculates the number of pennies to give the customer
                pennies = change;
                change = 0;
            }
        }

        // Sum coins
        coins = quarters + dimes + nickels + pennies;
    }

    // Prints total number of coins to give the customer
    printf("%i\n", coins);
}

int calculate_quarters(int cents)
{
    // Calculates the number of quarters
    int quarters = (int) floor(cents / 25);
    return quarters;
}

int calculate_dimes(int cents)
{
    // Calculates the number of dimes
    int dimes = (int) floor(cents / 10);
    return dimes;
}

int calculate_nickels(int cents)
{
    // Calculates the number of nickels
    int nickels = (int) floor(cents / 5);
    return nickels;
}

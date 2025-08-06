#include <cs50.h>
#include <math.h>
#include <stdio.h>

string type_of_card = "";
int check_input_validity(int no_of_digits, int first_digit, int second_digit);
void check_validity_of_card(int no_of_digits, long card_number);

int main(void)
{
    // get input
    long card_number = get_long("Pleae enter the card number: ");

    int no_of_digits = log10(card_number) + 1;
    int first_digit = (int) (card_number / pow(10, no_of_digits - 1));
    int second_digit = (int) (card_number / pow(10, no_of_digits - 2)) - (first_digit * 10);

    // check for valid input
    int invalid = check_input_validity(no_of_digits, first_digit, second_digit);

    if (invalid == 1)
    {
        printf("INVALID\n");
    }
    else
    {
        check_validity_of_card(no_of_digits, card_number);
    }
}

int check_input_validity(int no_of_digits, int first_digit, int second_digit)
{
    int invalid = 0;
    if (no_of_digits != 13 && no_of_digits != 15 && no_of_digits != 16)
    {
        invalid = 1;
    }
    else if (no_of_digits == 15)
    {
        // American Express
        type_of_card = "AMEX";
        if (first_digit != 3)
        {
            invalid = 1;
        }
        else if (first_digit == 3 && (second_digit != 4 && second_digit != 7))
        {
            invalid = 1;
        }
    }
    else if (no_of_digits == 16)
    {
        // Mastercard or Visa
        if (first_digit != 5 && first_digit != 4)
        {
            invalid = 1;
        }
        else if (first_digit == 5)
        {
            type_of_card = "MASTERCARD";
            if ((second_digit != 1 && second_digit != 2 && second_digit != 3 && second_digit != 4 && second_digit != 5))
            {
                invalid = 1;
            }
        }
        else if (first_digit == 4)
        {
            type_of_card = "VISA";
        }
    }
    else if (no_of_digits == 13)
    {
        // Visa card
        type_of_card = "VISA";
        if (first_digit != 4)
        {
            invalid = 1;
        }
    }
    return invalid;
}

void check_validity_of_card(int no_of_digits, long card_number)
{
    int oddSum = 0;
    int evenSum = 0;
    for (int j = 0; j < no_of_digits; j++)
    {
        int each_digit = (int) (card_number % 10);
        if (j % 2 != 0)
        {
            // get product of second-to-last-digit
            int prod = each_digit * 2;
            // split the numbers >10
            if (prod > 9)
            {
                prod = 1 + (prod - 10);
            }
            oddSum = oddSum + prod;
        }
        else
        {
            // sum up rst of the numbers
            evenSum = evenSum + each_digit;
        }
        card_number = card_number / 10;
    }
    // check if its multiple of 10s
    if ((oddSum + evenSum) % 10 != 0)
    {
        printf("INVALID\n");
    }
    else
    {
        // print card type
        printf("%s\n", type_of_card);
    }
}

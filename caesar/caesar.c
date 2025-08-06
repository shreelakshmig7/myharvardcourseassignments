#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int validate_key(string key);
string cipher_it(string input_string, int key);

int main(int argc, string argv[])
{
    // check for commandline argument and validate
    if (argc > 2 || argc < 2 || validate_key(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    int key = atoi(argv[1]);

    // get input string
    string input_string = get_string("plaintext:  ");
    char *cipher_text = malloc(strlen(input_string) + 1);

    // cipher the input string
    strcpy(cipher_text, cipher_it(input_string, key));

    // output the cipher text
    printf("ciphertext: %s\n", cipher_text);
    return 0;
}

int validate_key(string key)
{
    int i = 0;
    while (key[i] != '\0')
    {
        if (!isdigit(key[i]))
        {
            return 1;
        }
        i++;
    }
    return 0;
}

string cipher_it(string input_string1, int key1)
{
    int no_of_rotaions = key1 % 26;
    char *cipher_text1 = malloc(strlen(input_string1) + 1);
    if (no_of_rotaions == 0)
    {
        strcpy(cipher_text1, input_string1);
    }
    else
    {
        int i = 0;
        while (input_string1[i] != '\0')
        {
            // checking non-alphabetical characters
            if (!isalpha(input_string1[i]))
            {
                cipher_text1[i] = input_string1[i];
            }
            else
            {
                int ascii_val = (int) input_string1[i];
                int new_val = ascii_val + no_of_rotaions;

                // logic for lower and upper case letters
                if (islower(input_string1[i]) && new_val > 122)
                {
                    new_val = 97 + (new_val - 122 - 1);
                }
                else if (isupper(input_string1[i]) && new_val > 90)
                {
                    new_val = 65 + (new_val - 90 - 1);
                }
                cipher_text1[i] = (char) new_val;
            }
            i++;
        }
    }
    return cipher_text1;
}

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int validate_key(string key);
string cipher_it(string input_string, string key, string base_string);

int main(int argc, string argv[])
{
    // check for commandline argument and validate
    if (argc > 2 || argc < 2 || validate_key(argv[1]))
    {
        printf("Usage: ./substitution key\n Key should contain 26 alphabetical characters with no repetition\n");
        return 1;
    }

    string alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    // get input string
    string input_string = get_string("plaintext:  ");
    char *cipher_text = malloc(strlen(input_string) + 1);

    // cipher the input string
    strcpy(cipher_text, cipher_it(input_string, argv[1], alphabets));

    // output the cipher text
    printf("ciphertext: %s\n", cipher_text);
    return 0;
}

int validate_key(string key)
{
    if (strlen(key) != 26)
    {
        return 1;
    }

    int i = 0;
    while (key[i] != '\0')
    {
        string s1 = strchr(key, (int) key[i]);  // first occurance
        string s2 = strrchr(key, (int) key[i]); // last occurance

        // check for non-alphabetical and repetition of character (same case)
        if (!isalpha(key[i]) || strcmp(s1, s2) != 0)
        {
            return 1;
        }

        // checking repetition of character in different case
        if (islower(key[i]))
        {
            string s3 = strchr(key, (int) toupper(key[i]));
            if (s3 != NULL && strcmp(s1, s3) != 0)
            {
                return 1;
            }
        }
        else
        {
            string s3 = strchr(key, (int) tolower(key[i]));
            if (s3 != NULL && strcmp(s1, s3) != 0)
            {
                return 1;
            }
        }
        i++;
    }
    return 0;
}

string cipher_it(string input_string1, string key, string base_string)
{
    char *cipher_text1 = malloc(strlen(input_string1) + 1);
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
            // searching for index
            int j = 0;
            while (tolower(input_string1[i]) != tolower(base_string[j]))
            {
                j++;
            }

            if (isupper(input_string1[i]))
            {
                cipher_text1[i] = toupper(key[j]);
            }
            else
            {
                cipher_text1[i] = tolower(key[j]);
            }
        }
        i++;
    }
    return cipher_text1;
}

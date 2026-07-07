#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#define A 65
#define a 97

// Encrypts messages using the vigenere cipher.

int main(int argc, string argv[])
{
    if (argc == 1)
    {
        printf("Error: Please enter one argument as the Vigenere encryption key!\n");
        return 1;
    }
    else if (argc > 2)
    {
        printf("Error: Please enter exactly one argument as the Vigenere encryption key!\n");
        return 1;
    }
    else
    {
        string keys = argv[1];
        int keys_len = strlen(keys);

        for (int i = 0; i < keys_len; ++i)
        {
            if (!isalpha(keys[i]))
            {
                printf("Error! please print a vaild key with only alphabets!");
                return 1;
            }
            // convert to capital letters to compare with A
            keys[i] = toupper(keys[i]);
        }

        int len_alphabet = 26;
        // loop over the input string
        printf("plaintext: ");
        string msg = get_string();
        printf("\n");
        printf("ciphertext: ");

        int j = 0;  // loop over the key word
        for (int i = 0; i < strlen(msg); ++i)  // loop over the string
        {
            char key = keys[(j % keys_len)];
            // Add key to uppercase letters.
            if (isupper(msg[i]))
            {
                printf("%c", ((msg[i] - A + (key - A)) % len_alphabet) + A);
                ++j;
            }
            // Add key to lowercase letters.
            else if (islower(msg[i]))
            {
                printf("%c", ((msg[i] - a + (key - A)) % len_alphabet) + a);
                ++j;
            }
            else   // leave non-letters alone
            {
                printf("%c", msg[i]);
            }
        }
        printf("\n");

    }
    return 0;
}
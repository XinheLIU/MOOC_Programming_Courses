#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#define A 65
#define a 97

// Encrypts messages using the Caesar cipher.

int main(int argc, string argv[])
{
    if (argc == 1)
    {
        printf("Error: Please enter one argument as the Caesar encryption key!\n");
        return 1;
    }
    else if (argc > 2)
    {
        printf("Error: Please enter exactly one argument as the Caesar encryption key!\n");
        return 1;
    }
    else
    {
        int key = atoi(argv[1]);
        int len_alphabet = 26;
        // loop over the input string
        printf("plaintext: ");
        string msg = get_string();
        printf("\nciphertext: ");
        for (int i = 0; i < strlen(msg); ++i)
        {
            // Add key to uppercase letters.
            if (isupper(msg[i]))
            {
                printf("%c", ((msg[i] - A + key) % len_alphabet) + A);
            }
            // Add key to lowercase letters.
            else if (islower(msg[i]))
            {
                printf("%c", ((msg[i] - a + key) % len_alphabet) + a);
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
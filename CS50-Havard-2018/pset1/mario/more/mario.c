# include <stdio.h>
# include <cs50.h>

// This program by Xinhe Liu prints right-aligned pyramid by user input
int main(void)
{
    int height;
    // request user input
    do
    {
        printf("PLease give me a non-negative integer less than 23: ");
        height = get_int();
    }
    while (height < 0 || height > 23);
    // print the pyramid
    int width = height; // the last line has n hashes on the left
    for (int i = 0; i < height; i++)  // i rows
    {
        for (int j = 0; j < width; j++) // j columns
        {
            if (j < width - 1 - i)
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
        }
        printf("  ");
        for (int j = 0; j < i + 1; j++) // j columns
        {
            printf("#");
        }

        printf("\n");
    }
    return 0;
}
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
    int width = height + 1; // the last line has n+1 hashes
    for (int i = 0; i < height; i++)  // i rows
    {
        for (int j = 0; j < width; j++) // j columns
        {
            if (j < width - 2 - i)
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
        }
        printf("\n");
    }
    return 0;
}

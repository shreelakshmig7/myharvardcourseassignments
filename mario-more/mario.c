#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for positive integer
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);

    // Prints adjacent pyramids of blocks
    int i = n - 1, j = 0, k = 1, l = 0;

    while (i >= 0 && k <= n)
    {
        // Prints an right-aligned pyramid of bricks
        j = 0;
        while (j < n)
        {
            if (j < i)
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
            j++;
        }
        printf("  ");

        // Prints an left-aligned pyramid of bricks
        l = 0;
        while (l < k)
        {
            printf("#");
            l++;
        }
        i--;
        k++;
        printf("\n");
    }
}

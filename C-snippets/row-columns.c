// With this snippet the computer prints row and columns to make a pyramid but it can be adapted to make another figure.

#include <stdio.h>

int main(void)
{
    // first, get a desired height
    int height = 8; // or any decimal number;

    // second, make a loop that iterates till i is equal to the height  
    for (int i = 0; i < height; i++)
    {

        // third, make a loop that iterates j, that is equal to the height minus i minus 2, till j is equal or lower than 0.
        // the purpose of this loop is to push the hashes to the right, in case you want to see it more graphically, change the printf(" ") to printf(".")
        for (int j = height - i - 2; j >= 0; j--)
        {
            printf(" ");
        }
        // fourth, print the hashes. for each time that the first loop iterates, prints 1 more hash.
        for (int k = 0; k < i; k++)
        {
            printf("#");
        }
        printf("#");

        printf("\n");
    }
}

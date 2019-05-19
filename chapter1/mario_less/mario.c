#include <stdio.h>
#include <cs50.h>
int main(void)
{
    int height = 0;
    do
    {
        height = get_int("How high is the pyramid?");
    }
    while (height < 0 || height > 23);
    for(int i = 1; i <= height; i++) //more user friendly to start i as 1 in this case//
    {
        int spaces = height - i;
        //printf("%d\n", spaces);
        int hashes = i + 1;
        for(int j = 0; j < spaces; j++)
        printf(" ", );
        for(int k = 0; k < hashes; k++)
        printf("#");
        printf("\n");
    }
}
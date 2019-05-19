#include <cs50.h>
#include <stdio.h>
#include <math.h>

int month = 0;
int principle = 0;
int main(void)
{
    while (true)
    {
        month = get_int("How many days are in the month");
        if ( month > 27 && month < 32)
            break;
    }
    while (true)
    {
        principle = get_int("How many pennies do you start with");
        if (principle > 0)
            break;
    }

    double total = 0;
    for (int i = 0; i <= month; i++)
    {
         total = ((principle * pow(2,i)) - principle) / 100;
    }
    printf("$%.2f\n", total);

}

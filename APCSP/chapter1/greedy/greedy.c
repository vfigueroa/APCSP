#include <cs50.h>
#include <stdio.h>
#include <math.h>
float bill = 0;
int remander, quarters, dimes, nickels = 0;
int main(void)
{

while(true)
{
    bill = get_float("What is your bill");
    if (bill > 0)
    {
        break;
    }
}
int cents = round (bill * 100);
if(cents >= 25)
{
    quarters = cents / 25;
    cents = cents % 25;
    //printf("%.d\n", cents);
}
if(cents >= 10)
{
    dimes = cents / 10;
    cents = cents % 10;
    //printf("%d, %d, %d\n",dimes,cents,quarters);
}
if(cents >= 5)
{
    nickels = cents / 5;
    cents = cents % 5;
}

int coins = (quarters + dimes + nickels + cents);
printf("%d", coins);
//printf("%d,%d,%d,%d", quarters, dimes, nickels, cents);
}
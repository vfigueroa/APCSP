#include <cs50.h>
#include <stdio.h>

int main(void)
{
    float temp = get_float("Please enter a tempature in Celsius");
    float fahrenheit = ((temp * 9) / 5) + 32;
    printf("%.1f\n", fahrenheit);
}

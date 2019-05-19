/**
 * hello.c
 *
 * CS50 AP
 * Old Friends
 *
 * Greets a user by their name.
 */

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./hello <name>\n");
        return 1;
    }
    // collect a string from the user, then print their name
    printf("Hello, %s!\n", argv[1]);
}

#include <cs50.h>
#include <string.h>
#include <math.h>
#include <stdio.h>
#include <ctype.h>
char newletter = 0;
char encrypt(char olderletter, int key);
int main(int argc, string argv[])
{
    if (argc != 2)
        {
           printf("Usage: ./caesar <name>\n");
           return 1;
         }
    int key = atoi(argv[1]);
    string plaintext = get_string("Plaintext:");
    int length = strlen(plaintext);
    printf("ciphertext: ");
    for(int i = 0; i < length; i++)
    {
        char oldletter = plaintext[i];
        encrypt(oldletter, key);
    }
    printf("\n");
}
char encrypt(char oldletter, int key)
{
    if (isalpha(oldletter))
    {
        if (isupper(oldletter))
        {
            newletter = (((oldletter - 65) + key) % 26) + 65;
        }
        if (islower(oldletter))
        {
            newletter = (((oldletter - 97) + key) % 26) + 97;
        }
    }
    else
    {
        newletter = oldletter;
    }
    printf("%c", newletter);
    return 0;
}
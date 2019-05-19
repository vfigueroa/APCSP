#include <cs50.h>
#include <string.h>
#include <math.h>
#include <stdio.h>
#include <ctype.h>
int key = 0;
char newletter = 0;
int main(int argc, string argv[])
{
  if (argc != 2)
        {
           printf("Usage: ./hello <name>\n");
           return 1;
         }
    key = atoi(argv[1]);
    string plaintext = get_string("Plaintext:");
  int length = strlen(plaintext);
    for(int i = 0; i <= length; i++)
    {
      if (isalpha(plaintext[i]))
      {
        if (isupper(plaintext[i]))
        {
          newletter = (((plaintext[i] - 64) + key) % 26) + 64;
        }
        if (islower(plaintext[i]))
        {
           newletter = (((plaintext[i] - 96) + key) % 26) + 96;
        }
      }
      else
      {
        newletter = plaintext[i];
      }
      printf("%c", newletter);
    }
}
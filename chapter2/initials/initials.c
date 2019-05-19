#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdio.h>
char i1, j2, k3 = 0;
int i, k = 0;
int check = 0;
int main(void)
{
    string name = get_string() ;
    int length = strlen(name);
    //printf("%s, %d", name, length);
    for(int a = 0; a < length; a++)
    {
        if(check == 0)
        {
          for(i = k; i < length; i++)
          {
            if(name[i] != ' ')
            {
                i1 = name[i];
                printf("%c", toupper(i1));
                check = 1;
                break;
            }
          }
        }
       if(check == 1)
       {
           for(int j = i; j < length; j++)
           {
               if(name[j] == ' ')
               {
                   k = j;
                   check = 0;
                   break;
               }
           }
       }
    }
    printf("\n");
}
//second loops needs to start after the first name and then set check = 0

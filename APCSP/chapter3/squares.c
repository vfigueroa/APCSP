//project based off of CS50 code given in the program Fifteen//
#define _XOPEN_SOURCE 500

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void clear(void);
void greet(void);
void init(void);
void draw(void);
bool moveB(int col);
bool moveR(int col);
bool won(void);
bool check_horizontal(void);
bool check_vertical(void);
bool check_diaginall(void);
bool check_diaginalr(void);

int turn = 1;

int main(void)
{
    greet();
    init();
    while(true)
    {
        if(turn == 1)
        {
            clear();
            draw();
            if (!won())
            {
                break;
            }
            printf("Blue Move: ");
            int col = get_int();
            if (col == 0)
            {
                break;
            }
            turn = 2;
            if (!moveB(col))
            {
                printf("\nIllegal move.\n");
                usleep(500000);
                turn = 1;
            }
        }
        if(turn == 2)
        {
            clear();
            draw();
            if (!won())
            {
                break;
            }
            printf("Red Move: ");
            int col = get_int();
            if (col == 0)
            {
                break;
            }
            turn = 1;
            if (!moveR(col))
            {
                printf("\nIllegal move.\n");
                usleep(500000);
                turn = 2;
            }
        }

    }
}
//clear and greet were part of the source code for Fifteen//
void clear(void)
{
    printf("\033[2J");
    printf("\033[%d;%dH", 0, 0);
}
void greet(void)
{
    clear();
    printf("WELCOME TO GAME OF CONNECT FOUR\n");
    usleep(2000000);
}
// all of the following functions are 100% my own work//
int board[6][7];
void init(void)
{
     for(int i = 0; i<6; i++)
    {
        for(int j =0; j<7; j++)
        {
            board [i][j] = 0;
            //printf("%d  ", board [i][j]);
        }
        //printf("\n");
    }
}
void draw(void)
{
    for(int i = 0; i < 6; i++)
    {
        for(int j = 0; j < 7; j++)
        {
           if(board[i][j]==0)
            {
                printf("⚪");
            }
            if(board[i][j]==2)
            {
                printf("🔴");
            }
            if(board[i][j] == 1)
            {
                printf("🔵");
            }
        }
        printf("\n");
    }
}
bool moveB(int col)
{
    //printf("%d", col);
    if(col < 1 || col > 7)
    {
        return false;
    }
    int row = 5;
    while(board[row][col-1] != 0)
    {
        if(board[row][col-1] == 1 || board[row][col-1] == 2)
        {
            row--;
            if(row < 0)
            {
                return false;
            }
        }
    }
    board[row][col-1] = 1;
    return true;

}
bool moveR(int col)
{
  if(col < 1 || col > 7)
    {
        return false;
    }
    int row = 5;
    while(board[row][col-1] != 0)
    {
        if(board[row][col-1] == 1 || board[row][col-1] == 2)
        {
            row--;
            if(row < 0)
            {
                return false;
            }
        }
    }
    board[row][col-1] = 2;
    return true;
}
bool won(void)
{
   if(!check_horizontal() && !check_vertical() && !check_diaginall() && !check_diaginalr())
   {
       return true;
   }
   return false;
}
bool check_horizontal(void)
{
    for(int r = 0; r < 6; r++)
    {
        for( int c = 0; c < 4; c++)
        {
            if(board[r][c] == 1 && board[r][c+1] == 1 && board[r][c+2] == 1 && board[r][c+3] == 1)
            {
                printf("Blue Wins");
                return true;
            }
             if(board[r][c] == 2 && board[r][c+1] == 2 && board[r][c+2] == 2 && board[r][c+3] == 2)
            {
                printf("Red Wins");
                return true;
            }
        }
    }
    return false;
}
bool check_vertical(void)
{
    for(int r = 0; r < 3; r++)
    {
        for( int c = 0; c < 7; c++)
        {
            if(board[r][c] == 1 && board[r+1][c] == 1 && board[r+2][c] == 1 && board[r+3][c] == 1)
            {
                printf("Blue Wins");
                return true;
            }
             if(board[r][c] == 2 && board[r+1][c] == 2 && board[r+2][c] == 2 && board[r+3][c] == 2)
            {
                printf("Red Wins");
                return true;
            }
        }
    }
    return false;
}
bool check_diaginall(void)
{
    for(int r = 0; r < 3; r++)
    {
        for( int c = 0; c < 4; c++)
        {
            if(board[r][c] == 1 && board[r+1][c+1] == 1 && board[r+2][c+2] == 1 && board[r+3][c+3] == 1)
            {
                printf("Blue Wins");
                return true;
            }
             if(board[r][c] == 2 && board[r+1][c+1] == 2 && board[r+2][c+2] == 2 && board[r+3][c+3] == 2)
            {
                printf("Red Wins");
                return true;
            }

        }
    }
    return false;
}
bool check_diaginalr(void)
{
    for(int r = 0; r < 3; r++)
    {
        for( int c = 3; c < 6; c++)
        {
            if(board[r][c] == 1 && board[r+1][c-1] == 1 && board[r+2][c-2] == 1 && board[r+3][c-3] == 1)
            {
                printf("Blue Wins");
                return true;
            }
             if(board[r][c] == 2 && board[r+1][c-1] == 2 && board[r+2][c-2] == 2 && board[r+3][c-3] == 2)
            {
                printf("Red Wins");
                return true;
            }

        }
    }
    return false;
}
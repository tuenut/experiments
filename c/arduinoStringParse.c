#include <stdio.h>
#include <string.h>

int ledValue = 0;

int power(int digit, int pwr)
{
    int result = digit;
    if ( pwr == 0 )
        {
            return 1;
        }
    else
        {
            for( int i = pwr; i>1; i-- )
                {
                    result = result * digit;
                }
            return result;
        }
}

void setupValues(char * inVal, char * inVar)
{
    int intValue = 0;
    
    for ( int i = strlen(inVal) - 1, j = 0; i >= 0; i--, j++ )
        {
            int ii = power(10, i);
            intValue = ( (int)inVal[j] - '0' ) * ii + intValue;
        }

    if ( !strcmp(inVar, "led") )
        {
            ledValue = intValue;
        }
        
    printf("Ok. I set %s to %d\n", inVar, intValue);
}

void showValues(char inVar[])
{
    printf("Ok. Value of %s is %d\n", inVar, ledValue);
}

void main()
{
    char inputString[] = "set led 10";
    char * pch = strtok(inputString, " ");
    
    if ( !strcmp(pch, "set") )
        {
            setupValues(strtok(NULL, " "), strtok(NULL, " "));
        }
    else if ( !strcmp(pch, "show") )
        {
            showValues(strtok(NULL," "));
        }

}


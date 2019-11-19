//
// Created by rowan on 9/7/17.
//

#include <stdio.h>
#include <stdlib.h>

int main()
{
    char *str;

    str = (char *) malloc(15);
    printf("Hello World!");

    str = (char *) realloc(str, 25);

    free(str);

    return(0);
}
#include <stdio.h>
#include <stdlib.h>

void render(char s[])
{
    int i = 0;
    while (s[i] != '\0')
    {
        if (s[i] == '1')
        {
            s[i] = '#';
        }

        if (s[i] == '0')
        {
            s[i] = ' ';
        }

        i++;
    }

    printf("%s", s);
}

void render2file(char s[], char file[])
{
    int i = 0;
    while (s[i] != '\0')
    {
        if (s[i] == '1')
        {
            s[i] = '#';
        }

        if (s[i] == '0')
        {
            s[i] = ' ';
        }

        i++;
    }

    FILE * outfile;

    outfile = fopen (file, "w");

    fprintf(outfile, "%s", s);

    fclose(outfile);
}

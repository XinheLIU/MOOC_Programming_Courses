#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }
    string filename = argv[1];
    typedef uint8_t BYTE;
    //open file
    FILE *inptr = fopen(filename, "r");
    FILE *outptr = NULL;
    if (inptr == NULL)
    {
        printf("Err: cannot open file\n");
        return 2;
    }
    // create buffer arraies
    BYTE buffer[512], header[4];
    BYTE jpeg_header[4] = {0xff, 0xd8, 0xff, 0xe0};

    int jpeg_num = 0; // count and name
    char jpeg_name[8];
    //read in
    while (fread(&buffer, sizeof(buffer), 1, inptr) > 0)
    {
        // read in header if any
        for (int i = 0; i < 4; ++i)
        {
            header[i] = buffer[i];
        }
        // last 1 byte to zero
        header[3] >>= 4;
        header[3] <<= 4;

        // if a signature if found
        if (memcmp(header, jpeg_header, sizeof(jpeg_header)) == 0)
        {
            // no file open
            if (outptr == NULL)
            {
                sprintf(jpeg_name, "%03d.jpg", jpeg_num);
                outptr = fopen(jpeg_name, "a");
                fwrite(&buffer, sizeof(buffer), 1, outptr);
            }
            else // already a file open
            {
                fclose(outptr);
                ++jpeg_num;
                sprintf(jpeg_name, "%03d.jpg", jpeg_num);
                outptr = fopen(jpeg_name, "a");
                fwrite(&buffer, sizeof(buffer), 1, outptr);
            }
        }
        else //not find a header
        {
            if (outptr != NULL)
            {
                fwrite(&buffer, sizeof(buffer), 1, outptr);
            }
        }
    }

    //close the file
    fclose(inptr);
    fclose(outptr);
    return 0;
}

// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // TODO: Copy header from input file to output file

    /* BYTE header[HEADER_SIZE];
    fread(header, sizeof(BYTE), HEADER_SIZE, input);
    fwrite(header, sizeof(BYTE), HEADER_SIZE, output);

    // TODO: Read samples from input file and write updated data to output file
    int16_t *input_data = malloc(50);
    int16_t *output_data = malloc(50);
    int no_of_times = 0; */
    int *input_data = malloc(1);
    while(fread(input_data, sizeof(int), 1, input))
    {
        fwrite(input_data, sizeof(int), 1, output);
    }

    /* printf("current size - %lu\n", sizeof(*input_data));
    printf("current char - %d\n", *input_data);
    printf("current - %ld\n", ftell(input));
    fseek(input, 0, SEEK_END);

    // Printing position of pointer
    printf("end - %ld\n", ftell(input)); */
    free(input_data);
    fclose(input);
    fclose(output);
    return 1;
/*
    while (fread(input_data, sizeof(int16_t), 50, input))
    {
        for (int i = 0; i < 50; i ++)
        {
            *(output_data + i) = *(input_data + i) * factor;
        }

        printf("%i\n", no_of_times++);
        printf("%i\n", *input_data);
        printf("%f\n", *input_data * factor);
        printf("%i\n", *output_data);
        fwrite(output_data, sizeof(int16_t), 50, output);
    }

    free(input_data);
    free(output_data);

    if(!feof(input))
    {
        printf("Error in reading\n");
    }
 */
    // Close files
    fclose(input);
    fclose(output);
}

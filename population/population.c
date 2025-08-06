#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int start_size;
    int end_size;
    int no_of_years = 0;
    int end_of_year_population = 0;
    int new_born = 0;
    int passed_away = 0;

    // TODO: Prompt for start size
    do
    {
        start_size = get_int("Enter the starting population size: ");
    }
    while (start_size < 9);

    // TODO: Prompt for end size
    do
    {
        end_size = get_int("Enter the ending population size: ");
    }
    while (end_size < start_size);

    // TODO: Calculate number of years until we reach threshold
    end_of_year_population = start_size;
    while (end_of_year_population < end_size)
    {
        new_born = end_of_year_population / 3;
        passed_away = end_of_year_population / 4;
        end_of_year_population += new_born - passed_away;
        no_of_years++;
    }

    // TODO: Print number of years
    printf("Years: %i\n", no_of_years);
}

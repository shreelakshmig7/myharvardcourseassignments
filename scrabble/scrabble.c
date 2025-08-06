#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int get_mapping_number(char letters[], int array_size, char each_letter);
int calculate_sum(char letters[], int mapping_nums[], int array_size, string player);

int main(void)
{
    char letters[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    int mapping_nums[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
    int array_size = 26;

    // get input data
    string player1 = get_string("Player 1: ");
    string player2 = get_string("Player 2: ");

    int player1_score, player2_score;
    player1_score = calculate_sum(letters, mapping_nums, array_size, player1);
    player2_score = calculate_sum(letters, mapping_nums, array_size, player2);

    if (player1_score > player2_score)
    {
        printf("Player 1 wins!\n");
    }
    else if (player1_score < player2_score)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int calculate_sum(char letters[], int mapping_nums[], int array_size, string player)
{
    // calculate the string len of string
    int word_len = strlen(player);
    int sum = 0;

    // sum up all the numbers and return
    for (int i = 0; i < word_len; i++)
    {
        if (isalpha(player[i]))
        {
            char each_char = toupper(player[i]);
            int index = get_mapping_number(letters, array_size, each_char);
            sum = sum + mapping_nums[index];
        }
    }
    return sum;
}

int get_mapping_number(char letters[], int array_size, char each_letter)
{
    // search and get mapping num
    int middle_num = (array_size / 2) - 1;
    int player_char_val = (int) each_letter;
    int array_char_val = (int) letters[middle_num];
    int first = 0, last = array_size;

    while (middle_num >= 0 && middle_num <= array_size - 1)
    {
        if (player_char_val == array_char_val)
        {
            break;
        }
        else if (player_char_val < array_char_val)
        {
            last = middle_num;
            middle_num = first + ((int) (last - first) / 2);
            array_char_val = (int) letters[middle_num];
        }
        else if (player_char_val > array_char_val)
        {
            first = middle_num;
            middle_num = first + ((int) (last - first) / 2);
            array_char_val = (int) letters[middle_num];
        }
    }
    return middle_num;
}

#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

void get_letter_word_sentence_count(string input_text, int count_of_all[3]);
int compute_index_value(int no_of_letters, int no_of_words, int no_of_sentences);

int main(void)
{
    // get input text
    string input_text = get_string("Text: ");
    int count_of_all[] = {0, 0, 0};

    // get letters, words and sentences count
    get_letter_word_sentence_count(input_text, count_of_all);

    int no_of_letters = count_of_all[0];
    int no_of_words = count_of_all[1];
    int no_of_sentences = count_of_all[2];

    // compute index value
    int index = compute_index_value(no_of_letters, no_of_words, no_of_sentences);

    // output the grade
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %d\n", index);
    }
}

void get_letter_word_sentence_count(string input_text, int count_of_all[3])
{
    int letter_count = 0;
    int word_count = 0;
    int sentence_count = 0;
    int words_in_a_sentence = 0;

    for (int i = 0; i < strlen(input_text); i++)
    {
        if (isalpha(input_text[i]))
        {
            letter_count++;
            words_in_a_sentence++; // checking whether sentence contain at least one word
        }
        else if (isspace(input_text[i]) && !isspace(input_text[i - 1]))
        {
            word_count++;
        }
        else if (ispunct(input_text[i]) && (input_text[i] == '.' || input_text[i] == '!' || input_text[i] == '?'))
        {
            char prev_char_val = input_text[i - 1];
            if (prev_char_val != '.' && prev_char_val != '!' && prev_char_val != '?' && words_in_a_sentence > 0)
            {
                sentence_count++;
                words_in_a_sentence = 0;
            }
        }
    }
    count_of_all[0] = letter_count;
    count_of_all[1] = word_count + 1; // last word
    count_of_all[2] = sentence_count;
}

int compute_index_value(int no_of_letters, int no_of_words, int no_of_sentences)
{
    // compute index value
    float L, S = 0.0;
    int index = 0.0;

    L = (((float) no_of_letters / no_of_words) * 100);
    S = (((float) no_of_sentences / no_of_words) * 100);

    index = round((0.0588 * L) - (0.296 * S) - 15.8);

    return index;
}

import re


def get_count(text):
    letter_regex = re.compile("([a-z])", re.M | re.I)
    letters = letter_regex.findall(text)

    words_regex = re.compile("([a-zA-Z-']+)", re.M)
    words = words_regex.findall(text)

    sentence_regex = re.compile("(?:[a-zA-Z-']+)([.?!]+)", re.M)
    sentences = sentence_regex.findall(text)

    return (len(letters), len(words), len(sentences))


def compute_grade_level(letters, words, sentences):
    letter_word_avg = (letters / words) * 100
    sentence_word_avg = (sentences / words) * 100
    res_index = round((0.0588 * letter_word_avg) - (0.296 * sentence_word_avg) - 15.8)

    grade = ""

    if res_index >= 16:
        grade = "Grade 16+"
    elif res_index < 1:
        grade = "Before Grade 1"
    else:
        grade = "Grade " + str(res_index)

    return grade


def main():
    text = input("Text: ")
    letters, words, sentences = get_count(text)
    grade = compute_grade_level(letters, words, sentences)
    print(grade)


if __name__ == "__main__":
    main()

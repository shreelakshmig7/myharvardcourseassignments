import csv
import sys
import re


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py <csv-file> <text-file>")
        return 0

    if not re.search(r'^([\w\/]+\.csv)$', sys.argv[1]):
        print("Invalid csv file")
        return 0

    if not re.search(r'^([\w\/]+\.txt)$', sys.argv[2]):
        print("Invalid text file")
        return 0

    rows = []
    fieldNames = []
    # TODO: Read database file into a variable
    with open(sys.argv[1], 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        fieldNames = reader.fieldnames[1:]
        for row in reader:
            rows.append(row)

    # TODO: Read DNA sequence file into a variable
    individual_dna = ""
    with open(sys.argv[2], 'r') as txt_file:
        individual_dna = txt_file.read()

    # TODO: Find longest match of each STR in DNA sequence
    individual_str_count = {}
    for each_str in fieldNames:
        individual_str_count[each_str] = str(longest_match(individual_dna, each_str))

    # TODO: Check database for matching profiles
    found = 0
    for each_person in rows:
        found = 0
        for each_str in fieldNames:
            if individual_str_count[each_str] == each_person[each_str]:
                found += 1
        if found == len(fieldNames):
            print(each_person['name'])
            return

    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()

def extract_and_sort_phonemes(input_file):
    phonemes = set()  # Use a set to avoid duplicates and automatically handle sorting later

    with open(input_file, 'r') as file:
        for line in file:
            parts = line.strip().split()  # Split line into parts, [0] is the word, [1:] are the phonemes
            if len(parts) > 1:  # Check if there are phonemes
                phonemes.update(parts[1:])  # Add phonemes to the set

    sorted_phonemes = sorted(phonemes)  # Sort all phonemes alphabetically

    with open('data/local/dict/nonsilence_phones.txt', 'w') as output_file:
        for phoneme in sorted_phonemes:
            output_file.write(phoneme + '\n')  # Write each phoneme on a new line

    with open('data/local/dict/lexicon.txt', 'w') as lex:
        lex.write('sil sil'+'\n')
        for phoneme in sorted_phonemes:
            lex.write(phoneme + ' ' + phoneme + '\n')  # Write each phoneme on a new line

# Use the function
extract_and_sort_phonemes('lexicon.txt')


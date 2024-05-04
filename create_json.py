import json

def create_json_from_lexicon(input_filename, output_filename):
    data = {}
    with open(input_filename, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')  # Assuming the word and phonemes are separated by a tab
            if len(parts) == 2:
                word, phonemes = parts
                # Check if the word contains only alphabetic characters
                if word.isalpha():
                    data[word.lower()] = phonemes

    # Writing the dictionary to a JSON file
    with open(output_filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Example usage:
create_json_from_lexicon('lexicon.txt', 'lexicon.json')


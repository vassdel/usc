import json
import re
import os

def process_text(input_text_path, lexicon_path, output_text_path):
    # Load the lexicon
    with open(lexicon_path, 'r') as lexicon_file:
        lexicon = json.load(lexicon_file)

    # Process each line in the input text file
    with open(input_text_path, 'r') as infile, open(output_text_path, 'w') as outfile:
        for line in infile:
            # Remove unwanted characters, keep words and apostrophes
            parts = line.split()
            id = parts[0]
            words = re.findall(r'\b\w+\b', line)
            words = words[1:]   
            #words = re.findall(r"[\w']+|[.,!?;]", line)
            # Replace each word with its phoneme representation from the lexicon
            phonemes = [lexicon.get(word.lower(), word) for word in words]
            # Write the phonemes back to file
            outfile.write(id+ ' sil' + ' '.join(phonemes)+' sil' + '\n')
            #print(id+' '+ ' '.join(words))
            #print(id+ ' sil' + ' '.join(phonemes)+' sil')

dirs = [ 'train', 'test', 'dev']

for dir in dirs:
    in_text_file = f'data/{dir}/text'
    out_text_file = f'data/{dir}/temp'
    lex_path = 'lexicon.json'
    process_text(in_text_file, lex_path, out_text_file)
    os.rename(in_text_file, f'data/{dir}/old_text')
    os.rename(out_text_file, f'data/{dir}/text')

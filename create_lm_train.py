import json
import re
import os

def create_lm_files(input_text_path, output_text_path):
    # Process each line in the input text file
    with open(input_text_path, 'r') as infile, open(output_text_path, 'w') as outfile:
        for line in infile:
            # Remove unwanted characters, keep words and apostrophes
            parts = line.split()
            id = parts[0]
            words = re.findall(r'\b\w+\b', line)
            words = words[1:]   
            
            outfile.write(id + ' <s> '+ ' '.join(words)+' </s>' + '\n')
            #print(id+' <s> '+ ' '.join(words)+' </s>')

dirs = [ 'train', 'test', 'dev']

for dir in dirs:
    in_text_file = f'data/{dir}/text'
    out_text_file = f'data/local/dict/lm_{dir}.text'
    create_lm_files(in_text_file, out_text_file)
    #os.rename(in_text_file, f'data/{dir}/old_text')
    #os.rename(out_text_file, f'data/{dir}/text')


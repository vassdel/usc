def format_uttids(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            id = line.strip()  # Remove newline and any extra spaces
            formatted_line = f"~/kaldi/egs/usc/wav/{id}.wav\n"
            outfile.write(id + ' ' + formatted_line)


dirs = ['test', 'dev', 'train']

for dir in dirs:
    format_uttids(f'data/{dir}/uttids', f'data/{dir}/wav.scp')
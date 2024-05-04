# Define the path to the input and output files
input_file_path = 'uttids'
output_file_path = 'utt2spk'

# Open the input file for reading and the output file for writing
def utt2spk(input_file_path, output_file_path):
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        # Iterate over each line in the input file
        for line in infile:
            # Strip newline characters and any leading/trailing whitespace
            clean_line = line.strip()
            # Extract the prefix (first two characters of the line)
            prefix = clean_line[:2]
            # Write the formatted string to the output file
            outfile.write(f'{clean_line} {prefix}\n')

dirs = ['dev', 'train', 'test']

for dir in dirs:
    input_file_path = f'data/{dir}/uttids'
    output_file_path = f'data/{dir}/utt2spk'
    utt2spk(input_file_path, output_file_path)
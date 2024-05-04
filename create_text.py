def match_uttids_with_transcriptions(uttids_path, transcriptions_path, output_path):
    # Build a dictionary from transcriptions.txt
    transcription_dict = {}
    with open(transcriptions_path, 'r') as transcriptions_file:
        for line in transcriptions_file:
            if line.strip():
                # Split on the first space to separate the line number from the text
                line_number, text = line.split(maxsplit=1)
                # Remove any leading zeros for uniformity
                line_number = line_number.lstrip('0')
                transcription_dict[line_number] = text.strip()

    # Process each utterance ID and match it with the transcription
    with open(uttids_path, 'r') as uttids_file, open(output_path, 'w') as output_file:
        for uttid in uttids_file:
            uttid = uttid.strip()
            # Extract the numeric part of the utterance ID (assumes format like 'm1_035')
            _, num = uttid.split('_')
            # Remove leading zeros for matching
            num = num.lstrip('0')
            # Find the corresponding transcription
            if num in transcription_dict:
                # Write the matched line to the output file
                output_file.write(f"{uttid} {transcription_dict[num]}\n")
                #print(f'{uttid} {transcription_dict[num]}')
            else:
                print(f"No match found for {uttid}")


dirs = [ 'train', 'test', 'dev']

for dir in dirs: 
    uttids_path = f'data/{dir}/uttids'
    transcriptions_path = 'transcriptions.txt'
    output_path = f'data/{dir}/text'
    match_uttids_with_transcriptions(uttids_path, transcriptions_path, output_path)



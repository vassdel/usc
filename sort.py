import os

dirs = ['train', 'dev', 'test']

for dir in dirs:
    os.system(f'sort data/{dir}/wav.scp > data/{dir}/temp_wav.scp ; mv data/{dir}/temp_wav.scp data/{dir}/wav.scp')
    os.system(f'sort data/{dir}/text > data/{dir}/temp_text ; mv data/{dir}/temp_text data/{dir}/text')
    os.system(f'sort data/{dir}/utt2spk > data/{dir}/temp_utt2spk ; mv data/{dir}/temp_utt2spk data/{dir}/utt2spk ')


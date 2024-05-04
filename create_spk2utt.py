import os

dirs = ['train', 'test', 'dev']

#os.system('chmod +x /utils/utt2spk_to_spk2utt.pl')

for dir in dirs:
    os.system(f'utils/utt2spk_to_spk2utt.pl data/{dir}/utt2spk > data/{dir}/spk2utt')

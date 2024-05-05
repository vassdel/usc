import os 

def create_ilm(file):
    # creates the unigram.ilm.gz & bigram.ilm.gz files
    os.system(f'build-lm.sh -i ~/kaldi/egs/usc/data/local/dict/lm_{file}.text -n 1 -o ~/kaldi/egs/usc/data/local/lm_tmp/{file}_unigram.ilm.gz')
    print(f'############################### {file} unigram.ilm.gz ready')
    os.system(f'build-lm.sh -i data/local/dict/lm_{file}.text -n 2 -o ~/kaldi/egs/usc/data/local/lm_tmp/{file}_bigram.ilm.gz')
    print(f'############################### {file} bigram.ilm.gz ready')

def create_lm_phone(file):
    # creates the arpa files that correspond to the above:
    # unigram.ilm.gz -> lm_phone_ug.arpa.gz
    # bigram.ilm.gz  -> bigram_phone_bg.arpa.gz
    os.system(f'compile-lm ~/kaldi/egs/usc/data/local/lm_tmp/{file}_unigram.ilm.gz -t=yes /dev/stdout | grep -v unk | gzip -c > ~/kaldi/egs/usc/data/local/nist_lm/lm_{file}_ug.arpa.gz')
    print('############################### lm_phone_ug.arpa.gz ready')
    os.system(f'compile-lm ~/kaldi/egs/usc/data/local/lm_tmp/{file}_bigram.ilm.gz -t=yes /dev/stdout | grep -v unk | gzip -c > ~/kaldi/egs/usc/data/local/nist_lm/lm_{file}_bg.arpa.gz')
    print('############################### lm_phone_bg.arpa.gz ready')

files = ['dev', 'train','test']

for file in files:
    create_ilm(file)

for file in files:
    create_lm_phone(file)

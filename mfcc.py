import os

dirs = ['test', 'dev', 'train']

for dir in dirs:
    os.system(f'steps/make_mfcc.sh --mfcc-config conf/mfcc.conf --cmd "run.pl" \ data/{dir} exp/make_mfcc/{dir} mfcc_{dir}')
    os.system(f'steps/compute_cmvn_stats.sh data/{dir} exp/make_mfcc/{dir} mfcc')
    
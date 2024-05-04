import os

print('DIMENSION OF CHARACTERISTICS')
os.system('feat-to-dim ark:mfcc_train/raw_mfcc_train.1.ark -')

print('FRAMES PER SENTENCE:')
os.system('feat-to-len scp:data/train/feats.scp ark,t:data/train/feats.lengths')

print('FIRST 5 SENTENCES:')
os.system('head -5 data/train/feats.lengths')
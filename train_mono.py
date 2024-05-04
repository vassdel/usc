import os

print('Training monophone model...')
os.system('steps/train_mono.sh data/train data/lang exp/mono')

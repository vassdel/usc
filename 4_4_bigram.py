import os 

os.system('cp ./data/lang_phones_ug/G.fst ./data/lang/G.fst')

# Make HCLG grph
os.system('utils/mkgraph.sh --mono data/lang exp/mono exp/mono/graph_nosp_tgpr')

# Decode for dev (validation) set
os.system('steps/decode.sh exp/mono/graph_nosp_tgpr data/dev exp/mono/decode_dev')
# Decode for the test set.
os.system('steps/decode.sh exp/mono/graph_nosp_tgpr data/test exp/mono/decode_test')


# Print PER for test
print('Printing PER results for test: ')
os.system('./local/score.sh data/test ./data/lang ./exp/mono/decode_test/')
# Print PER fore dev
print('Printing PER results for dev: ')
os.system('./local/score.sh data/dev ./data/lang ./exp/mono/decode_dev/')
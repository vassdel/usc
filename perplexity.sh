#!/bin/bash
source ./path.sh
cd "data/local/lm_tmp"

echo "# Calculating perplexity for the unigram model of the dev set #"
compile-lm dev_unigram.ilm.gz --eval=../dict/lm_dev.text --dub=10000000

echo "# Calculating perplexity for the bigram model of the dev set #"
compile-lm dev_bigram.ilm.gz --eval=../dict/lm_dev.text --dub=10000000

echo "# Calculating perplexity for the unigram model of the test set #"
compile-lm test_unigram.ilm.gz --eval=../dict/lm_test.text --dub=10000000

echo "# Calculating perplexity for the bigram model of the test set #"
compile-lm test_bigram.ilm.gz --eval=../dict/lm_test.text --dub=10000000
cd ../../..

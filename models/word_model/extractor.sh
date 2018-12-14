#!/usr/bin/env bash
cd /mnt/c/Users/Anne/Desktop/COMP550/final_project/mert-work
/mnt/c/Users/Anne/Desktop/COMP550/final_project/mosesdecoder/bin/extractor --sctype BLEU --scconfig case:true  --scfile run1.scores.dat --ffile run1.features.dat -r /mnt/c/Users/Anne/Desktop/COMP550/final_project/tune.en -n run1.best100.out.gz

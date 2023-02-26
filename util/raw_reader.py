import json
import os
import pandas as pd
from tqdm import tqdm
from preprocess import clear_string

eng_tok_lines = {"eng": [], "tok": []}

# read toki-ante tsv files
for address, dirs, files in os.walk("corpora/toki-ante-master"):
    for filename in tqdm(files):
        with open(address + "/" + filename, 'r', encoding="utf-8") as f:
            for line in f.readlines():
                if line == '\n':
                    continue

                eng, tok = line.split('\t')
                if "http" not in eng and "http" not in eng and eng != '' and tok != '': # check if translation exist and the sting is not a rubbish
                    eng_tok_lines["eng"].append(clear_string(eng))
                    eng_tok_lines["tok"].append(clear_string(tok))


# read this semi-empty csv monstrosity
for address, dirs, files in os.walk("corpora/raw-csv"):
    for filename in tqdm(files):
        d = pd.read_csv(address + "/" + filename)
        eng_pon = zip(map(str, list(d["original"])), map(str, list(d["jan Ke Tami"])))
        for pair in eng_pon:
            if pair[0] != 'nan' and pair[1] != 'nan':   # check if translation even exist
                eng_tok_lines["eng"].append(clear_string(pair[0]))
                eng_tok_lines["tok"].append(clear_string(pair[1]))


df = pd.DataFrame(eng_tok_lines, )
df = df.reset_index(drop=True)
df.dropna()
df.to_csv("corpora/eng_tok.csv")
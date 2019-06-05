import MeCab
import pandas as pd
import os, json, re
import numpy as np

class Tokenizer:
    def __init__(self):
        self.m = MeCab.Tagger ("-Owakati -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd")

    def run(self, text):
        return self.m.parse(text)

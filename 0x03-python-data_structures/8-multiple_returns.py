#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None or sentence == "":
        fc = None
        sentence_len = 0
    else:
        fc = sentence[0]
        sentence_len = len(sentence)
    return (sentence_len, fc)

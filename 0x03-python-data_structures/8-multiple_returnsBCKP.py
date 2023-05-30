#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    count = len(sentence)
    strval = sentence[0]
    return (count, strval)

#!/usr/bin/env python3
import sys
import os
import random

quotefiles = ("kapten_haddock", "twin_peaks")
location = os.path.dirname(os.path.realpath(__file__))

def main():
    quotes = []
    for qf in quotefiles:
        qfile = open(location + os.path.sep + qf, "r")
        quotes.extend(qfile.readlines())
        qfile.close()
    quote = random.choice(quotes)
    print(quote)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import sys
import os
import random

quotefiles = ("kapten_haddock", "twin_peaks")

def main():
    quotes = []
    for qf in quotefiles:
        qfile = open(qf, "r")
        quotes.extend(qfile.readlines())
        qfile.close()
    quote = random.choice(quotes)
    print(quote)


if __name__ == "__main__":
    main()

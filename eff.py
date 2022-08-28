#!/usr/bin/env python
# Tested on python 3.10.5, numpy 1.23.1

import csv
import sys
import argparse
from numpy.random import RandomState
from collections import OrderedDict


parser = argparse.ArgumentParser(
    description="EFF Diceware passphrase generator (https://www.eff.org/dice).",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument(
    "seed",
    nargs="?",
    help="seed for random dice roll generation",
    type=int,
    default=12345,
)
parser.add_argument("-n", help="number of words in passphrase", type=int, default=6)
style_choices = OrderedDict(
    (("lc", str.lower), ("uc", str.upper), ("cap", str.capitalize))
)
parser.add_argument(
    "-s",
    "--style",
    choices=style_choices.keys(),
    help="passphrase style (lower/upper/capitalized)",
    type=str,
    default="lc",
)
parser.add_argument(
    "-d",
    "--delimiter",
    help="passphrase delimiter",
    type=str,
    default="-",
)
args = vars(parser.parse_args())


def generate_passphrase(n: int, seed: int):
    eff_dict = {}
    with open("eff_large_wordlist.txt") as f:
        for row in f.read().splitlines():
            num, word = row.split("\t")
            # num is a string
            eff_dict[num] = word
    rs = RandomState(seed)

    # list of strings
    rolls = ["".join(map(str, rs.choice(6, 5) + 1)) for _ in range(n)]
    words = [eff_dict[r] for r in rolls]

    return rolls, words


if __name__ == "__main__":
    rolls, words = generate_passphrase(args["n"], args["seed"])
    word_fn = style_choices[args["style"]]
    phrase = args["delimiter"].join(map(word_fn, words))

    print(" ".join(rolls))
    print(phrase)

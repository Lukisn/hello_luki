#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
from hello_luki.say_hello import say_hello


def parse_args(args=None):
    parser = argparse.ArgumentParser(prog="Say hello")
    parser.add_argument(
        "name", type=str,
        help="Name to say hello to"
    )
    return parser.parse_args(args=args)


def main():
    args = parse_args()
    say_hello(name=args.name)


if __name__ == "__main__":
    sys.exit(main())

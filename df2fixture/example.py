import argparse
import sys
import typing as t

import pandas as pd
import numpy as np

from .generators import BaseGenerator

from df2fixture.mappers.mappers import IdMapper

RANDOM_STATE = 11


"""Parse arguments."""
parser = argparse.ArgumentParser(
    prog='fixtures generator',
    description='automatic fixtures generator from actual db'
)

parser.add_argument('--name', type=str, required=True, metavar='name', help='Testcase name')
parser.add_argument('--output', type=str, required=True, metavar='output', help='output file')


if __name__ == '__main__':

    args = parser.parse_args()
    gen = BaseGenerator()
    print(gen.generate(args.name))

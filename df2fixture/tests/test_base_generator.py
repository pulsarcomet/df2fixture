import pytest

import pandas as pd
import numpy as np

from ..generators import BaseGenerator


def simple_func():
    return 'bbb'

def load_data():
    # pretend that this data was loaded from an external resource
    df = pd.DataFrame()
    df['id'] = [32, 43, 123]
    df['name'] = ['John', 'Alex', 'Bruce']
    df['job'] = ['dev', 'qa', 'pm']
    return df


class Test_BaseGenerator():

    @pytest.fixture
    def config(self) -> list:
        return [
            dict(
                func=load_data,
                kwargs={
                },
                obfuscators={
                    'id': lambda x: x+1,
                    'name': lambda x: 'abc '+x[:3],
                    'job': lambda x: 'xyz '+x[:3]
                },
                #rows_filter=filter_rows
            )
        ]

    def test_constructor(self):
        BaseGenerator()

    def test_generate(self, config: dict):
        generator = BaseGenerator()
        actual = generator.generate('case1', config)
        print('===\n'+actual+'\n===')
        expected = '''# automatically generated file, do not edit!

import typing as t
import pandas as pd
import numpy as np
from datetime import datetime


def __fixture__case1_load_data() -> pd.DataFrame:
    df: pd.DataFrame = pd.DataFrame(columns=['id', 'name', 'job'])
    df['id'] = [33, 44, 124]
    df['name'] = ['abc John', 'abc Alex', 'abc Bruce']
    df['job'] = ['xyz dev', 'xyz qa', 'xyz pm']
    return df


'''
        assert actual == expected

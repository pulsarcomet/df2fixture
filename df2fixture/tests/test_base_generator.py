import pytest

import pandas as pd
import numpy as np
import textwrap

from ..generators import BaseGenerator


def simple_func():
    return 'bbb'

def load_data() -> pd.DataFrame:
    # pretend that this data was loaded from an external resource
    df = pd.DataFrame()
    df['id'] = [32, 43, 123]
    df['name'] = ['John', 'Alex', 'Bruce']
    df['job'] = ['dev', 'qa', 'pm']
    return df


def rows_filter_func(df: pd.DataFrame) -> pd.DataFrame:
    return df.query('id < 44')


class Test_BaseGenerator():

    @pytest.fixture
    def config(self) -> list:
        return [
            dict(
                func=load_data,
                kwargs={
                },
                obfuscators={
                    'id': lambda x: x + 1,
                    'name': lambda x: 'abc '+x[:3],
                    'job': lambda x: 'xyz '+x[:3]
                }
            )
        ]

    @pytest.fixture
    def config_rows_filtered(self) -> list:
        return [
            dict(
                func=load_data,
                kwargs={
                },
                obfuscators={
                    'id': lambda x: x + 1,
                    'name': lambda x: 'abc '+x[:3],
                    'job': lambda x: 'xyz '+x[:3]
                },
                rows_filter=rows_filter_func
            )
        ]

    def test_constructor(self):
        BaseGenerator()

    def test_generate_full(self, config: dict):
        generator = BaseGenerator()
        actual = generator.generate('case1', config)
        expected = textwrap.dedent('''\
        # automatically generated file, do not edit!
        
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
        
        
        ''')
        assert actual == expected

    def test_generate_rows_filter(self, config_rows_filtered: dict):
        generator = BaseGenerator()
        actual = generator.generate('case1', config_rows_filtered)
        print(f'\n------\n{actual}\n------')

        expected = textwrap.dedent('''\
        # automatically generated file, do not edit!
        
        import typing as t
        import pandas as pd
        import numpy as np
        from datetime import datetime
        
        
        def __fixture__case1_load_data() -> pd.DataFrame:
            df: pd.DataFrame = pd.DataFrame(columns=['id', 'name', 'job'])
            df['id'] = [33, 44]
            df['name'] = ['abc John', 'abc Alex']
            df['job'] = ['xyz dev', 'xyz qa']
            return df
        
        
        ''')

        assert actual == expected

import typing as t

import pandas as pd
import numpy as np
import re

from pandas.api.types import is_datetime64_any_dtype
from tqdm import tqdm
import autopep8

import importlib
import sys

class BaseGenerator:

    # TODO put it into config
    ISO_DATE_FORMAT = '%Y-%m-%d'

    def is_datetime(self, val: t.Any) -> bool:
        '''
        Test if given series or array is all of datetime kind

        :param val: pd.Series or np.ndarray
        :return: True if all items are datetime, False otherwise
        '''
        if type(val) in (np.ndarray, pd.Series):
            if val.dtype == object:
                val = val.fillna(pd.to_datetime('1970-01-01'))
                return bool(pd.to_datetime(val, errors='coerce').notnull().all())
            else:
                return is_datetime64_any_dtype(val)
        elif type(val) == pd.Timestamp:
            return True
        return False

    def format_scalar(self, scalar: t.Any) -> str:
        if self.is_datetime(scalar):
            return "'{}'".format(pd.to_datetime(scalar).strftime(self.ISO_DATE_FORMAT))
        return f"'{scalar}'" if type(scalar) == str else str(scalar)

    def format_column(self, column: pd.Series, compress: bool = True) -> str:
        data: str
        new_column: pd.Series
        is_dt: bool = self.is_datetime(column)

        if is_dt:
            column = pd.to_datetime(column).dt.strftime(self.ISO_DATE_FORMAT)

        if compress:
            new_column = column.drop_duplicates()
            if len(new_column) == 1:
                data = new_column.values[0]
                if type(data) == str:
                    data = f"'{data}'"
            else:
                data = str(column.to_list())
        else:
            data = str(column.to_list())

        if is_dt:
            data = f'pd.to_datetime({data})'

        return data

    def execute_case(self, case_name, func, obfuscators, rows_filter, *args, **kwargs):

        src = ''
        varname = 'data'
        vartype = 't.Any'

        value = func(*args, **kwargs)
        if type(value) == pd.DataFrame:
            varname = 'df'
            vartype = 'pd.DataFrame'

        src += f'def __fixture__{case_name}() -> {vartype}:\n'

        if vartype == 'pd.DataFrame':
            src += f'    {varname}: {vartype} = pd.DataFrame(columns={list(value.columns)})\n'

            if rows_filter:
                value = rows_filter(value).copy()

            if obfuscators:
                for col, obf_func in obfuscators.items():
                    value[col] = obf_func(value[col])

            for col in value.columns:
                data = self.format_column(value[col])
                src += f'    {varname}[\'{col}\'] = {data}\n'

        else:
            data = self.format_scalar(value)
            src += f'    {varname}: {vartype} = {data}\n'

        src += f'    return {varname}\n'
        text: str = autopep8.fix_code(src)
        return text

    def generate(self, case_name: str, config: dict) -> str:
        src: str = '# automatically generated file, do not edit!\n\n'
        src += 'import typing as t\n'
        src += 'import pandas as pd\n'
        src += 'import numpy as np\n'
        src += 'from datetime import datetime\n'
        src += '\n\n'

        tq = tqdm(config, desc='')
        for function in tq:
            func_spec = function['func']
            func_name = ''
            tq.set_description_str(str(func_spec))
            args = function.get('kwargs', {})
            obfuscators = function.get('obfuscators')
            rows_filter = function.get('rows_filter')
            func = None

            if type(func_spec) == str:
                path = func_spec.split('.')
                mod = importlib.import_module('.'.join(path[:-1]))
                func = getattr(mod, path[-1])
                # else:
                #     func = getattr(sys.modules[__name__], path[-1])
            elif callable(func_spec):
                func = func_spec
                func_name = re.findall(r'function ([._0-9A-Za-z]+)', repr(func))[0]
            else:
                raise ValueError(f'func {str(func_spec)} specification must be str or callable')

            assert func
            src += self.execute_case(case_name + '_' + func_name, func, obfuscators, rows_filter, **args) + '\n\n'

        return src

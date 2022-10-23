# df2fixture
Generate pytest fixtures from pandas DataFrames

## How to use

### Install
```bash
$ pip install git+https://github.com/pulsarcomet/df2fixture
```

### Import
```python
import pandas as pd
import df2fixture as dfx

def load_data():
    return pd.read_csv('sample.csv')


config = {
    'func': load_data
}

with open('tests/sample_test.py', 'w') as f:
    print(dfx.Generator().generate('case1', config), file=f)
```

## How to contribute


### Clone project

```bash
$ git clone https://github.com/pulsarcomet/df2fixture
$ cd df2fixture
```

### pip

#### Create virtualenv
Make sure python >= 3.7 version is installed!
```bash
$ sudo apt-get install virtualenv
$ vistualenv venv --python python3
$ pip install -r requirements.txt
```
#### Activate virtualenv
```bash
$ . venv/bin/activate
```

### conda
#### Create env
```bash
$ conda env create -f environment.yml
```
#### Activate conda env
```bash
$ conda activate conda-dfx-env
```

### Run tests
```bash
$ pytest tests
```

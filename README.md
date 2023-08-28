# Cryptocurrency Trading Bot response

Here you can see 

## Installing

```cmd
cd your/code/folder
git clone 
cd defi_response
python3.10 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Docs

Project tree:

defi_response
    |---- app
            |---- data
                    |---- prices.csv (does not load on git)
            |---- src
                    |---- use_cases.py
            |---- tests
                    |---- __init__.py
                    |---- all_test.py
            |---- utils
                    |---- __init__.py
                    |---- functions.py
            |---- __init__.py
    |---- main.py
    |---- .gitignore
    |---- README.md
    |---- requirements.txt


`data` folder contains csv file with stock information
`src` folder contains source code. In our example there you can find use cases for our tasks
`test` folder contains file with all tests for the functions
`utils` folder contains file with all functions that are requered to procceed the operations

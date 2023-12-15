# Simple Fake Data Utility

**Most** applications require data to be useful.

This project will make use of the Faker Python library to conveniently generate a pre-seeded fake data instance for a common purpose. Since most systems contain Users and their respective profiles, that is what we will demonstrate as a baseline although these models may be extended to cover additional attributes/properties to encapsulate more information.

## Why Python?

Python is a generic, glue language available for literally **ANY** operating system and it supports most popular current programming paradigms (functional, procedural, object-oriented, etc...). While that's not as big of a deal as it once was, it may also be installed in user space (via anaconda/miniconda installers) which typically doesn't require administrator privileges unlike most alternatives.

<!-- migrate sentiments about colleges and Java vs Python vs go vs other flavor of the week -->

### Faker Library

There are many implementations of the Faker library in various languages (C#, Ruby, PHP, Perl, Javascript, to name just a few), but Python seemed easier, more available, and most practical.

Additionally, Python has many libraries available for data science, analysis, and other activities which make it a premiere candidate for use.

## Setup

It is commonly suggested in Python to utilize `virtual environments`. 

I personally prefer a configuration which utilizes `pyenv` to manage multiple Python Versions in user space installations and then using the `pipenv` package as a secondary wrapper to manage each project's virtual environment and associated dependency graphs.

### (Possible) Pre-Requisite Installations

#### pyenv (optional)

For information about pyenv installation, [Check Here](https://github.com/pyenv/pyenv#installation)

#### pipenv (required unless you "circumvent")

To install pipenv, make certain that your system is using the correct Python version through pyenv and directly install it into the user environment packages with the command: `pip install pipenv` or `pip3 install pipenv` as it may vary based on operating system.

<!-- Does pipenv exist in conda-verse? pyenv in windows-verse?` -->

### Project Setup

First, the Faker package will need to be installed. In a new project that would be done with the following command: `pipenv install Faker`

Similarly, the pandas (panel data; a data science library) and openpyxl (for writing excel files) would need to be added: `pipenv install pandas openpyxl`

However, since this project already contains a Pipfile, this will be achieved by going to the `./src/app` directory and issuing the command: `pipenv install`

### Activate The Pipenv Virtual Environment

Activation of the pipenv virtual environment is achieved by navigating to the python project's directory `./src/app` (and/or the local directory of the Pipfile item) in a terminal and issuing the command: `pipenv shell`

### Running Main Program

By convention, most programs have a `main` method which instantiates and controls the applications "main" thread. 

In Python, this file is generally named 'app.py' or 'main.py' depending on the framework, However, there is also a magic/dunder method to identify if the file was directly run by the Python interpreter.

That bit of logic is observed in the `./src/app/main.py` file around line 15:

```python
# previous library imports and declarations removed for brevity
if __name__ == "__main__":
    # and so on and so forth
```

In order to run the program, your terminal session should be in the `./src/app` and the pipenv virtual environment should be active.

Running the program is done by issuing the command: `python main.py`

### Program Options

In the files `main.py` and `models/FakerClasses.py`, there are several hard-coded options which effect the runtime behavior of the script application.

In `main.py` these options are observed in the top-most portion of the file contents:

```python
# adjust the number of required entries to meet your data sampling needs
number_of_records = 100

# determine if tab-separated csv or excel output format
excel_file_format = 0

# ... and so on
```

Looking to the `models/FakerClasses.py` file beyond the imports:

```python
# seed to make our data reproducable
Faker.seed(0)

# add localization
f = Faker('en-US')

# ... and so on
```

The call to the .seed() method on the Faker object allows us to replicate the same dataset which will become more important when we begin to analyze the data for results comparison.


### Closing Remarks

For more information about the available Faker providers, [Click Here!](https://faker.readthedocs.io/en/master/providers.html)

For more information about pandas, [Click Here!](https://pandas.pydata.org/docs/)
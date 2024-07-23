# mujtaba-charm
This is a python package.


- [Project Description](#project-description)
- [Installation](#installation)
- [Usage Section](#usage-section)
- [Testing](#testing)

## Project Description
The project aims to provide a python package using poetry which has 3 sub-packages:
1. analysis
2. models
3. utils

## Installation
1. Install pytest:
```bash
poetry add --dev pytest
```

2. Ensure all dependencies, including pytest, are installed.
```bash
poetry install
```

## Usage Section
1. To clone GitHub repo:
```bash
git clone https://github.com/MujtabaNasir/mujtaba_charm.git
```

2. To install poetry with pip after cloning the repo:
```bash
pip install poetry
```

3. To create and switch to a new branch:
```bash
git checkout -b branch_uno
```

4. To push the new branch to GitHub:
```bash
git push -u origin branch_uno
```

5. To create a poetry package:
```bash
poetry new mujtaba_charm
```

6. Creating analysis, models and utils as sub packages in the main package mujtaba_charm
```bash
mkdir analysis
mkdir models
mkdir utils
```

7. To add __init__.py in sub packages of analysis, models and utils in order to make them python packages
```bash
touch analysis/__init__.py models/__init__.py utils/__init__.py
```

8. To use the hello funtion from the utils sub-package:
```
>>> from mujtaba_charm.utils import hello

>>> hello("john")
'hello john!'

>>> hellp()
'hello world!'
```

## Testing
1. To run the tests:
```
poetry run pytest
```
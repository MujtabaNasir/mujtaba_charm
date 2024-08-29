# mujtaba-charm
This is a python package.


- [Project Description](#project-description)
- [Installation](#installation)
- [Project Setup](#project-setup)
- [Usage Section](#usage-section)
- [Testing](#testing)

## Project Description
The project aims to provide a python package using poetry which has 3 sub-packages:
1. analysis
2. models
3. utils

## Installation
1. Install mujtaba-charm package using pip:
```bash
pip install git+https://github.com/MujtabaNasir/mujtaba-charm.git
```

2. Install a specific branch "branch_uno" from mujtaba-charm package using pip:
```bash
pip install git+https://github.com/MujtabaNasir/mujtaba-charm.git@branch_uno
```

## Project Setup
1. To clone GitHub repo:
```bash
git clone https://github.com/MujtabaNasir/mujtaba_charm.git
```

2. Navigate into the cloned repository:
```bash
cd mujtaba-charm
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

8. Install pytest:
```bash
poetry add --dev pytest
```

9. Ensure all dependencies, including pytest, pytest coverage, black, isort are installed.
```bash
poetry install
```

10. To build the python package and create dist directory with the built package files including .tar.gz source archive and a .whl binary wheel
```bash
poetry build
```

11. Install mujtaba-charm package using pip
```bash
pip install dist/mujtaba_charm-0.1.0-py3-none-any.whl
```

12. To install mujtaba-charm in editable mode
```bash
pip install -e .
```

13. Install black and isort using poetry
```bash
poetry add --dev black isort
```

14. Install coverage
```bash
poetry add --dev pytest coverage
```

15. Install pytest-cov
```bash
poetry add --dev pytest-cov
```

16. Install sphinx along with autodoc
```bash
poetry add --group dev sphinx sphinx-autodoc-typehints
```

17. Configure Sphinx to set up documentation
```bash
poetry run sphinx-quickstart
```

19. To generate documentation
```bash
poetry run sphinx-build -b html source _build/html
```

20. Install Core Dependencies
```bash
pip install -r requirements.txt
```

21. Install Development Dependencie
```bash
pip install -r dev-requirements.txt
```

## Usage Section
1. To use the hello funtion from the utils sub-package:
```
>>> from mujtaba_charm.utils import hello

>>> hello("john")
'hello john!'

>>> hello()
'hello world!'

>>> hello(2024)
TypeError: int is not allowed, name should be of string type
```

2. To run black and isort using poetry
```bash
poetry run black .
poetry run isort .
```

## Testing
1. To run the tests along with pytest coverage:
```
poetry run pytest
```

# mujtaba-charm
This is a python package.


- [Project Description](#project-description)
- [Installation](#installation)
- [Usage Section](#usage-section)

## Project Description
The project aims to provide a python package using poetry which has 3 sub-packages:
1. analysis
2. models
3. utils

## Installation
1. To install poetry:
```
pip install poetry
```

## Usage Section
1. To clone GitHub repo:
```
git clone https://github.com/MujtabaNasir/mujtaba_charm.git
```

2. To create and switch to a new branch:
```
git checkout -b branch_uno
```

3. To push the new branch to GitHub:
```
git push -u origin branch_uno
```

4. To create a poetry package:
```
poetry new mujtaba_charm
```

5. Creating analysis, models and utils as sub packages in the main package mujtaba_charm
```
mkdir analysis
mkdir models
mkdir utils
```

6. To add __init__.py in sub packages of analysis, models and utils in order to make them python packages
```
touch analysis/__init__.py models/__init__.py utils/__init__.py
```
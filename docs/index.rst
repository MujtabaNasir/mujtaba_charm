.. mujtaba-charm documentation master file, created by
   sphinx-quickstart on Mon Jul 29 20:29:21 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to mujtaba-charm's documentation!
===========================

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

Project Description
-------------------
The project aims to provide a python package using pip which has 3 sub-packages:

1. analysis
2. models
3. utils

Installation
------------
1. Install mujtaba-charm package using pip:

   .. code-block:: bash

      pip install git+https://github.com/MujtabaNasir/mujtaba-charm.git

2. Install a specific branch "branch_uno" from mujtaba-charm package using pip:

   .. code-block:: bash

      pip install git+https://github.com/MujtabaNasir/mujtaba-charm.git@branch_uno

Project Setup
-------------
1. To clone GitHub repo:

   .. code-block:: bash

      git clone https://github.com/MujtabaNasir/mujtaba_charm.git

2. Navigate into the cloned repository:

   .. code-block:: bash

      cd mujtaba-charm

3. To create and switch to a new branch:

   .. code-block:: bash

      git checkout -b branch_uno

4. To push the new branch to GitHub:

   .. code-block:: bash

      git push -u origin branch_uno

5. Install pytest:

   .. code-block:: bash

      pip install pytest

6. Install all core dependencies:

   .. code-block:: bash

      pip install -r requirements.txt

7. Install development dependencies:

   .. code-block:: bash

      pip install -r dev-requirements.txt

Usage Section
-------------
1. To use the hello function from the utils sub-package:

   .. code-block:: python

      from mujtaba_charm.utils import hello

      hello("john")  # 'hello john!'

      hello()  # 'hello world!'

      hello(2024)  # TypeError: int is not allowed, name should be of string type

Testing
-------
1. To run the tests along with pytest coverage:

   .. code-block:: bash

      pytest --cov=mujtaba_charm
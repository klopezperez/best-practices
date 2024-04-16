Getting Started
===============

This page details how to get started with molecool. 

Installation
------------
To install molecool, you will need to an environment with Python 3.7 or greater with the following packages:

* Python 3.11
* Numpy
* Matplotlib

Once you have these, you can install molecool using pip:

.. code-block:: bash

    pip install -i https://test.pypi.org/simple/ molecool

Usage 
-----
Here is an example of using molecool to visualize a molecule:

.. code-block:: python 
    
    import molecool

    symbols, coordinates = molecool.open_pdb('water.pdb')

    print(symbols)
    print(coordinates)
Geometry3
=========

|pypi| |license| |python|

**Geometry3** is a Python 3.7 package that provides 


TL;DR
-----

1. Clone the repo and install

.. code:: bash

          $ git clone https://github.com/JnyJny/Geometry3.git
          $ cd Geometry3
	  $ pip3 install -r requirements.txt
	  
1. Install with pip

.. code:: bash

	  $ pip3 install -U geometry3
	  

Uninstall with pip:

.. code:: bash

	  $ pip3 uninstall geometry3

Usage
-----

Once installed, 

.. code:: python

	from Geometry3 import Point

	o = Point()
	p = Point(1,1,1)
	o.is_origin == True
	p.is_origin == False
	p.distance(o)
	p.midpoint(o)


.. |pypi| image:: https://img.shields.io/pypi/v/geometry3.svg?style=flat-square&label=version
    :target: https://pypi.org/pypi/geometry3
    :alt: Latest version released on PyPi


.. |python| image:: https://img.shields.io/pypi/pyversions/geometry3.svg?style=flat-square
   :target: https://pypi.org/project/geometry3/
   :alt: Python Versions	  

.. |license| image:: https://img.shields.io/badge/license-apache-blue.svg?style=flat-square
    :target: https://github.com/jnyjny/geometry3/blob/master/LICENSE
    :alt: Apache license version 2.0  




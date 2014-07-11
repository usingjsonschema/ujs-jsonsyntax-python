=================
JSON Syntax Check
=================

.. image:: https://travis-ci.org/usingjsonschema/ujs-jsonsyntax-python.svg?branch=master
    :target: https://travis-ci.org/usingjsonschema/ujs-jsonsyntax-python

Part of the
`Using JSON Schema <http://usingjsonschema.github.io>`_
project.

The 'hello world' of JSON processing, check the syntax of a JSON file.

For command line/script use, a console message is displayed and the process
exits with 0 for success, 1 for failure.

Command Line / Script Use
-------------------------
Usage: jsonsyntax filename
- filename name of file to check (path optional)

To run the syntax checker (command line or script) against the file
``example.json`` use,

.. code-block:: bash

    jsonsyntax example.json

Library Function Use
--------------------
To use the syntax checker as a library function, call the ``syntaxCheck``
function in a try/except block. For example,

.. code-block:: python

    from jsonsyntax import checkSyntax
    try :
        checkSyntax ("example.json")
        print ("Valid JSON file")
    except as e:
        print ("Error: " + e.message);

Install
-------
Installation using pip for Python 2 (2.7) or Python 3.

.. code-block:: bash

    pip install ujs-jsonsyntax

License
-------
MIT
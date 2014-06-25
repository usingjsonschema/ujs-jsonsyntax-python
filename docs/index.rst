==========
jsonsyntax
==========

``jsonsyntax`` is a simple library and command line script to check the
syntax of a JSON file.

Command line usage

.. code-block:: bash

    jsonsyntax filename

Library usage

.. code-block:: python

    from jsonsyntax import checkSyntax, CheckSyntaxError

    try:
        checkSyntax ("valid.json")
        print ("JSON content is valid")
    except CheckSyntaxError as e:
        print ("Error " + str (e))

The jsonsyntax program is hosted on GitHub in this
`repository <https://github.com/usingjsonschema/ujs-jsonsyntax-python/>`_.

Contents:

.. toctree::
   :maxdepth: 4

   jsonsyntax


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


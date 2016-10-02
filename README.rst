========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |codecov|
        | |landscape|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/python-rfcmx/badge/?style=flat
    :target: https://readthedocs.org/projects/python-rfcmx
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/joyinsky/python-rfcmx.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/joyinsky/python-rfcmx

.. |requires| image:: https://requires.io/github/joyinsky/python-rfcmx/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/joyinsky/python-rfcmx/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/joyinsky/python-rfcmx/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/joyinsky/python-rfcmx

.. |landscape| image:: https://landscape.io/github/joyinsky/python-rfcmx/master/landscape.svg?style=flat
    :target: https://landscape.io/github/joyinsky/python-rfcmx/master
    :alt: Code Quality Status

.. |version| image:: https://img.shields.io/pypi/v/rfcmx.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/rfcmx

.. |downloads| image:: https://img.shields.io/pypi/dm/rfcmx.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/rfcmx

.. |wheel| image:: https://img.shields.io/pypi/wheel/rfcmx.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/rfcmx

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/rfcmx.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/rfcmx

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/rfcmx.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/rfcmx


.. end-badges

A Python Package to validate and generate Mexican codes (RFC, CURP)

* Free software: BSD license

Installation
============

::

    pip install rfcmx

Documentation
=============

https://python-rfcmx.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

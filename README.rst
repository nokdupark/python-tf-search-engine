========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-tf-search-engine/badge/?style=flat
    :target: https://readthedocs.org/projects/python-tf-search-engine
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/ionelmc/python-tf-search-engine.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ionelmc/python-tf-search-engine

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/ionelmc/python-tf-search-engine?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/ionelmc/python-tf-search-engine

.. |requires| image:: https://requires.io/github/ionelmc/python-tf-search-engine/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/ionelmc/python-tf-search-engine/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/ionelmc/python-tf-search-engine/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/ionelmc/python-tf-search-engine

.. |version| image:: https://img.shields.io/pypi/v/tf-search-engine.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/tf-search-engine

.. |wheel| image:: https://img.shields.io/pypi/wheel/tf-search-engine.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/tf-search-engine

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/tf-search-engine.svg
    :alt: Supported versions
    :target: https://pypi.org/project/tf-search-engine

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/tf-search-engine.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/tf-search-engine

.. |commits-since| image:: https://img.shields.io/github/commits-since/ionelmc/python-tf-search-engine/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/ionelmc/python-tf-search-engine/compare/v0.0.0...master



.. end-badges

An example package. Generated with cookiecutter-pylibrary.

* Free software: MIT license

Installation
============

::

    pip install tf-search-engine

You can also install the in-development version with::

    pip install https://github.com/ionelmc/python-tf-search-engine/archive/master.zip


Documentation
=============


https://python-tf-search-engine.readthedocs.io/


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

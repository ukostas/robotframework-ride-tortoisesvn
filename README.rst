TortoiseSVN plugin for RIDE (robotframework IDE)
================================================

.. contents::
   :local:

TortoiseSVN plugin for RIDE(robotframework IDE) adds additional menu item to trigger TortoiseSVN (it has to be installed separately) commands.
So that RIDE users can update/commit/etc. directly from RIDE.

For more information about TortoiseSVN automation, see http://tortoisesvn.net/docs/release/TortoiseSVN_en/tsvn-automation.html.

For more information about Robot Framework and the ecosystem, see http://robotframework.org.

- Main menu
    .. image:: pics/main_menu.png
        :alt: Main menu

- Tree context menu
    .. image:: pics/context_menu.png
        :alt: Tree context menu

Installation
------------

If you already have Python_ with `pip <http://pip-installer.org>`_ installed,
you can simply run::

    pip install robotframework-ride-tortoisesvn

Alternatively you can get TortoiseSVN plugin source code by downloading the source
distribution from PyPI_ and extracting it, or by cloning the project repository
from GitHub_. After that you can install the framework with::

    python setup.py install

.. _Python: http://python.org
.. _GitHub: https://github.com/ukostas/robotframework-ride-tortoisesvn
.. _PyPI: https://pypi.python.org/pypi/robotframework-ride-tortoisesvn
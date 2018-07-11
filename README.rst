Akt: python virtual environment activation done right
#####################################################

**Akt is still a work in progress, please be patient.**

Run a command inside a virtualenv.  *Akt* is an alternative to :code:`source
<virtualenv>/bin/activate` that does not touch the current environment, but
forks a new process in the virtualenv.  You can think of *Act* like you would
:code:`sudo`, but instead of running a command as another user, *Akt* runs a
command in another Python environment.

*Akt* is a direct alternative to |Vex|_.  However, while |Vex|_ focuses on out of
project virtual environments *Akt* focuses on in project virtual environments.
*Akt* can be run from the main directory or any sub directory of a project that
has a virtualenv at its root and will use the project's virtualenv.

*Akt* does not attempt to replace :code:`virtualenv` or :code:`python -m venv`
but only picks up where they left off by offering an easy way to enter and exit
virtualenv's and to run commands in those environments.

.. _Vex: https://github.com/sashahart/vex

.. |Vex| replace:: *Vex*

.. _PyPI: https://pypi.org/

Installation
------------

There are three ways to install *Akt*, from PyPI_, from source, or using the
single file script.  The latter is useful if you don't have a full Python
installation and just need to place a script somewhere.


From PyPI_
^^^^^^^^^^

*Akt will be comming to PyPI soon, until then, install from source.*

.. code:: sh

    $ pip install akt


From Source
^^^^^^^^^^^

.. code:: sh

    $ pip install git+git://github.com/mrshannon/akt.git


Single File Script
^^^^^^^^^^^^^^^^^^

*Akt single file comming soon, until then, install from source.*

.. code:: sh

    $ curl -O https://raw.githubusercontent.com/mrshannon/akt/singlefile/akt
    $ chmod +x akt

Then you can move the script to wherever is convenient.


Usage
-----

First you need a virtualenv, if you already have one (preferably in you project
root) then congratulations, you may begin using *Akt* immediately.  If you don't
already have one you can create one with:

.. code:: sh

    $ virtualenv <env>          # for python 2.x
    $ python3 -m venv <env>     # for python 3.x

where :code:`<env>` is the name of the new environment.

.. note::

    While it is possible to use :code:`virtualenv3` to create a Python 3.x
    virtualenv the :code:`venv` module provided by the standard library is
    recommended as it does not need to make a separate install of setuptools or
    pip.

Now that you have a virtualenv, simply call :code:`akt` from any directory
which itself or any of it's parents contains the virtualenv.

.. code:: sh

    $ akt

which will open up a new shell (should work for all shells).  You can also
specify a command to run.

.. code:: sh

    $ akt pip install sphinx

*Akt* will search the current directory and all parents until it reaches the
root filesystem for a virtualenv and open a shell or run the given command in
that virtualenv's context.

If you need to specify a virtualenv you can use the :code:`-e` or
:code:`--environment` flags.

.. code:: sh

    $ akt -e $HOME/.virtualenv/dev 

If you want to use a virtualenv that is not in the project's root then you can
place a :code:`.aktrc` file in the project root that contains a relative or
absolute path to the virtualenv you wish to use.  Therefore, to use the
virtualenv above without the :code:`-e` flag, place a :code:`.aktrc` file in
the project's root directory containing:

.. code::

    $HOME/.virtualenv/dev


Frequently Asked Questions
--------------------------

.. **Why does Akt leave a .akt file beside my virtualenv directory?**
..
.. *Akt* must work it's way up the file system to find the virtualenv.  To do this
.. it must check every directory along it's way to see if it is a virtualenv.  If
.. your project is small this does not take much time.  However, if you are
.. working on a large project with many nested directories this can take awhile.
..
.. In order to avoid having to do this expensive traversal *Akt* will place a
.. :code`.akt` file in the same directory the virtualenv is contained in.  The
.. file will contain the name of the virtualenv.  When *Akt* is searching for a
.. virtualenv it will first try to find a .akt file, if it finds one it will
.. use the virtualenv listed in the file.

**Why use Akt instead of sourcing the activate script in the virtualenv?**

Simple, *Akt* does not mess with the ENVIRONMENT of your current shell. When
the called command, or invoked shell exits you will be returned to the same
shell you executed *Akt* from.

**Why use Akt instead of virtualenvwrapper?**

*virtualenvwrapper* provides management tools on top of *virtualenv* but it
still modifies the existing ENVIRONMENT.  *Akt* on the other hand does not
change the current environment and therefore it is failsafe, if the called
program crashes you will be returned to the shell that invoked *Akt* with your
environment exactly how you left it.

**Isn't Akt the same as Vex then?**

Yes, they are very similar.  However, *Akt* differs in two ways.

1. *Akt* is built around a workflow involving virtualenv's in the project
   directory and not in a centralized directory in the user's :code:`$HOME`.
   Therefore, *Akt* can use a virtualenv outside of a centralized directory
   without requiring the user to specify a path.
2. *Akt* is much simpler than |Vex|_.  |Vex|_ attempts to replace
   *virtualenvwrapper* and thus it encompasses environment creation,
   management, and activation, *Akt* only runs a command inside the first
   virtualenv it finds.

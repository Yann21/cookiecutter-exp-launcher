Cookiecutter PyPackage
======================

![image](https://pyup.io/repos/github/audreyfeldroy/cookiecutter-pypackage/shield.svg%0A%20:target:%20https://pyup.io/repos/github/audreyfeldroy/cookiecutter-pypackage/%0A%20:alt:%20Updates)

![image](https://travis-ci.org/audreyfeldroy/cookiecutter-pypackage.svg?branch=master%0A%20:target:%20https://travis-ci.org/github/audreyfeldroy/cookiecutter-pypackage%0A%20:alt:%20Build%20Status)

![image](https://readthedocs.org/projects/cookiecutter-pypackage/badge/?version=latest%0A%20:target:%20https://cookiecutter-pypackage.readthedocs.io/en/latest/?badge=latest%0A%20:alt:%20Documentation%20Status)

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template
for a Python package.

-   GitHub repo:
    <https://github.com/audreyfeldroy/cookiecutter-pypackage/>
-   Documentation: <https://cookiecutter-pypackage.readthedocs.io/>
-   Free software: BSD license

Features
--------

-   Testing setup with `unittest` and `python setup.py test` or `pytest`
-   [TravisCCI](http://travis-ci.org/): Ready for Travis Continuous
    Integration testing
-   [Tox](http://testrun.org/tox/) testing: Setup to easily test for
    Python 3.6, 3.7, 3.8
-   [Sphinx](http://sphinx-doc.org/) docs: Documentation ready for
    generation with, for example, [Read the
    Docs](https://readthedocs.io/)
-   [bump2version](https://github.com/c4urself/bump2version):
    Pre-configured version bumping with a single command
-   Auto-release to [PyPI](https://pypi.python.org/pypi) when you push a
    new tag to master (optional)
-   Command line interface using Click (optional)

Build Status
------------

Linux:

![image](https://img.shields.io/travis/audreyfeldroy/cookiecutter-pypackage.svg%0A%20:target:%20https://travis-ci.org/audreyfeldroy/cookiecutter-pypackage%0A%20:alt:%20Linux%20build%20status%20on%20Travis%20CI)

Windows:

![image](https://ci.appveyor.com/api/projects/status/github/audreyr/cookiecutter-pypackage?branch=master&svg=true%0A%20:target:%20https://ci.appveyor.com/project/audreyr/cookiecutter-pypackage/branch/master%0A%20:alt:%20Windows%20build%20status%20on%20Appveyor)

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this
requires Cookiecutter 1.4.0 or higher):

    pip install -U cookiecutter

Generate a Python package project:

    cookiecutter https://github.com/audreyfeldroy/cookiecutter-pypackage.git

Then:

-   Create a repo and put it there.
-   Add the repo to your [TravisCCI](http://travis-ci.org/) account.
-   Install the dev requirements into a virtualenv.
    (`pip install -r requirements_dev.txt`)
-   [Register](https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives)
    your project with PyPI.
-   Run the Travis CLI command `travis encrypt --add deploy.password` to
    encrypt your PyPI password in Travis config and activate automated
    deployment on PyPI when you push a new tag to master branch.
-   Add the repo to your [Read the Docs](https://readthedocs.io/)
    account + turn on the Read the Docs service hook.
-   Release your package by pushing a new tag to master.
-   Add a `requirements.txt` file that specifies the packages you will
    need for your project and their versions. For more info see the [pip
    docs for requirements
    files](https://pip.pypa.io/en/stable/user_guide/#requirements-files).
-   Activate your project on [pyup.io](https://pyup.io/).

For more details, see the [cookiecutter-pypackage
tutorial](https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html).

Not Exactly What You Want?
--------------------------

Don't worry, you have options:

### Similar Cookiecutter Templates

-   [Nekroze/cookiecutter-pypackage](https://github.com/Nekroze/cookiecutter-pypackage):
    A fork of this with a PyTest test runner, strict flake8 checking
    with Travis/Tox, and some docs and `setup.py` differences.
-   [tony/cookiecutter-pypackage-pythonic](https://github.com/tony/cookiecutter-pypackage-pythonic):
    Fork with py2.7+3.3 optimizations. Flask/Werkzeug-style test runner,
    `_compat` module and module/doc conventions. See `README.rst` or the
    [github comparison
    view](https://github.com/tony/cookiecutter-pypackage-pythonic/compare/audreyr:master...master)
    for exhaustive list of additions and modifications.
-   [ardydedase/cookiecutter-pypackage](https://github.com/ardydedase/cookiecutter-pypackage):
    A fork with separate requirements files rather than a requirements
    list in the `setup.py` file.
-   [lgiordani/cookiecutter-pypackage](https://github.com/lgiordani/cookiecutter-pypackage):
    A fork of Cookiecutter that uses
    [Punch](https://github.com/lgiordani/punch) instead of
    [bump2version](https://github.com/c4urself/bump2version) and with
    separate requirements files.
-   [briggySmalls/cookiecutter-pypackage](https://github.com/briggySmalls/cookiecutter-pypackage):
    A fork using [Poetry](https://python-poetry.org/) for neat package
    management and deployment, with linting, formatting, no makefiles
    and more.
-   [veit/cookiecutter-namespace-template](https://github.com/veit/cookiecutter-namespace-template):
    A cookiecutter template for python modules with a namespace
-   [zillionare/cookiecutter-pypackage](https://zillionare.github.io/cookiecutter-pypackage/):
    A template containing [Poetry](https://python-poetry.org/),
    [Mkdocs](https://pypi.org/project/mkdocs/), Github CI and many more.
    It's a template and a package also (can be installed with pip)
-   [waynerv/cookiecutter-pypackage](https://waynerv.github.io/cookiecutter-pypackage/):
    A fork using [Poetry](https://python-poetry.org/),
    [Mkdocs](https://pypi.org/project/mkdocs/),
    [Preccommit](https://pre-commit.com/),
    [Black](https://black.readthedocs.io/en/stable/) and
    [Mypy](https://mypy.readthedocs.io/en/stable/). Run test, staging
    and release workflows with GitHub Actions, automatically generate
    release notes from CHANGELOG.
-   Also see the
    [network](https://github.com/audreyr/cookiecutter-pypackage/network)
    and [family
    tree](https://github.com/audreyr/cookiecutter-pypackage/network/members)
    for this repo. (If you find anything that should be listed here,
    please add it and send a pull request!)

### Fork This / Create Your Own

If you have differences in your preferred setup, I encourage you to fork
this to create your own version. Or create your own; it doesn't strictly
have to be a fork.

-   Once you have your own version working, add it to the Similar
    Cookiecutter Templates list above with a brief description.
-   It's up to you whether or not to rename your fork/own version. Do
    whatever you think sounds good.

### Or Submit a Pull Request

I also accept pull requests on this, if they're small, atomic, and if
they make my own packaging experience better.

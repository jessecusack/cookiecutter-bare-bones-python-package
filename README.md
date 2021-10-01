# Bare-Bones Python Package

A bare-bones cookiecutter template for a python package. It avoids all the best-practices including testing frameworks, CI and documentation generation in an effort to keep things as simple as possible. 

## Requirements

* [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html)

You can install [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) easily with [conda](https://conda.io/en/latest/).

``` bash
conda install -c conda-forge cookiecutter
```

## Quickstart

To create a new package, run:

``` bash
cookiecutter gh:jessecusack/cookiecutter-bare-bones-python-package
```

> this should be run from the location that you want the project folder to live, or you will need to move the directory around later

If you have previously created a package with this template confirm the prompt to redownload the newest version.
The installation dialog will ask for a few inputs:
* `full_name`: Your name.
* `email`: Your email.
* `project_name`: The name of the project which is also the name of the directory if will be created in (whitespaces will be replaced with underscores).
* `description`: A short description of the project for the readme.
* `create_author_file`: To include an `AUTHOR.md` file. 
* `open_source_license`: Choose a license for your project.

> Unfortunately there seems to be a bug that does [not allow backspace](https://github.com/audreyr/cookiecutter/issues/875) in cookiecutter on certain platforms. If you make a typo cancel the input `ctrl+c` and start over again.

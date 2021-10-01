import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

    
if not '{{cookiecutter.create_author_file}}' == 'y':
    remove('AUTHORS.md')
    
if '{{ cookiecutter.open_source_license }}' == 'Not open source':
    remove('LICENSE')
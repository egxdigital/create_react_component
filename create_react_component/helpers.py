"""Helpers

Copyright (c) 2020, Emille Giddings
All rights reserved.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

import os

import shutil

from typing import List

def lowercase_string_list(li: List[str]) -> List[str]:
    """Takes a list of strings and returns a list 
    of the same strings in lowercase"""
    return list(map(lambda x : x.lower(), li))


def create_directory(name: str) -> None:
    """Takes a name as a string and creates a 
    directory in the current directory"""
    try:
        os.mkdir(name)
    except OSError as err:
        print(f'Something went wrong: {err}')
        
    except FileExistsError as e:
        print (f'Component already exists. Ignoring {name}')
        return False
    else:
        print(f'Created directory \'{name}\' in current directory')
        return True


def remove_directory(name: str) -> None:
    """Takes a name as a string and creates a 
    directory in the current directory"""
    try:
        shutil.rmtree(name)
    except Exception as e:
        print(e)
        return False
    else:
        print(f'Removed directory \'{name}\' in current directory')
        return True


def create_file(name: str, content: str) -> None:
    with open(f'{name}', 'w+') as f:
        f.write(content)


def remove_file(name: str) -> None:
    """Takes a name as a string and removes a file in the
    current directory"""
    try:
        os.remove(name)
    except Exception as e:
        print(e)
        return False
    else:
        print(f'Removed file \'{name}\' in current directory')
        return True

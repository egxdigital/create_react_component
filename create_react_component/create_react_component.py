#!/usr/bin python
"""Create React Component

Creates a React component according to an opinionated convention
That uses an index.js and a meaningful file name to store the
component's declaration.

Examples
     $ python -m create_react_component Button
     $ python -m create_react_component Button Menu Nav
     $ python -m create_react_component @args.txt
     $ python -m create_react_component --test Button Timer Menu

Copyright (c) 2020, Emille Giddings
All rights reserved.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.

"""
import os

import argparse

from create_react_component.helpers import create_directory, lowercase_string_list, create_file

def hasComponents() -> None:
    """Returns true if the current directory has components/"""
    return 'components' in lowercase_string_list(os.listdir('.'))

def _createComponentModule(name: str, content:str) -> None:
    """Takes a module name and content and creates several files
    inside components/"""
    create_file(name, content)
    

def _createComponent(c: str, options: dict) -> None:
    """Takes a component name as a string and creates
    a directory in components/ of the same name"""
    c = c.capitalize()
    create_directory(f'components/{c}')
    _createComponentModule(
        f'components/{c}/index.js', f"import React from 'react'\nimport './{c}'")
    _createComponentModule(
        f'components/{c}/{c}.js', f"import React from 'react'\nimport './{c}.css'")
    _createComponentModule(
        f'components/{c}/{c}.css', '')

    if options:
        if options.get('test'):
            print(f'Creating a unit test module for the {c} component')
            _createComponentModule(
                f'components/{c}/{c}.test.js', '')


def main():
    # check for components/
    if not hasComponents():
        print("No components folder detected in the current directory")
        return

    my_parser = argparse.ArgumentParser(prog='create-react-component',
                                        fromfile_prefix_chars='@',
                                        usage='%(prog)s [options] path',
                                        description='Create a React component',
                                        epilog='Enjoy the program! :)')

    my_parser.add_argument('Component',
                           metavar='component',
                           type=str,
                           nargs='*',
                           help='the name of the component')

    my_parser.add_argument('-t', '--test', action='store_true',
                           required=False, help='add unit test module to component')

    args = my_parser.parse_args()

    components = args.Component
    options = vars(args)

    for component in components:
        _createComponent(component, options)


if __name__ == '__main__':
    main()


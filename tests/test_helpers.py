import unittest

import os

from create_react_component.helpers import *


class TestHelpers(unittest.TestCase):

    def test_lowercase_string_list(self):
        self.assertEqual(lowercase_string_list(
            ["Apple", "ORANGE", "Grape"]), ["apple", "orange", "grape"])


    def test_create_directory(self):
        create_directory('components')
        self.assertIn('components', os.listdir())
        remove_directory('components')

    
    def test_remove_directory(self):
        create_directory('components')
        self.assertIn('components', os.listdir())
        remove_directory('components')
        self.assertNotIn('components', os.listdir())


    def test_create_file(self):
        create_file('Button.js', 'import react\nimport Button.css')
        self.assertIn('Button.js', os.listdir('.'))        
        with open('Button.js', 'r') as f:
            contents = f.read()        
        self.assertEqual(contents, 'import react\nimport Button.css')
        remove_file('Button.js')

    
    def test_remove_file(self):
        create_file('Button.js', 'import react\nimport Button.css')
        self.assertIn('Button.js', os.listdir('.'))
        remove_file('Button.js')
        self.assertNotIn('Button.js', os.listdir('.'))


if __name__ == '__main__':
    unittest.main()

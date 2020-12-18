import unittest

import os

from create_react_component.helpers import *
from create_react_component.create_react_component import hasComponents, _createComponent, _createComponentModule


class CreateReactComponent(unittest.TestCase):
    def setUp(self):
        create_directory('components')

    def tearDown(self):
        remove_directory('components')

    def test_hasComponents(self):        
        self.assertEqual(hasComponents(), True)
            
    def test_createComponent(self):
        dir = 'components/Button'
        _createComponent('Button', {})
        self.assertIn('Button', os.listdir('components'))
        self.assertIn('index.js', os.listdir(dir))
        self.assertIn('Button.js', os.listdir(dir))
        self.assertIn('Button.css', os.listdir(dir))
        

    def test_createComponentModule(self):        
        _createComponent('Button', {})
        _createComponentModule('components/Button/Button.js',
                               'import react\nimport Button.css')
        self.assertIn('Button.js', os.listdir('./components/Button'))



if __name__ == '__main__':
    unittest.main()

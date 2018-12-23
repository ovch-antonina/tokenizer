import unittest
from indexator import index_shelve

class IndexatorTest(unittest.TestCase):
    '''tests for indexator.py'''

    def test_regular(self):
        '''
        tests a string with mixed alphabetical symbols, numbers, whitespaces, 
        and punctuation
        '''
        shelf = index_shelve('one two three 1 2 3 !!!')
        self.assertEqual(len(list(shelf.keys())), 6)
        self.assertEqual(shelf['0'].symboltype, 'letter')
        self.assertEqual(shelf['5'].symboltype, 'digit')
        
    def test_typeError(self):
        '''
        tests how the tokenizer handles receiving an integer instead of a string
        as input
        '''
        with self.assertRaises(TypeError):
             index_shelve(123)
    
    def test_emptyString(self):
        '''
        tests how the tokenizer handles receiving an empty string as input
        '''
        with self.assertRaises(TypeError):
             index_shelve('')
             
if __name__ == '__main__':
    unittest.main()
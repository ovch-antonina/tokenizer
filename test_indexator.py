import unittest
from indexator_updated import Position, index_shelve

class IndexatorTest(unittest.TestCase):
    '''tests for indexator.py'''

    def test_regular(self):
        '''
        tests an input file with several tokens, no repeating tokens
        '''
        shelf = index_shelve("input1.txt", "output_shelf.db")
        keys_list = []
        text_list = []
        for key in shelf.keys():
            keys_list.append(key)
            dic = shelf[key]
            for key2 in dic.keys():
                text_list.append(key2)
        self.assertEqual(len(keys_list), 6)
        self.assertEqual(keys_list[0], 'one')
        self.assertEqual(text_list[1], 'input1.txt')
        
    def test_two_files(self):
        '''
        tests two input files with several tokens, some repeating
        '''
        shelf = index_shelve("input1.txt", "output_shelf_2.db")
        shelf = index_shelve("input2.txt", "output_shelf_2.db")
        keys_list = []
        text_list = []
        for key in shelf.keys():
            keys_list.append(key)
            dic = shelf[key]
            for key2 in dic.keys():
                text_list.append(key2)
        self.assertEqual(len(keys_list), 6)
        self.assertEqual(keys_list[0], 'one')
        self.assertEqual(text_list[1], 'input2.txt')
        
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
# -*- coding: utf-8 -*-
import unittest
from tokenizer import Token, Tokenizer

class TokenizerTest(unittest.TestCase):
    '''tests for tokenizer.py'''
    
    def test_regular(self):
        '''
        tests a string with mixed alphabetical symbols, numbers, and whitespaces
        '''
        tokens = Tokenizer.tokenize('3fff dsl f')
        self.assertEqual(len(tokens), 3)
        self.assertEqual(tokens[0].position, 1)
        self.assertEqual(tokens[0].substring, 'fff')
        self.assertEqual(tokens[2].position, 9)
        self.assertEqual(tokens[2].substring, 'f')
        
    def test_typeError(self):
        '''
        tests how the tokenizer handles receiving an integer instead of a string
        as input
        '''
        with self.assertRaises(TypeError):
            Tokenizer.tokenize(123)

    def test_whitespaces(self):
        '''
        tests a string that starts and ends with a whitespace and has multiple
        whitespaces in a row
        '''
        tokens = Tokenizer.tokenize(' white  space ')
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].position, 1)
        self.assertEqual(tokens[0].substring, 'white')
        self.assertEqual(tokens[1].position, 8)
        self.assertEqual(tokens[1].substring, 'space')       
        
    def test_punctiation(self):
        '''
        tests a string with several puctuation marks
        '''
        tokens = Tokenizer.tokenize(';.^punctuation!:)')
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].position, 3)
        self.assertEqual(tokens[0].substring, 'punctuation')
        
    def test_noLetters(self):
        '''
        tests a string that contains no alphabetical symbols
        '''
        tokens = Tokenizer.tokenize('1...2! 3?')
        self.assertEqual(len(tokens), 0)
        
    def test_accentedLetters(self):
        '''
        tests a string that contains accented letters
        '''
        tokens = Tokenizer.tokenize('Àá... ÂãÄ!')
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].position, 0)
        self.assertEqual(tokens[0].substring, 'Àá')
        self.assertEqual(tokens[1].position, 6)
        self.assertEqual(tokens[1].substring, 'ÂãÄ')
        
if __name__ == '__main__':
    unittest.main()

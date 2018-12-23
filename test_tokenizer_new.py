# -*- coding: utf-8 -*-
import unittest
from tokenizer_new import Token, Tokenizer

class TokenizerTest(unittest.TestCase):
    '''tests for tokenizer_new.py'''
    
    def test_regular(self):
        '''
        tests a string with mixed alphabetical symbols, numbers, whitespaces, 
        and punctuation
        '''
        tokens = Tokenizer.tokenize('is this working 123 !')
        self.assertEqual(len(tokens), 9)
        self.assertEqual(tokens[0].position, 0)
        self.assertEqual(tokens[0].substring, 'is')
        self.assertEqual(tokens[0].symboltype, 'letter')
        self.assertEqual(tokens[8].position, 20)
        self.assertEqual(tokens[8].substring, '!')
        self.assertEqual(tokens[8].symboltype, 'punctuation')
        
    def test_typeError(self):
        '''
        tests how the tokenizer handles receiving an integer instead of a string
        as input
        '''
        with self.assertRaises(TypeError):
            Tokenizer.tokenize(123)      
            
    def test_emptyString(self):
        '''
        tests how the tokenizer handles receiving an empty string
        '''
        with self.assertRaises(TypeError):
            Tokenizer.tokenize('')

    def test_onesymbol(self):
        '''
        tests a string that has only one symbol
        '''
        tokens = Tokenizer.tokenize('a')
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].substring, 'a')
        
    def test_punctiation(self):
        '''
        tests a string with several puctuation marks
        '''
        tokens = Tokenizer.tokenize(';.punctuation!:)')
        self.assertEqual(len(tokens), 3)
        self.assertEqual(tokens[1].position, 2)
        self.assertEqual(tokens[1].substring, 'punctuation')
        
    def test_othertype(self):
        '''
        tests a string that contains symbols other than letters, digits, 
        whitespaces or punctuation
        '''
        tokens = Tokenizer.tokenize('^_^')
        self.assertEqual(len(tokens), 3)
        self.assertEqual(tokens[0].position, 0)
        self.assertEqual(tokens[0].symboltype, 'other')
        
    def test_accentedLetters(self):
        '''
        tests a string that contains accented letters
        '''
        tokens = Tokenizer.tokenize('Àá... ÂãÄ!')
        self.assertEqual(len(tokens), 5)
        self.assertEqual(tokens[0].position, 0)
        self.assertEqual(tokens[0].substring, 'Àá')
        self.assertEqual(tokens[3].position, 6)
        self.assertEqual(tokens[3].substring, 'ÂãÄ')
        
if __name__ == '__main__':
    unittest.main()

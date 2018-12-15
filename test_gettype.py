# -*- coding: utf-8 -*-
import unittest
from gettype import GetType

class TokenizerTest(unittest.TestCase):
    '''tests for gettype.py'''
    def test_typeError(self):
        '''
        tests how the tokenizer handles receiving an integer instead of a string
        as input
        '''
        with self.assertRaises(TypeError):
            GetType.gettype(123)      
        
    def test_stringTypeError(self):
        '''
        tests how the tokenizer handles receiving a string with more than one 
        symbol as input
        '''
        with self.assertRaises(TypeError):
            GetType.gettype('aaa')      
            
    def test_letter(self):
        self.assertEqual(GetType.gettype('a'), 'letter')
    
    def test_digit(self):
        self.assertEqual(GetType.gettype('1'), 'digit')
    
    def test_letter(self):
        self.assertEqual(GetType.gettype(' '), 'whitespace')
    
    def test_letter(self):
        self.assertEqual(GetType.gettype('!'), 'punctuation')
    
    def test_letter(self):
        self.assertEqual(GetType.gettype('^'), 'other')
        
    def test_accentedLetter(self):
        self.assertEqual(GetType.gettype('À'), 'letter')
          
if __name__ == '__main__':
    unittest.main()

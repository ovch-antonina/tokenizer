# -*- coding: utf-8 -*-
class Token:
    """
    'Token' class for storing subsubstrings extracted from a string
    """
    def __init__(self, substring, position, symboltype):
        """
        Defining the Token class: it stores the information about the type of
        the substring, its content, and the position of its first symbol
        """
        # a substring where all symbols belong to the same type
        self.substring = substring 
        # records the position of the substring's first symbol
        self.position = position
        # records the type of the symbols
        self.symboltype = symboltype
        
class Tokenizer:   
    '''
    Class that contains a function for tokenizing a text
    '''
    def tokenize(text):     
        '''
        Breaks the input string into substrings of symbols of uniform types
        (tokens), records the position of (the first symbols of) tokens within 
        the input string.
        @param text String : input string        
        @return tokens List : a list of all the tokens in the input string, the
        positions of their first symbols, and the types of the symbols in them
        '''
        from gettype import GetType
        tokens=[]  
        # the first symbol of the current token, is the first symbol of the  
        # input string by default
        first = text[0]
        # the position of the first symbol of the current token, is 0 by default
        start = 0
        for i,c in enumerate(text): 
            # if the type of the current symbol is different from the type of 
            # the first symbol of the current token, then the current token has 
            # ended and the current symbol is the first symbol of the next token
            if not GetType.gettype(c)==GetType.gettype(first):
                    tokens.append(Token(text[start:i], start, GetType.gettype(first)))
                    first = c
                    start = i
        # records the last token in the input string
        tokens.append(Token(text[start:i+1], start, GetType.gettype(first)))
        for token in tokens:
            print(token.substring, token.position, token.symboltype)
        return tokens

#text = '5^3'
#Tokenizer.tokenize(text)

# -*- coding: utf-8 -*-
class Token:
    """
    'Token' class for storing alphabetical substrings extracted from a string
    """
    def __init__(self, substring, position):
        """
        Defining the Token class: it stores the information about the substring
        and about te position of its first symbol
        """
        # a substring of only alphabetical symbols
        self.substring = substring 
        # records the position of the substring's first symbol
        self.position = position 

class Tokenizer:   
    """
    Tokenizer class for performing the tokenize function
    """
    def tokenize(text):
        """
        Breaks the input string into substrings of alphabetical symbols 
        (tokens), records the position of (the first symbols of) tokens within 
        the input string.
        @param text String : input string        
        @return tokens List : a list of all the tokens in the input string and 
        the positions of their first symbols
        """
        tokens=[]  
        # a variable used to check if a change from a non-alphabetical symbol 
        # to an alphabetical one (or vice versa) occured. False by default
        isToken = False 
        for i,c in enumerate(text): 
            if isToken:
                if not c.isalpha(): 
                    # variable isToken changes back to False if a 
                    # non-alphabetical symbol is found after an alphabetical 
                    # one, marking the last symbol of a token
                    isToken = False 
                    tokens.append(Token(text[start:i], start))
            else:
                if c.isalpha():
                    # the index of the first symbol of the current token
                    start = i 
                    # variable isToken changes to True if an alphabetical 
                    # symbol is found after a non-alphabetical one, marking the
                    # first symbol of a token
                    isToken = True 
        # records the final token in cases when the last symbol of the input 
        # string is alphabetical and the final change to a non-alphabetical 
        # symbol never occured, as evidenced by isToken being True after the 
        # cycle ended
        if isToken:    
            tokens.append(Token(text[start:], start)) 
        for token in tokens:
            print(token.substring, token.position)
        return tokens

#text = 'Àá... ÂãÄ!'
#Tokenizer.tokenize(text)

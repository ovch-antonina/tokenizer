# -*- coding: utf-8 -*-
class GetType:
    '''
    Class that contains a function for determining the type of a symbol
    '''
    def gettype(symbol):
        '''
        Determines the type of a symbol
        @param symbol String : input symbol 
        @return symboltype String : the type of the input symbol 
        '''
        import unicodedata 
        # raise an error if the input string is not one symbol long
        if not len(symbol) == 1:
            raise TypeError
        # type is 'other' by default
        symboltype = 'other'
        # type is 'letter' if the symbol is alphabetical
        if symbol.isalpha():
            symboltype = 'letter'
        # type is 'digit' if the symbol is a digit
        if symbol.isdigit():
            symboltype = 'digit'
        # type is 'whitespace' if the symbol is a whitespace
        if symbol.isspace():
            symboltype = 'whitespace'    
        # type is 'punctuation' if the symbol is a punctuation mark 
        if unicodedata.category(symbol)[0] == 'P':
            symboltype = 'punctuation'
        return symboltype
        
#x = GetType.gettype('aaa')
#print(x)
    


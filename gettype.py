# -*- coding: utf-8 -*-
import unicodedata 
def gettype(symbol):
    '''
    Determines the type of a symbol
    @param symbol String : input symbol 
    @return symboltype String : the type of the input symbol 
    '''
    # raise an error if the input string is not one symbol long
    if len(symbol) != 1:
        raise TypeError
    # type is 'letter' if the symbol is alphabetical
    if symbol.isalpha():
        symboltype = 'letter'
    # type is 'digit' if the symbol is a digit
    elif symbol.isdigit():
        symboltype = 'digit'
    # type is 'whitespace' if the symbol is a whitespace
    elif symbol.isspace():
        symboltype = 'whitespace'    
    # type is 'punctuation' if the symbol is a punctuation mark 
    elif unicodedata.category(symbol)[0] == 'P':
        symboltype = 'punctuation'
    else:
        # type is 'other' by default
        symboltype = 'other'
    return symboltype
        
#x = gettype('a')
#print(x)
    


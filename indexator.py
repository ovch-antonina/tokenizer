import shelve
from tokenizer_new import Token, Tokenizer

def index_shelve(text):
    '''
    Saves tokens of 'letter' or 'digit' type into an indexed database
    @param text String : input string
    @return shelf Class 'shelve.DbfilenameShelf' : indexed database
    '''
    # creates the database file
    shelf = shelve.open("output_shelf.db")
    tokens = Tokenizer.tokenize(text)
    # marks the order of the letter/digit tokens in the input string
    i = 0
    for token in tokens:
        if token.symboltype is 'letter' or token.symboltype is 'digit':
            # key is the position of the token in the tokens order, value is 
            # the token itself
            shelf[str(i)] = token
            i = i+1
    return shelf

#text = 'one two three 1 2 3 '
#shelf = index_shelve(text)
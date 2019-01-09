import shelve
from tokenizer_new import Token, Tokenizer

class Position:
    """
    'Position' class for storing information about a token's position in a text
    """
    def __init__(self, left, right):
        """
        Defining the Position class: it stores the indexes of the left and 
        right boundaries of a token
        """
        # index of the token's first symbol
        self.left = left
        # index of the sybmol after the token's last symbol
        self.right = right
    def __repr__(self):
        """
        Defining how the Position class is represented
        """
        # the form used to represent the class is 
        # 'Position([left index]:[right index])
        return 'Position(%s:%s)' % (self.left, self.right)

def index_shelve(text, output):
    '''
    Creates or updates a shelve database that stores the positions of all 
    instances of a specific substring in a text.
    @param text String : path to the input text file
    @return shelf Class 'shelve.DbfilenameShelf' : indexed database
    '''
    # opens the indexed database, creates a new one if it doesn't exist yet
    shelf = shelve.open(output)
    # reads the input file 
    with open(text, 'r', encoding='utf-8') as text_temp:
        data = text_temp.read()
    # breaks the input file into tokens
    tokens = Tokenizer.tokenize(data)
    for token in tokens:
        if token.symboltype is 'letter' or token.symboltype is 'digit':
            right = token.position + len(token.substring)
            # records the position of the current token
            pos = Position(token.position, right)
            val = {}
            # if the current token's substring is not an existing key, creates 
            # one and assigns its position as the value
            if token.substring not in shelf:
                val[text] = [pos]
                shelf[token.substring] = val
            # if the current token's substring is an existing key 
            else:
                # reads the value of that existing key
                val_new = shelf[token.substring]
                # if the values dictionary doesn't have the current file path
                # as a key, creates a new dictionary entry and updates the 
                # value of the existing indexer key with it
                if text not in val_new:
                    val_new.update({text:[pos]})
                    shelf[token.substring] = val_new
                # if the values dictionary has the current file path as a key,
                # updates the list of positions in that values dictionary 
                # entry
                else:
                    val_new[text].append(pos)
                    shelf[token.substring] = val_new                        
    return shelf

#text1 = "input1.txt"
#text2 = "input2.txt"
#output = "output_shelf.db"
#shelf = index_shelve(text1, output)
#shelf = index_shelve(text2, output)
#for key in shelf.keys():
#    print('key:', key)
#    dic = shelf[key]
#    for key2 in dic.keys():
#        print('text:', key2)
#        for thing in dic[key2]:
#            print('pos:', thing)
#shelf.close()
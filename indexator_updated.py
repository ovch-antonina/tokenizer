import shelve
from tokenizer_new import Token, Tokenizer

class Position:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __repr__(self):
        return 'Position(%s:%s)' % (self.left, self.right)

def index_shelve(texts):
    '''
    Saves tokens of 'letter' or 'digit' type into an indexed database
    @param text String : input string
    @return shelf Class 'shelve.DbfilenameShelf' : indexed database
    '''
    # creates the database file
    shelf = shelve.open("output_shelf.db")
    val = {}
    for text in texts:
        tokens = Tokenizer.tokenize(text)
        for token in tokens:
            if token.symboltype is 'letter' or token.symboltype is 'digit':
                #print(token.substring)
                positions = []
                positions.append(Position(token.position, len(token.substring)))
                if token.substring not in shelf:
                    val[text] = positions
                    shelf[token.substring] = val
                else:
                    val = shelf[token.substring]
                    if text not in val:
                        val.update({text:positions})
                        shelf[token.substring] = val
                    else:
                        val[text].append(positions)
                        shelf[token.substring] = val                        
    return shelf

texts = ['one two three 1 2 3','one one one 1 two']
shelf = index_shelve(texts)
#for key in shelf.keys():
#    print('key:', key)
#    dic = shelf[key]
#    for key2 in dic.keys():
#        print('text', key2)
#        for thing in dic[key2]:
#            print('pos:', thing)
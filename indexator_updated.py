import shelve
from tokenizer_new import Token, Tokenizer

class Position:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __repr__(self):
        return 'Position(%s:%s)' % (self.left, self.right)

def index_shelve(texts, output):
    shelf = shelve.open(output)
    for text in texts:
        tokens = Tokenizer.tokenize(text)
        for token in tokens:
            if token.symboltype is 'letter' or token.symboltype is 'digit':
                #print(token.substring)
                positions = []
                positions.append(Position(token.position, len(token.substring)))
                val = {}
                if token.substring not in shelf:
                    val[text] = positions
                    shelf[token.substring] = val
                else:
                    val_new = shelf[token.substring]
                    if text not in val_new:
                        val_new.update({text:positions})
                        shelf[token.substring] = val_new
                    else:
                        val_new[text].append(positions)
                        shelf[token.substring] = val_new                        
    return shelf

texts = ['one two three 1 2 3','one one one 1 two']
output = "output_shelf.db"
shelf = index_shelve(texts, output)
for key in shelf.keys():
    print('key:', key)
    dic = shelf[key]
    for key2 in dic.keys():
        print('text', key2)
        for thing in dic[key2]:
            print('pos:', thing)
shelf.close()
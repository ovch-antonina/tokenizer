import shelve
from tokenizer_new import Token, Tokenizer

class Position:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __repr__(self):
        return 'Position(%s:%s)' % (self.left, self.right)

def index_shelve(text, output):
    shelf = shelve.open(output)
    with open(text, 'r', encoding='utf-8') as text_temp:
        data = text_temp.read()
    tokens = Tokenizer.tokenize(data)
    for token in tokens:
        if token.symboltype is 'letter' or token.symboltype is 'digit':
            right = token.position + len(token.substring)
            pos = Position(token.position, right)
            val = {}
            if token.substring not in shelf:
                val[text] = [pos]
                shelf[token.substring] = val
            else:
                val_new = shelf[token.substring]
                if text not in val_new:
                    val_new.update({text:[pos]})
                    shelf[token.substring] = val_new
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
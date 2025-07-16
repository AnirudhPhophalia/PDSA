# Here is the extracted text from your image, formatted for easy copy-paste:

# Write a function Huffman(s) that accepts a string s of characters a, b, c, d, e and f without any space. The function should generate the prefix code for each character based on its frequency in string s and return a dictionary where the key of the dictionary represents the character and the corresponding value represents the Huffman code for that character.


class Node:
    def __init__(self,frequency,symbol = None,left = None,right = None):
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right
def Huffman(s):
    huffcode = {}
    char = list(s)
    freqlist = []
    unique_char = set(char)
    for c in unique_char:
        freqlist.append((char.count(c), c))
    nodes = []
    for nd in sorted(freqlist):
        nodes.append((nd, Node(nd[0], nd[1])))
    while len(nodes) > 1:
        nodes.sort()
        L = nodes[0][1]
        R = nodes[1][1]
        newnode = Node(L.frequency + R.frequency, L.symbol + R.symbol, L, R)
        nodes.pop(0)
        nodes.pop(0)
        nodes.append(((L.frequency + R.frequency, L.symbol + R.symbol), newnode))
    for ch in unique_char:
        temp = newnode
        code = ''
        while ch != temp.symbol:
            if ch in temp.left.symbol:
                code += '0'
                temp = temp.left
            else:
                code += '1'
                temp = temp.right
        huffcode[ch] = code
    return huffcode

s = input()
res = Huffman(s)
for char in sorted(res):
    print(char,res[char])
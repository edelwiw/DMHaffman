from collections import Counter
import sys


class Node(object):

    def __init__(self, char=None, value=0, right=None, left=None,):
        self.value = value
        self.right = right
        self.left = left
        self.char = char

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return "\"" + str(self.char) + "\"-" + str(self.value) + " (" + str(self.right) + " " + str(self.left) + ")"

    #def __str__(self):
    #    return "\"" + str(self.char) + "\"-" + str(self.value)


class Dict(object):

    def __init__(self):
        self.nodes = []
        self.dict = {}

    def create_dict(self, text):
        c = Counter(text)
        for e in c:
            self.nodes.append(Node(e, c[e]))

        while len(self.nodes) > 1:
            self.nodes.sort()
            m1 = self.nodes.pop(0)
            m2 = self.nodes.pop(0)

            self.nodes.append(Node(m1.char + m2.char, m1.value + m2.value, m1, m2))

        self.__dfs__(self.nodes[0], "")

    def set_dict(self, dict: dict):
        self.dict = dict

    def __dfs__(self, node, way):
        if node.right and node.left:
            self.__dfs__(node.right, way + "1")
            self.__dfs__(node.left, way + "0")
        else:
            self.dict[node.char] = way
            return

    def get_dict(self):
        return self.dict

    def encode(self, text):
        encoded = ""
        for el in text:
            encoded += self.dict[el]
        return encoded

    def decode(self, text):
        letters = {value: key for key, value in self.dict.items()}
        decoded = ""
        buff = ""

        for i in text:
            buff += i
            if buff in letters:
                decoded += letters[buff]
                buff = ""
        return decoded

    def __repr__(self):
        return str(self.dict)


if __name__ == '__main__':
    if len(sys.argv) < 4:
        raise "Not enough arguments"
    method = sys.argv[1]
    in_path = sys.argv[2]
    out_path = sys.argv[3]


    inf = open(in_path, 'rb')
    ouf = open(out_path, 'wb')

    d = Dict()

    if method == '--encode':
        text = inf.read()
        d.create_dict(text)
        encoded = d.encode(text)


        for i in
        print(encoded)







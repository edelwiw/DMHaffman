from collections import Counter
import sys


class Node(object):

    def __init__(self, char=None, value=0, right=None, left=None,):
        self.value = value  # вес ноды ака количество таких символов в тексте
        self.right = right  # правый ребенок
        self.left = left  # левый ребенок
        self.char = char  # символ, для которого работаем

    def __lt__(self, other):  # less than - для сортировкм нод
        return self.value < other.value

    def __repr__(self): # represent - по большей части для дебага, возвращает описание ноды
        return "\"" + str(self.char) + "\"-" + str(self.value) + " (" + str(self.right) + " " + str(self.left) + ")"


def create_dict(text):
    dict = {}
    nodes = []

    def dfs(node, way):
        if node.right or node.left:  # если есть ребенок
            dfs(node.right, way + "1") # запускаем для правого, записываем путь
            dfs(node.left, way + "0")  # для левого
        else:
            dict[node.char] = way  # дошли до конца - записываем в словарь код символа (путь)
            return

    c = Counter(text)  # считаем количество символов
    for e in c:
        nodes.append(Node(e, c[e])) # создаем ноду для каждого символа

    while len(nodes) > 1:
        nodes.sort()  # сортируем и берем 2 самых маленьких ноды (те, символов которых меньше всего в тексте)
        m1 = nodes.pop(0)
        m2 = nodes.pop(0)
        nodes.append(Node(m1.char + m2.char, m1.value + m2.value, m1, m2))  # содаем ноду-родителя, символы конкатенируем, веса складываем

    dfs(nodes[0], "")  # запускаем дфс
    return dict




def encode(text, dict):  # просто бежим по символам и записываем их код
    encoded = ""
    for el in text:
        encoded += dict[el]
    return encoded


def decode(text, dict):
    letters = {value: key for key, value in dict.items()}  # транспонируем словарь
    decoded = ""
    buff = ""

    for i in text:
        buff += i  # добавляем в буффер новый бит
        if buff in letters:  # если встретился символ с таким кодом, записываем. Коды соотв. правилу фано - однозначное трактование
            decoded += letters[buff]
            buff = ""
    return decoded


if __name__ == '__main__':
    if len(sys.argv) < 4:
        raise "Not enough arguments"
    method = sys.argv[1]
    in_path = sys.argv[2]
    out_path = sys.argv[3]

    if method == '--encode':
        inf = open(in_path, 'r')
        ouf = open(out_path, 'wb')

        text = inf.read()
        print("Input text = " + text)

        dict = create_dict(text)  # создаем словарь с кодами
        print(dict)
        ouf.write((str(len(dict)) + '\n').encode())  # пишем длину в фаил

        for el in dict:
            ouf.write((el + ' ' + str(dict[el]) + '\n').encode())

        encoded = encode(text, dict)
        print("Encoded text = " + encoded)
        ouf.write(encoded.encode())

        inf.close()
        ouf.close()

    if method == '--decode':
        inf = open(in_path, 'rb')
        ouf = open(out_path, 'w')

        dict = {}

        l = int(inf.readline())

        for i in range(l):
            line = inf.readline()
            dict[chr(line[0])] = line[2:-1].decode()

        text = inf.readline().decode()
        decoded = decode(text, dict)
        print("Decoded text = " + decoded)
        ouf.write(decoded)

        inf.close()
        ouf.close()








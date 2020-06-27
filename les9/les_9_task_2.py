# 2. Закодируйте любую строку по алгоритму Хаффмана.

# thestr = "zemlia smerdit do samix zvezd"
#
# freq = {}
# for char in thestr:
#     if char not in freq:
#         freq[char] = 0
#     freq[char] += 1
# print(freq)
# tree = freq.items()
# print(tree)
#
# class MyNode:
#     def __init__(self, left=None, right=None):
#         # self.data = data
#         self.left = left
#         self.right = right
#
#     def children(self):
#         return self.left, self.right
#
#
# def haffman(node, code=""):
#     if isinstance(node, str):
#         return {node: code}
#
#     lef, rig = node.children()
#
#     res = {}
#     res.update(haffman(lef, code + "0"))
#     res.update(haffman(rig, code + "1"))
#
#     return res
#
#
# while len(tree) > 1:
#     tree = sorted(tree, reverse=True, key=lambda x: x[1])
#     ch1, cnt1 = tree[-1]
#     ch2, cnt2 = tree[-2]
#     tree = tree[:-2]
#     tree.append((MyNode(ch1, ch2), cnt1 + cnt2))
#
# codeTab = haffman(tree[0][0])
# coded = []
# for char in thestr:
#     coded.append(codeTab[char])
#
# print("Исходная строка: " + thestr)
# print(f"Закодированная строка: {' '.join(coded)}")
from collections import Counter, deque


class MyNode:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def haffman_tree(s):
    count_s = Counter(s)
    sorted_s = deque(sorted(count_s.items(), key=lambda item: item[1]))
    while len(sorted_s) > 1:
        weight = sorted_s[0][1] + sorted_s[1][1]
        node = MyNode(left=sorted_s.popleft()[0], right=sorted_s.popleft()[0])
        # Вставка пары "узел, вес" на нужное место в список
        for i, item in enumerate(sorted_s):
            if weight > item[1]:
                continue
            else:
                sorted_s.insert(i, (node, weight))
                break
        else:
            sorted_s.append((node, weight))
    return sorted_s[0][0]


code_table = dict()


def haffman_code(tree, path=''):
    if not isinstance(tree, MyNode):
        code_table[tree] = path

    else:
        haffman_code(tree.left, path=f'{path}0')
        haffman_code(tree.right, path=f'{path}1')


s = input('Введите строку для кодировки: ')
# Формирование таблицы кодирования
haffman_code(haffman_tree(s))
for i in s:
    print(code_table[i], end=' ')

print()
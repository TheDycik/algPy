

# import hashlib
# S = input("Введите строку: ")
# N = len(S)
# Res = set()
#
# for i in range(N):
#     if i == 0:
#         N = len(S) - 1
#     else:
#         N = len(S)
#     for j in range(N, i, -1):
#         print(S[i:j])
#         Res.add(hashlib.sha1(S[i:j].encode('utf-8')).hexdigest())
# print(Res)
#
# print(f"Количество различных подстрок в строке '{S}' равно {len(Res)}")
# import hashlib
#
# def find(s: str) -> int:
#   assert len(s) > 0, 'The string could not be empty'
#
#   counter = 0
#   hashes = []
#
#   for i in range(len(s)):
#     for j in range(len(s)):
#       if hashlib.sha1(s[i:j].encode('utf-8')).hexdigest() not in hashes:
#         hashes.append(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
#         counter += 1
#   return counter
#
# string = input('Enter the string: ')
#
# count = find(string)
#
# print(count if count else 'The are no substrings in the given string!')

import hashlib


def subs_count(s):
    subs = set()
    for i in range(len(s) + 1):
        for j in range(i + 1, len(s) + 1):
            sub_s = hashlib.sha1(s[i:j].encode('utf-8')).hexdigest()
            subs.add(sub_s)
    return len(subs)


s = input('Введите строку: ')
print(f'В строке "{s}" {subs_count(s)} подстрок')

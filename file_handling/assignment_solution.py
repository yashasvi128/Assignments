# question-1
N = 2;
from itertools import islice

with open("2.txt") as f:
    h = list(islice(f, N))
print(h)



# question-2
from collections import Counter


def word_count(fname):
    with open(fname) as f:
        return Counter(f.read().split())
print("Number of words in the file :", word_count("8.txt"))




# question-3
with open("3.txt") as f:
    with open("4.txt", "w") as f1:
        for line in f:
            f1.write(line)



# question-4
with open('1.txt') as f:
    with open('2.txt') as f1:
        for line1, line2 in zip(f, f1):
            print(line1 + line2)




# question-5
num = ['1', ' 23', '4', '5', '6', '7', '6', '65', '5', ' 6', '55', '44', '45', '54', '45']

with open('number6.txt', 'w') as filehandle:
    for listitem in num:
        filehandle.write('%s\n' % listitem)

f = open("number6.txt")
num = []
for l in f:
    num.append(int(l))
num.sort()
f.close
with open('number5.txt', 'w') as filehandle:
    for listitem in num:
        filehandle.write('%s\n' % listitem)
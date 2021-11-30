from time import time


def gen_filename():
    while True:
        t = int(time() * 1000)
        pattern = f"file-{int(t)}.jpg"
        yield pattern

        print('lka;jl;akjd')

def gen(s):
    for i in s:
        yield i

def gen2(n):
    for i in range(n):
        yield i

g1 = gen('vasya')
g2 = gen2(5)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)
    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass

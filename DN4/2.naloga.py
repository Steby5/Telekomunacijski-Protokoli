import math
def racun(s):
    a=min(s)
    b=max(s)
    c=(sum(s) / len(s))
    d=min(s, key = lambda x: abs(c - x))
    return a,b,c,d

stevila=input('Vnesi stevila:')
stevila=stevila.split(',')
stevila=[int(x) for x in stevila]
print(racun(stevila))

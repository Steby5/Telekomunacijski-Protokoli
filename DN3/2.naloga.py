data = {"prices": [41970, 40721, 41197, 41137, 43033],

       "volume": [49135346712, 50768369805, 47472016405, 34809039137, 38700661463]}
vrednosti=[None]*len(data)
def najvecja_vrednost(podatki):
    i=0
    for key in podatki:
        a=max(podatki[key])
        vrednosti[i]=a
        i+=1
    return vrednosti
vrednosti = najvecja_vrednost(data)
print(vrednosti)
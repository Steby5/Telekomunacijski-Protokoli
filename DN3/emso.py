def emso_leta_preracun(a):
    emso=str(a)
    datum=emso[0:4]
    dan=datum[0:2]+'.'
    mesec=datum[2:4]+'.'
    letnica=emso[4:7]
    spol=emso[7:10]
    if dan.startswith('0'):
        dan = dan[1:]
    if mesec.startswith('0'):
        mesec=mesec[1:]
    if letnica.startswith('0'):
        letnica='2'+letnica
    elif letnica.startswith('9'):
        letnica='1'+letnica
    rojstni_dan=dan+mesec+letnica
    starost=2022-int(letnica)
    if spol=='500':
        print("Star si:",starost,"let.")    #starost ugotovi glede na leto in ne ali si ze imel rojstni dan
        print("Rojstni dan imas:",rojstni_dan)
    elif spol=='505':
        print("Stara si:",starost,"let.")
        print("Rojstni dan imas:",rojstni_dan)


starost = emso_leta_preracun(input("Vnesi svoj EMSO: "))
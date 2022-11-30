def emso_leta_preracun(a):
    emso=str(a)
    datum=emso[0:4]
    dan=datum[0:2]+'.'
    mesec=datum[2:4]+'.'
    letnica=emso[4:7]
    regija=emso[7:9]
    spol=emso[9:12]
    
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
    
    if regija in range(0,9):
        drzava='izven nekdanje Jugoslavije (tujci)'
    elif regija in range(10,19):
        drzava='v Bosni'
    elif regija in range(20,29):
        drzava='v Crni Gori'
    elif regija in range(30,39):
        drzava='na Hrvaskem'
    elif regija in range(40,49):
        drzava='v Makedoniji'
    elif regija in range(50,59):
        drzava='v Sloveniji'
    elif regija in range(60,69):
        drzava='izven nekdanje Jugoslavije (zacasno prebivalisce)'
    elif regija in range(70,79):
        drzava='v Srbiji'
    elif regija in range(80,89):
        drzava='v Srbiji(Vojvodina)'
    elif regija in range(90,99):
        drzava='v Kosovu'
    
    if spol in range(000,499):
        print("Star si:",starost,"let.")    #starost ugotovi glede na leto in ne ali si ze imel rojstni dan
        print('Rojen si ',drzava)
        print("Rojstni dan imas:",rojstni_dan)
    elif spol in range(500,999):
        print("Stara si:",starost,"let.")
        print('Rojena si ',drzava)
        print("Rojstni dan imas:",rojstni_dan)


starost = emso_leta_preracun(input("Vnesi svoj EMSO: "))
d = {
    "mačka": "Micka",
    "pes": "Fido",
    "volk": "Rex",
    "medved": "Žan",
    "slon": "Jan",
    "žirafa": "Helga",
    "lev": "Gašper",
    "tiger": "Anže",
    "papagaj": "Črt",
    "ribica": "Elena",
    "krokodil": "Kasper",
    "zajec": "Lars",
    "kamela": "Manca"
}

#izpisi kluce ki imajo v vrednosti crko r ali R
for k in d.keys(): 
    if d[k].find("r") != -1 or d[k].find("R") != -1: 
        print(k)
    
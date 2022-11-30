import requests

a=input('Vnesi iskalni niz za RTV:')
headers = {'User-Agent': 'whatever'}    #to more bit ker idk
r=requests.get('https://www.rtvslo.si/iskalnik?q=',headers=headers,params=a)
print(r.text)
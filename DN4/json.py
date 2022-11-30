import json

podatki = {

  "name": "John",
  "age": 30,
  "city": "New York"
}

izhod=json.dumps(podatki, indent=3)
print(izhod)
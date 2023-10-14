import xml.etree.ElementTree as ET
import requests
from copy import copy

def dictify(r,root=True):
    if root:
        return {r.tag : dictify(r, False)}
    d=copy(r.attrib)
    if r.text:
        d["text"]=r.text
    for x in r.findall("./*"):
        if x.tag not in d:
            d[x.tag]=[]
        d[x.tag].append(dictify(x,False))
    return d

r = requests.get('https://www.cbr.ru/scripts/XML_daily.asp')
root = ET.fromstring(r.text)
d = dictify(root)

print(d['ValCurs']['Valute'][0])
print(d['ValCurs']['Valute'][0]['Name'][0]['text'])
print(d['ValCurs']['Valute'][0]['Value'][0]['text'])


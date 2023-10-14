import xml.etree.ElementTree as ET
import requests
from copy import copy

def createCurrency():
    r = requests.get('https://www.cbr.ru/scripts/XML_daily.asp')
    root = ET.fromstring(r.text)
    d = dictify(root)

    currency = {}

    for i in range(len(d['ValCurs']['Valute'])):
        currency[f"{d['ValCurs']['Valute'][i]['Name'][0]['text']}"] = d['ValCurs']['Valute'][i]['Value'][0]['text']
    return currency

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

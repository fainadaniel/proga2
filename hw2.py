import json as j
from pprint import pprint as pp
import urllib.request as r


def setup():
    su = []
    for x in ("elmiram, maryszmary, lizaku, nevmenandr".split(", ")):
        su.append(x)
    for x in ("ancatmara, roctbb, akutuzov, agricolamz".split(", ")):
        su.append(x)
    for x in ("bcongdon, kylepjohnson, mikekestemont".split(", ")):
        su.append(x)
    for x in ("demidovakatya, lehkost, JelteF, gvanrossum".split(", ")):
        su.append(x)
    for x in ("arogozhnikov, shwars, jasny, whyisjake, timgraham".split(", ")):
        su.append(x)
    us = input().split(', ')
    for eac in us:
        if eac not in su:
            print('nahuj! esche raz davaj. hochu teh rebyat iz dz')
            us = input().split(', ')
    return(us)
us = setup()


def setup2(us):
    token = 'cd4950256098dc0185fa46d5996c885e006564f0'
    ii = 'https://api.github.com/users/{}/repos?access_token={}'
    urlnew = ii.format(us[0], token)
    answer = r.urlopen(urlnew)
    txt = answer.read().decode('utf-8')
    data = j.loads(txt)
    return (data, token)

data, token = setup2(us)


def languages_personal(data):
    for rep in data:
        print(rep['name'])
        print(rep['description'])
        print()
    d = {}
    for rep in data:
        d[rep['language']] = d.get(rep['language'], 0) + 1
    print('languages this gal has:', d)
    return()
languages_personal(data)


def languages_all(us, token):
    d = {}
    ee = 'https://api.github.com/users/{}/repos?access_token={}'
    for turtur in us:
        url = ee.format(turtur, token)
        response = r.urlopen(url)
        txt = response.read().decode('utf-8')
        datei = j.loads(txt)
        for rep in datei:
            d[rep['language']] = d.get(rep['language'], 0) + 1
    print('\nmost popular language:', max(d.keys(), key=lambda x: d[x]), '\n')
    return()
languages_all(us, token)


def most_followed(us):
    mostpop = [-1, []]
    uu = 'https://api.github.com/users/{}/followers?access_token={}'
    for purpur in us:
        yetanotherurl = uu.format(purpur, token)
        reply = r.urlopen(yetanotherurl)
        txt = reply.read().decode('utf-8')
        dates = j.loads(txt)
        nof = len(dates)
        if nof > mostpop[0]:
            mostpop = [nof, [purpur]]
        elif nof == mostpop[0]:
            mostpop[1].append(purpur)
    print ("the most followed is:", mostpop[1])
    return()
most_followed(us)

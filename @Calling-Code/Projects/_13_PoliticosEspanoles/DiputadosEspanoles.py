import http.client
import json
import pandas as pd

url_main = 'https://www.congreso.es/busqueda-de-diputados'

conn = http.client.HTTPSConnection("www.congreso.es")

payload = "_diputadomodule_idLegislatura=-1&_diputadomodule_genero=0&_diputadomodule_grupo=all&_diputadomodule_tipo=0&_diputadomodule_nombre=&_diputadomodule_apellidos=&_diputadomodule_formacion=all&_diputadomodule_filtroProvincias=%5B%5D&_diputadomodule_nombreCircunscripcion="

headers = {
    'accept': "application/json, text/javascript, */*; q=0.01",
    'accept-language': "en-US,en;q=0.6",
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36",
    'x-requested-with': "XMLHttpRequest"
    }

conn.request("POST", "/busqueda-de-diputados?p_p_id=diputadomodule&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=searchDiputados&p_p_cacheability=cacheLevelPage", payload, headers)

res = conn.getresponse()

data = res.read()

info = data.decode("utf-8")

responseObject = json.loads(info)['data']

data = pd.DataFrame(responseObject)

# --------

script_1 = '''
conn = http.client.HTTPSConnection("www.congreso.es")

payload = "_diputadomodule_idLegislatura=-1&_diputadomodule_genero=0&_diputadomodule_grupo=all&_diputadomodule_tipo=0&_diputadomodule_nombre=&_diputadomodule_apellidos=&_diputadomodule_formacion=all&_diputadomodule_filtroProvincias=%5B%5D&_diputadomodule_nombreCircunscripcion="

headers = {
    'accept': "application/json, text/javascript, */*; q=0.01",
    'accept-language': "en-US,en;q=0.6",
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36",
    'x-requested-with': "XMLHttpRequest"
    }

conn.request("POST", "/busqueda-de-diputados?p_p_id=diputadomodule&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=searchDiputados&p_p_cacheability=cacheLevelPage", payload, headers)

res = conn.getresponse()

data = res.read()

info = data.decode("utf-8")

responseObject = json.loads(info)['data']

data = pd.DataFrame(responseObject)
'''
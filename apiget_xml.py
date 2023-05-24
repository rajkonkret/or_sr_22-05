import requests as re
import xml.etree.ElementTree as ET

url = 'http://api.nbp.pl/api/exchangerates/tables/A?format=xml'

response = re.get(url)
print(response)
# <Response [200]>

xml_data = response.content
print(xml_data)

root = ET.fromstring(xml_data)
print(root)
table_name = root.find('.//Table').text
print(table_name)
date = root.find('.//EffectiveDate').text
print(date)
rates = root.findall('.//Rate')
print(rates)

for rate in rates:
    currency = rate.find('Currency').text
    code = rate.find('Code').text
    mid = rate.find('Mid').text
    print(f"{code}: {currency} - {mid}")
# THB: bat (Tajlandia) - 0.1204
# USD: dolar amerykański - 4.1573
# AUD: dolar australijski - 2.7351
# HKD: dolar Hongkongu - 0.5307
# CAD: dolar kanadyjski - 3.0703
# NZD: dolar nowozelandzki - 2.5525
# SGD: dolar singapurski - 3.0873
# EUR: euro - 4.4803
# HUF: forint (Węgry) - 0.011962
# CHF: frank szwajcarski - 4.6087
# GBP: funt szterling - 5.1640
# UAH: hrywna (Ukraina) - 0.1131
# JPY: jen (Japonia) - 0.029998
# CZK: korona czeska - 0.1893
# DKK: korona duńska - 0.6016
# ISK: korona islandzka - 0.029534
# NOK: korona norweska - 0.3788
# SEK: korona szwedzka - 0.3895
# RON: lej rumuński - 0.9023
# BGN: lew (Bułgaria) - 2.2907
# TRY: lira turecka - 0.2091
# ILS: nowy izraelski szekel - 1.1150
# CLP: peso chilijskie - 0.005177
# PHP: peso filipińskie - 0.0746
# MXN: peso meksykańskie - 0.2321
# ZAR: rand (Republika Południowej Afryki) - 0.2159
# BRL: real (Brazylia) - 0.8360
# MYR: ringgit (Malezja) - 0.9056
# IDR: rupia indonezyjska - 0.00027901
# INR: rupia indyjska - 0.050257
# KRW: won południowokoreański - 0.003157
# CNY: yuan renminbi (Chiny) - 0.5906
# XDR: SDR (MFW) - 5.5441

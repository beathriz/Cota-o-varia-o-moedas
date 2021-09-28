import json
import requests

requisicao = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')

cotacao = json.loads(requisicao.text)


print('COTAÇÃO VARIAÇÃO MOEDAS PARA O REAL\n')
print('- Dólar:', cotacao ['USDBRL']['high'])
print('Variação DOLAR/REAL:', cotacao ['USDBRL'] ['varBid'])
print('- Euro:', cotacao ['EURBRL']['high'])
print('Variação EURO/REAL:', cotacao ['EURBRL'] ['varBid'])
print('- Bitcon', cotacao ['BTCBRL']['high'])
print('Variação BITCON/REAL:', cotacao ['BTCBRL'] ['varBid'])
import json

with open ("dados.json", encoding='utf-8') as info_json:
    dados = json.load(info_json)

def menorvalor(dados):
    menor_valor = min(dados, key=lambda d : d['valor'])['valor']
    print('\nMenor valor:',menor_valor,'\nDia(s):')
    return [item['dia'] for item in dados if item['valor'] == menor_valor]
def maiorvalor(dados):
    maior_valor = max(dados, key=lambda d: d['valor'])['valor']
    print('\nMaior valor:',maior_valor,'\nDia(s):')
    return [item['dia'] for item in dados if item['valor'] == maior_valor]
def faturamento(dados):
   print('\nNúmero de dias no mês em que o valor de faturamento diário foi superior à média mensal:')
   valores = []
   for i in dados:
       if i['valor'] != 0:
           valores.append(i['valor'])
   media_mensal = sum(valores)/len(valores)
   return [item['dia'] for item in dados if item['valor'] > media_mensal]

print(maiorvalor(dados))
print(menorvalor(dados))
print(faturamento(dados))

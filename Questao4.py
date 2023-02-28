faturamento_mensal = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}
total= sum(faturamento_mensal.values())
percentual = dict()
for item in faturamento_mensal:
    percentual[item] = '{:.2%}'.format(faturamento_mensal[item] / total)

print("Faturamento Mensal(Por estado) = ", faturamento_mensal)
print("Faturamento Total mensal = ", total)
print("Faturamento Percentual(Por estado) = ", percentual)



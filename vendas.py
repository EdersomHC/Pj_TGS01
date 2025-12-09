import json

# Carregar dados do arquivo vendas.json
with open("vendas.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

# Função para calcular comissão
def calcular_comissao(valor):
    if valor < 100:
        return 0
    elif valor < 500:
        return valor * 0.01
    else:
        return valor * 0.05

# Agrupar comissão por vendedor
comissoes = {}
for venda in dados["vendas"]:
    vendedor = venda["vendedor"]
    valor = venda["valor"]
    comissao = calcular_comissao(valor)
    comissoes[vendedor] = comissoes.get(vendedor, 0) + comissao

# Mostrar resultado
for vendedor, total in comissoes.items():
    print(f"{vendedor}: R$ {total:.2f}")

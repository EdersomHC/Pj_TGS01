import json
import uuid

# Carregar dados do arquivo estoque.json
with open("estoque.json", "r", encoding="utf-8") as f:
    estoque = json.load(f)

# Função para movimentar estoque
def movimentar(codigoProduto, quantidade, tipo):
    for produto in estoque["estoque"]:
        if produto["codigoProduto"] == codigoProduto:
            if tipo == "entrada":
                produto["estoque"] += quantidade
            elif tipo == "saida":
                produto["estoque"] -= quantidade
            else:
                print("Tipo inválido")
                return
            movimento_id = str(uuid.uuid4())
            print(f"Movimento {movimento_id}: {tipo} de {quantidade} unidades do produto {produto['descricaoProduto']}")
            print(f"Estoque final: {produto['estoque']}")
            return
    print("Produto não encontrado")

# Exemplos de uso
movimentar(101, 20, "entrada")
movimentar(102, 10, "saida")

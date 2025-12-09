from datetime import datetime

def calcular_juros(valor, data_vencimento):
    hoje = datetime.now().date()
    vencimento = datetime.strptime(data_vencimento, "%Y-%m-%d").date()
    dias_atraso = (hoje - vencimento).days
    
    if dias_atraso > 0:
        multa = valor * 0.025 * dias_atraso
        valor_final = valor + multa
        print(f"Dias de atraso: {dias_atraso}")
        print(f"Multa total: R$ {multa:.2f}")
        print(f"Valor final: R$ {valor_final:.2f}")
    else:
        print("Pagamento em dia. Sem multa.")

# Exemplo de uso
calcular_juros(1000, "2025-12-01")  # vencimento em 1º de dezembro

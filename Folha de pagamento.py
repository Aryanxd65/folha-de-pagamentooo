# Função para calcular o INSS
def calcular_inss(salario_base):
    if salario_base <= 1100.00:
        return salario_base * 0.075
    elif salario_base <= 2203.48:
        return salario_base * 0.09
    elif salario_base <= 3305.22:
        return salario_base * 0.12
    elif salario_base <= 6433.57:
        return salario_base * 0.14
    return 854.36  # Valor máximo

# Função para calcular o IRRF
def calcular_irrf(salario_base, dependentes):
    base_irrf = salario_base - calcular_inss(salario_base) - (dependentes * 189.59)
    if base_irrf <= 2259.20:
        return 0
    elif base_irrf <= 2826.65:
        return base_irrf * 0.075 - 171.97
    elif base_irrf <= 3751.05:
        return base_irrf * 0.15 - 354.80
    elif base_irrf <= 4664.68:
        return base_irrf * 0.225 - 636.13
    return base_irrf * 0.275 - 869.36

# Função para calcular a folha de pagamento
def folha_pagamento():
    salario_base = float(input("Digite o salário base do funcionário (R$): "))
    vale_transporte = 0.06 * salario_base if input("Deseja receber vale transporte? (s/n): ").lower() == 's' else 0
    vale_refeicao = float(input("Digite o valor do vale refeição fornecido pela empresa (R$): ")) * 0.20
    plano_saude = 150.00  # Desconto fixo para plano de saúde
    irrf = calcular_irrf(salario_base, dependentes=1)
    inss = calcular_inss(salario_base)

    # Cálculo dos descontos
    descontos = inss + irrf + vale_transporte + vale_refeicao + plano_saude
    salario_liquido = salario_base - descontos

    # Exibindo dados
    print(f"\nSalário Base: R$ {salario_base:.2f}")
    print(f"Desconto INSS: R$ {inss:.2f}")
    print(f"Desconto IRRF: R$ {irrf:.2f}")
    print(f"Desconto Vale Transporte: R$ {vale_transporte:.2f}")
    print(f"Desconto Vale Refeição: R$ {vale_refeicao:.2f}")
    print(f"Desconto Plano de Saúde: R$ {plano_saude:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

# Chamando a função
folha_pagamento()

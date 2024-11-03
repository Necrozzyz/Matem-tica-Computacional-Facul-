def calcular_salario_final(salario_fixo, total_vendas, num_carros_vendidos):
    # Valores fixos da comissão e percentuais
    comissao_por_carro = 300.0  
    percentual_comissao = 0.05  
    percentual_bonus = 0.10     

    if num_carros_vendidos == 0:
        return salario_fixo
    
    salario_com_comissao = salario_fixo + (comissao_por_carro * num_carros_vendidos)
    
    if num_carros_vendidos > 10:
        percentual = percentual_bonus
    else:
        percentual = percentual_comissao

    salario_final = salario_com_comissao + (total_vendas * percentual)
    return salario_final

# Solicitando os valores do usuário
salario_fixo = float(input("Digite o salário fixo do vendedor: R$ "))
total_vendas = float(input("Digite o valor total das vendas do vendedor: R$ "))
num_carros_vendidos = int(input("Digite o número de carros vendidos: "))

# Calculando o salário final
salario_final = calcular_salario_final(salario_fixo, total_vendas, num_carros_vendidos)
print(f"Salário final do vendedor: R${salario_final:.2f}")

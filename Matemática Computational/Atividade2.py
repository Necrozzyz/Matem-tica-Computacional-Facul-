# Função para verificar se todas as idades são inteiros positivos
def validar_idades(idades):
    return all(isinstance(idade, int) and idade > 0 for idade in idades)

# Função principal
def calcular_soma_produto(homem1, homem2, mulher1, mulher2):
    idades_homens = [homem1, homem2]
    idades_mulheres = [mulher1, mulher2]
    
    # Verificar se as idades são válidas
    if not validar_idades(idades_homens + idades_mulheres):
        return "Erro: Todas as idades devem ser números inteiros positivos."
    
    # Determinar homem mais velho e mais novo
    homem_mais_velho = max(idades_homens)
    homem_mais_novo = min(idades_homens)
    
    # Determinar mulher mais velha e mais nova
    mulher_mais_velha = max(idades_mulheres)
    mulher_mais_nova = min(idades_mulheres)
    
    # Calcular soma e produto conforme as regras
    soma = homem_mais_velho + mulher_mais_nova
    produto = homem_mais_novo * mulher_mais_velha
    
    return f"Soma do homem mais velho com a mulher mais nova: {soma}\nProduto do homem mais novo com a mulher mais velha: {produto}"

# Entrada de dados pelo usuário
try:
    homem1 = int(input("Digite a idade do primeiro homem: "))
    homem2 = int(input("Digite a idade do segundo homem: "))
    mulher1 = int(input("Digite a idade da primeira mulher: "))
    mulher2 = int(input("Digite a idade da segunda mulher: "))
    
    # Chamada da função e exibição do resultado
    resultado = calcular_soma_produto(homem1, homem2, mulher1, mulher2)
    print(resultado)

except ValueError:
    print("Erro: Todas as idades devem ser números inteiros.")

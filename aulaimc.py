
# Esse código calcula o índice de IMC do usuário de acordo com os dados de entrada

print('Seja bem vindo a calculadora de IMC!') # Mensagem de saudação
nome = input('Digite o seu nome: ') # Solicita o nome do usuário 
altura = input('Digite a sua altura: ') # Solicita a altura do usuário
peso = input('Digite o seu peso: ') # Solicita o peso do usuário

altura = float(altura) # Defini o tipo de variável como float
peso = float(peso)

imc = peso / altura ** 2 # executa o cálculo de acordo com a fórmula de IMC

print(f'Seu imc é {imc:.2f}') # Apresenta ao usuário o rescultado do cálculo

# ... Colocar uma tabela com dados de IMC aceitáveis de acordo com comparação entre peso, altura e IMC resultante
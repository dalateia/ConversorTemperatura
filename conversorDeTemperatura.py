#Projeto #1: Conversor de Temperatura em Python
#Repositório: github.com/mateusdalateia/ConversorTemperatura
#Autor: Mateus Dalateia
#Data: 20/07/2025
#Descrição: Este programa converte temperaturas entre Celsius, Fahrenheit e Kelvin.
#Versão: v1.0

# Menu simples
print("=== Conversor de Temperatura ===")
print("Selecione a escala de ORIGEM:")
print("1 - Celsius")
print("2 - Fahrenheit")
print("3 - Kelvin")
escala_origem = input("Digite a opção desejada: ")

print("Selecione a escala de DESTINO:")
print("1 - Celsius")
print("2 - Fahrenheit")
print("3 - Kelvin")
escala_destino = input("Digite a opção desejada: ")

temperatura_inicial = float(input("Informe o valor da temperatura a ser convertida: "))

#Convertendo Celsius para outras escalas
if escala_origem == "1" and escala_destino == "2":
    temperatura_convertida = (temperatura_inicial * 9 / 5) + 32
elif escala_origem == "1" and escala_destino == "3":
    temperatura_convertida = temperatura_inicial + 273.15

#Convertendo Fahrenheit para outras escalas
elif escala_origem == "2" and escala_destino == "1":
    temperatura_convertida = (temperatura_inicial - 32) * 5 / 9
elif escala_origem == "2" and escala_destino == "3":
    temperatura_convertida = ((temperatura_inicial - 32) * 5 / 9) + 273.15

#Convertedo Kelvin para outras escalas
elif escala_origem == "3" and escala_destino == "1":
    temperatura_convertida = temperatura_inicial - 273.15
elif escala_origem == "3" and escala_destino == "2":
    temperatura_convertida = ((temperatura_inicial - 273.15) * 9 / 5) + 32

#Exibição dos resultados
print("\nResultado da conversão:")
print("Temperatura informada:", temperatura_inicial, "graus")
print("Temperatura convertida:", temperatura_convertida, "graus")

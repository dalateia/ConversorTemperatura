#Projeto #1: Conversor de Temperatura em Python
#Repositório: github.com/mateusdalateia/ConversorTemperatura
#Autor: Mateus Dalateia
#Data: 20/07/2025
#Descrição: Este programa converte temperaturas entre Celsius, Fahrenheit e Kelvin.
#Versão: v1.0

while True:
    print("=== Conversor de Temperatura ===")
    print("Selecione a escala de ORIGEM:")
    print("1 - Celsius")
    print("2 - Fahrenheit")
    print("3 - Kelvin")
    escala_origem = input("Digite a opção desejada (1/2/3): ")  

    while escala_origem not in ["1", "2", "3"]:
        print("Opção inválida. Por favor, selecione 1, 2 ou 3.")
        escala_origem = input("Digite a opção desejada (1/2/3): ")

    if escala_origem == "1":      
        print("Selecione a escala de DESTINO:")
        print("2 - Fahrenheit")
        print("3 - Kelvin")
        escala_destino = input("Digite a opção desejada (2/3): ")
        while escala_destino not in ["2", "3"]:
            print("Opção inválida. Por favor, selecione 2 ou 3.")
            escala_destino = input("Digite a opção desejada (2/3): ")

    elif escala_origem == "2":
        print("Selecione a escala de DESTINO:")
        print("1 - Celsius")
        print("3 - Kelvin")
        escala_destino = input("Digite a opção desejada (1/3): ")
        while escala_destino not in ["1", "3"]:
            print("Opção inválida. Por favor, selecione 1 ou 3.")
            escala_destino = input("Digite a opção desejada (1/3): ")

    elif escala_origem == "3":
        print("Selecione a escala de DESTINO:")
        print("1 - Celsius")
        print("2 - Fahrenheit")
        escala_destino = input("Digite a opção desejada (1/2): ")
        while escala_destino not in ["1", "2"]:
            print("Opção inválida. Por favor, selecione 1 ou 2.")
            escala_destino = input("Digite a opção desejada (1/2): ")

    while True :
        entrada = input("Informe o valor da temperatura a ser convertida: ")
        try:
            temperatura_inicial = float(entrada)
            break
        except ValueError:
            print("Valor inválido. Digite apenas números.")

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
    escalas = {
        "1": "°C (Celsius)",
        "2": "°F (Fahrenheit)",
        "3": "°K (Kelvin)"
    }
    print("\nResultado da conversão:")
    print(f"Temperatura informada: {temperatura_inicial:.1f}{escalas[escala_origem]}")
    print(f"Temperatura convertida: {temperatura_convertida:.1f}{escalas[escala_destino]}")
    print(f"{temperatura_inicial:.1f}{escalas[escala_origem]} equivale a {temperatura_convertida:.1f}{escalas[escala_destino]}")
    
    repetir = ""
    while repetir not in ("n","s"):
        repetir = input("Deseja realizar outra conversão? (s/n)").lower()
        if repetir not in ("n","s"):
           print("O valor digitado é invalido, digite s para continuar ou n para encerrar o programa.")
    else:
     if repetir == "n" :
        break
     elif repetir == "s":
        continue
    
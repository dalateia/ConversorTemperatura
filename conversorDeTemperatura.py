#Projeto #1: Conversor de Temperatura em Python
#Repositório: github.com/mateusdalateia/ConversorTemperatura
#Autor: Mateus Dalateia
#Data: 30/07/2025
#Descrição: Este programa converte temperaturas entre Celsius, Fahrenheit e Kelvin.
#Versão: v3.5

def exibir_menu_escala_origem():
    print("=== Conversor de Temperatura ===")
    print("Selecione a escala de ORIGEM:")
    print("1 - Celsius")
    print("2 - Fahrenheit")
    print("3 - Kelvin")
    escala_origem = input("Digite a opção desejada (1/2/3): ").strip()  

    while escala_origem not in ["1", "2", "3"]:
        print("Opção inválida. Por favor, selecione 1, 2 ou 3.")
        escala_origem = input("Digite a opção desejada (1/2/3): ").strip()
    return escala_origem

def exibir_menu_escala_destino(escala_origem):
    if escala_origem == "1":      
        print("Selecione a escala de DESTINO:")
        print("2 - Fahrenheit")
        print("3 - Kelvin")
        escala_destino = input("Digite a opção desejada (2/3): ").strip()
        while escala_destino not in ["2", "3"]:
            print("Opção inválida. Por favor, selecione 2 ou 3.")
            escala_destino = input("Digite a opção desejada (2/3): ").strip()

    elif escala_origem == "2":
        print("Selecione a escala de DESTINO:")
        print("1 - Celsius")
        print("3 - Kelvin")
        escala_destino = input("Digite a opção desejada (1/3): ").strip()
        while escala_destino not in ["1", "3"]:
            print("Opção inválida. Por favor, selecione 1 ou 3.")
            escala_destino = input("Digite a opção desejada (1/3): ").strip()

    elif escala_origem == "3":
        print("Selecione a escala de DESTINO:")
        print("1 - Celsius")
        print("2 - Fahrenheit")
        escala_destino = input("Digite a opção desejada (1/2): ").strip()
        while escala_destino not in ["1", "2"]:
            print("Opção inválida. Por favor, selecione 1 ou 2.")
            escala_destino = input("Digite a opção desejada (1/2): ").strip()
    return escala_destino

def ler_temperatura():
    while True :
        temperatura_inicial = input("Informe o valor da temperatura a ser convertida: ").strip()
        temperatura_inicial = temperatura_inicial.replace(",",".")
        try:
            temperatura_inicial = float(temperatura_inicial)
            return temperatura_inicial
        except ValueError:
            print("Valor inválido. Digite apenas números.")

# Limites físicos mínimos por escala
limites_minimos = {
    "1": -273.15,   # Celsius
    "2": -459.67,   # Fahrenheit
    "3": 0          # Kelvin
    }

def verificar_limite_fisico(escala_origem, temperatura_inicial):
    minimo = limites_minimos[escala_origem]
    if temperatura_inicial < minimo:
        return True # Caso True, ao executar a função abaixo, entrará no segundo loop para perguntar se deseja continuar
    else:
        return False # Quebra o looping e segue o código

def informar_limite_e_perguntar(escala_origem):
    referencias = {
        "1": "-273.15°C (Zero Absoluto)",
        "2": "-459.67°F (Zero Absoluto)",
        "3": "0 K (Zero Absoluto)"
    }
    
    print(f"\nATENÇÃO: O valor informado é fisicamente inalcançável.")
    print(f"Referência do limite mínimo para a escala selecionada: {referencias[escala_origem]}")
    print("Porém, para fins de curiosidade, o programa pode continuar e mostrar o resultado da conversão.\n")

    while True:
        resposta = input("Deseja prosseguir com a conversão? (s = sim / n = alterar valor): ").strip().lower()
        if resposta == "s":
            return True  # Aqui ela quebra o loop e continua a conversão
        elif resposta == "n":
            return False  # Aqui chamará novamente a função ler_temperatura()
        else:
            print("Resposta inválida. Digite 's' para continuar ou 'n' para alterar o valor.")

def realizar_conversao(escala_origem, escala_destino, temperatura_inicial):
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
    else:
        print("Erro interno: conversão inválida. Verifique as escalas.")
        return None
    return temperatura_convertida

   
    #Dicionário para exibição detalhada
escalas = {
        "1": "°C (Celsius)",
        "2": "°F (Fahrenheit)",
        "3": "°K (Kelvin)"
    }

def exibir_resultados(escala_origem, escala_destino, temperatura_inicial, temperatura_convertida):    #Exibição dos resultados
    print("\nResultado da conversão:")
    print(f"Temperatura informada: {temperatura_inicial:.2f}{escalas[escala_origem]}")
    print(f"Temperatura convertida: {temperatura_convertida:.2f}{escalas[escala_destino]}")
    print(f"{temperatura_inicial:.2f}{escalas[escala_origem]} equivale a {temperatura_convertida:.2f}{escalas[escala_destino]}")

def repetir_conversao():
    repetir = ""
    while True:
        repetir = input("Deseja realizar outra conversão? (s/n)").lower().strip()
        if repetir == "s":
           return True 
        elif repetir == "n":
            return False
        else:
           print("O valor digitado é invalido, digite s para continuar ou n para encerrar o programa.")

def main():
    try:
        while True:  # Loop principal do programa
            escala_origem = exibir_menu_escala_origem()
            escala_destino = exibir_menu_escala_destino(escala_origem)

            # Loop interno para leitura e validação da temperatura
            while True:
                temperatura_inicial = ler_temperatura()
                if verificar_limite_fisico(escala_origem, temperatura_inicial):
                    if informar_limite_e_perguntar(escala_origem):
                        break  # Aqui o usuário já recebeu a mensagem e escolheu seguir para conversão
                    else:
                        print("Por favor, informe um novo valor dentro do limite físico.")
                        # Neste else, a condição false foi alcançada e irá chamar novamente a função ler_temperatura()
                else:
                    break  # Caso false em verificar_limite_fisico, o código segue.

            temperatura_convertida = realizar_conversao(escala_origem, escala_destino, temperatura_inicial)
            if temperatura_convertida is None:
                print("Conversão não realizada. Programa encerrado por segurança.")
                break
            else:
                exibir_resultados(escala_origem, escala_destino, temperatura_inicial, temperatura_convertida)
            if not repetir_conversao():
                break

    except (KeyboardInterrupt, EOFError):
        print("\nPrograma encerrado pelo usuário.")

main()
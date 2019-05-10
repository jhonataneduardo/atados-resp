from utils.functions import has_number, has_repeated_letter, is_isogram


# Entrada de dado do usuário
def main():
    palavra = input("Digite uma palavra: ")
    if not palavra:
        print("Para continuar a verificação é necessário digitar uma palavra. Tente novamente.")
        main()
    return is_isogram(palavra.lower())

if __name__ == '__main__':
    main()












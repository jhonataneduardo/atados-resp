#
# Funções auxiliares
#

# verifica se a string de entrada possuí algum número
def has_number(value):
    for i in value:
        if i.isdigit():
            resul = False
            break
        else:
            resul = True
    return resul

# verifica se a string de entrada possui alguma letra repetida
def has_repeated_letter(value):
    for i in value:
        if value.count(i) > 1:
            resul = True
            break
        else:
            resul = False
    return resul

# Verifica se a palavra é um isograma
def is_isogram(value):
    if has_number(value):
        if not has_repeated_letter(value):
            print("É um isograma! \o/")
            return True
        else:
            print("Não é um isograma! :(")
            return False
    else:
        print("Palavra iválida! :S")
        return False


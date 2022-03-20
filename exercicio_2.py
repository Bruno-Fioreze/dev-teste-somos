# python imports

#3rd imports

#my imports
from message_assert import write_success, write_error

def sanitize_characters_sequence(text: str, characters: str) -> str:
    """ Função responsável por remover caracteres sequenciais
    Args:
        text (str): sequencia de caracteres a serem válidados.
        characters (str): caracter a ser verificado.

    Returns:
        str:  retorna o texto válidado
    """
    #Aqui eu pensei em usar fatiamento de string, mas achei melhor seguir dessa forma.
    position_initial_final  = text.find(characters)
    lista_string = list(text)
    lista_string.pop(position_initial_final)
    lista_string.pop(position_initial_final)
    text = "".join(lista_string)
    return text

def check_even_characters(text: str) -> str:
    """Método responsável por validar se uma sequencia de caracteres é válida.
    Args:
        text (caracteres): sequencia de caracteres
    Returns:
        bool:  resultado da verificação.
    """
    is_valid = True
    # se for impar não tem como ter um par, então eu já paro a função aqui.
    if len(text) % 2 == 1:
        is_valid = False
        return is_valid
    
    # Removo os caracteres sequenciais
    check_characters = {"()", "[]", "{}"}
    for character in check_characters:
        if character in text :
            text = sanitize_characters_sequence(text, character)
    
    #se a string possuir caracteres invertidos ela não é válida.
    characters_inverse = {
        ")(", "}{", "]["
    }
    for character in characters_inverse:
        if character in text:
            is_valid = False
            return False
    
    # Verifico se é igual a zero.
    if len( text ) == 0:
        return is_valid
    
    # faço o processamento para descobrir se os pares são válidos
    list_string = list(text)
    inverse = len(list_string)  
    limit = int( inverse / 2)  -1
    is_valid = True

    characters = {
        "]": "[",
        ")": "(",
        "}": "{",
    }

    for string in enumerate(list_string):
        position, value  = string
        inverse -= 1
        if value != characters[list_string[inverse]]:  
            is_valid =  False
            break
        if limit == position:
            break
    return is_valid        


assert check_even_characters("{[()]}") == True and write_success(), write_error()
assert check_even_characters("()[]{}") == True and write_success(), write_error()
assert check_even_characters("([])") == True and write_success(), write_error()
assert check_even_characters("{{[[(())]]}}") == True and write_success(), write_error()
assert check_even_characters("([]") == False and write_success(), write_error()
assert check_even_characters("[({)}]") == False and write_success(), write_error()
assert check_even_characters(")(") == False and write_success(), write_error()
assert check_even_characters("(([{()}])))") == False and write_success(), write_error()




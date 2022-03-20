# python imports

#3rd imports

#my imports
from message_assert import write_success, write_error

text = "ABCDCDC"
search = "CDC"

def verify_occrences_in_string(text:str , search:str) -> str:
    """Método responsável por verificar quanas vezes search ocorre em text.

    Args:
        text (str): 
        search (str): 

    Returns:
        int: Número de vezes que search está presente em text.
    """
    limit = len(text)
    occorences = 0 
    
    for position, character in enumerate(text):
        substr = text[position:limit]
        first_character = search[0]
        if search in substr and first_character == character:
            occorences += 1

    return occorences


assert verify_occrences_in_string( text, search ) == 2 and write_success(), write_error()

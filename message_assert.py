def write_success(msg='assert OK'):
    """Função responsável por mostrar a mensagem assert ok.

    Args:
        msg (str, optional): Mensagem a ser exibida. Defaults to 'assert OK'.

    Returns:
        bool: 
    """
    print( msg )
    return True

def write_error(msg="Assert no ok"):
    """Função responsável por mostrar mensagem de Assert no ok.

    Args:
        msg (str, optional): _description_. Defaults to "Assert no ok".

    Returns:
        bool:
    """
    print(msg )
    return msg 

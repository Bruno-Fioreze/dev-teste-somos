
import json
from pprint import pprint


def get_position(text, first_position, last_position, first=False, pontuations=(".","!", "?")):
    """Método responsável por pegar o número de corte da sentença.

    Args:
        text (str): 
        first_position (int): posição inicial
        last_position (int): posição final
        first (bool, optional): Quando True é passado o fatiamento não é ativado. Defaults to False.
        pontuations (tuple, optional): Pontuação final. Defaults to (".","!", "?").

    Returns:
        int:  posição onde a sentença termina.
    """
    numbers = []
    for pontuation in pontuations:
        if first:
            position = text.find(pontuation) + 1
        else:
            position = text[first_position:last_position].find(pontuation) + 1
        if position != 0 and position != -1:
            numbers.append(position)
    return min( numbers )

def extract_sentence( text:str) -> str:
    """Método responsável por extrair as senteças do texto

    Args:
        text (str): 

    Returns:
        list: Lista com dicionarios contendo as sentenças.
    """
    sentences = []
    run = True
    length_text = len( text )
    first_position, cont_position, last_position = 0, 0 , 0

    while run:
        if first_position == 0:
            first_position = get_position(text, first_position, length_text)
            text_extract = text[0: first_position]
            #print(f"text : /n {text[0: cont_position + first_position]}")
            #print(f"first_position: {first_position} // cont_position: {cont_position}")
            sentence = {
                "sentença": text_extract
            }
            sentences.append(sentence)
            cont_position = cont_position + first_position
        else:
            last_position = get_position(text, cont_position, length_text)
            text_extract = text[cont_position: cont_position+ last_position]
            sentence = {
                "sentença": text_extract
            }
            sentences.append(sentence)
            #print(f"text : /n {text[cont_position: cont_position + last_position]}")
            cont_position = cont_position + last_position
        if cont_position == length_text:
            run = False

    return sentences
        
#def extract_sentence( text:str) -> str:
    # text_ = ""
    # for character in text:
    #     text_ += character
    #     if character in punctuation: 
    #         #print("entrou aqui")   
    #         sentence = {
    #             "sentença": text_
    #         }
    #         sentences.append(sentence)
    #         text_ = ""

    # return sentences

def get_data_or_null(expressions_present):
    """Função responsável por retornar null ou a expressão.

    Args:
        expressions_present (list):  Lista que contém as expressões.

    Returns:
        str: lista com as expressões ou null
    """
    return expressions_present if len(expressions_present) > 0 else "null"

def check_expression(sentence):
    """Método responsável por verificar se existe a expressão no início da sentença.

    Args:
        sentence (str): 

    Returns:
        lista:  lista validada com as expressões.
    """
    expressions_present = []
    data = []
    expressions = sentence.lower().split(",")[0:3]
    path = "./expressoes.txt"
    with open(path, "r") as file:
        for expression_file in file.readlines():
            expression_file = expression_file.strip()
            # expressions_present = [
            #    expression.strip()  for expression in expressions if expression.strip() == expression_file
            # ]
            for expression in expressions: 
                expression = expression.strip() 
                if expression== expression_file:
                    expressions_present.append(
                        expression
                    )

    data.append(
        {
            "sentença": sentence, 
            "expressão": get_data_or_null(expressions_present)
         }
    )
    return data

# sentence = "Logo, baseado no que foi dito, vale citar o filósofo Pitágoras, que explica que é melhor educar bem as crianças do que ter que reeducá-las como adultos."
# result = check_expression(sentence)    
# pprint(
#     result
# )     

def process_text():
    """
        Função responsável por receber textos e gerar o output.json
    """
    path = "./textos.json"
    list_sentences = []
    data_list_sentences = {}
    with open(path, "r") as file:
        list_data = json.load(file)
        for data in list_data:
            sentences_validated = []
            id_text, text = data["id"], data["texto"]
            sentences = extract_sentence(text)
            sentences_validated += [ check_expression(sentence["sentença"])   for sentence in sentences ]
            data_list_sentences = {
                "id": id_text,
                "sentenças": sentences_validated
            }
            list_sentences.append(data_list_sentences)
    
    out_file = open("output.json" ,"w", encoding='utf-8')  
    json.dump(list_sentences, out_file, indent = 4, ensure_ascii=False)  
    out_file.close()  
    


process_text()
   
   
# print(
#     result
# )
#text = "Em primeiro lugar, a forma atual de ensino, em que o aluno é obrigado a sentar-se em intervalos determinados pelos superiores, forma os adultos que levam essa forma de produção para o ofício. Logo, baseado no que foi dito, vale citar o filósofo Pitágoras, que explica que é melhor educar bem as crianças do que ter que reeducá-las como adultos. Assim, os maus hábitos adquiridos na infância podem gerar, nos adultos, muitas complicações, já que dentro da sala de aula, a movimentação dos alunos pelo ambiente é repudiada e muitas vezes com consequências. Como consequência, a doutrinação do modelo educacional não atende aos paradigmas de formação de um adulto atento à saúde ocupacional."

    #sentences = extract_sentence(text)
   
    # while punctuation in text:
        
    #     onde_corta = text[position_initial:position_final].find(punctuation)
    #     print(
    #         onde_corta
    #     )
    #     texto = text[position_initial:position_final]
    #     text = text[onde_corta:length_text]
    #     print(
    #         f"{onde_corta} // {length_text}"
    #     )
        # if position_final == 0:
        #     position_final = text.find(punctuation)
        #     texto = text[0:position_final]
        #     counter_position = counter_position + position_final 
        #     position_initial = position_final
        # else:
        #     onde_corta = text[position_initial:length_text].find(punctuation) +1
        #     conteudo = text[position_initial:length_text]
        #     position_initial = text[counter_position:length_text].find(punctuation) +1
        #     counter_position = counter_position + counter_position
        #     texto = text[position_initial:counter_position]
             
        #     print(
        #         f"ini {position_initial} // final {counter_position}"
        #     )

      
        # if len(text) == 0:
        #     break
    
    # sentence = {
    #     "id": len(sentences)  ,
    #     "sentence": texto
    # }
    # sentences.append(sentence)
    # return sentences



# pprint(
#     sentences
# )
# if "?" in text:
#     sentences = extract_sentence(text, ".")
# if "!" in text:
#     sentences = extract_sentence(text, ".")

# pprint(
#     sentences
# )




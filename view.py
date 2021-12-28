def words_into_url(url:str)-> list:
    """
    Función que recibe como parametro una url cualquiera y retorna una lista con las palabras encontradas
    """
    cont = 0
    list_words = []# lista que contendra todas las palabras encontradas en la url 
    found_word = []# lista que contiene las letras de una nueva posible palabra encontrada
    special_characters = [".","/","?q","+","_","-","&","=","//",":","%","?","#","$"]# caracteres que generalmente indican el final o separación de una palabra
    numbers = ['1','2','3','4','5','6','7','8','9','0']# lista de numeros enteros como string's
    url_separator = url.partition("https://")#Se utiliza el método partition para separar la parte de la url que se va a operar, es decir, no se tiene en cuenta la parte del "http..."  debido a que es común en cualquier url
    
    if url_separator[2] == '':
        url_separator = url.partition("http://") 
    
    string_to_evaluate = url_separator[2] #parte de la url a evaluar, lo que sigue despues de "https://" o "http://"

    for character in string_to_evaluate: #evalua cada caracter de la url
        cont += 1
        
        if character in special_characters or character in numbers: #si la letra es un caracter o un numero no la tiene en cuenta e indica el final de una posible palabra
            add_word_to_list(found_word,list_words)
            found_word.clear()#Se limpia la lista que forma la palabra

        elif len(string_to_evaluate) == cont: # se evalua si es la ultima iteración para que se incluida la ultima palabra y/o letra
            found_word.append(character)# Se agrega la letra que formará una posible palabra
            add_word_to_list(found_word,list_words)

        else:    
            found_word.append(character)# Se agrega la letra que formará una posible palabra
    
    return list_words

def add_word_to_list(found_word:str,list_words:list[str]):
    """
    Función que incluye una palabra a una listado de palabras
    """
    list_words.append(''.join(found_word))# Se agrega la nueva palabra al listado
    if len(list_words[-1]) <= 1: #evalue si la palabra contiene sola una letra para quitarla del listado
        del list_words[-1]

def repeated_word_counter(list_words:list[str])->list[tuple]:
    """
    Función que recibe como parametro una lista de palabras y retorna una lista de tuplas 
    ordenada ascedentemente por la cantidad de repeticiones de la palabra
    """
    import operator

    last = ""
    unique_list_words = []
    cont_repetitions = []
    ordered_list_words = sorted(list_words)
    for word in ordered_list_words:
        if last != word:
            unique_list_words.append(word)
            cont_repetitions.append(ordered_list_words.count(word))
        last = word
    
    result = dict(zip(unique_list_words,cont_repetitions)) #Se juntan los elementos (palabra y cantidad de repeticiones) y luego se convierte en un diccionario
    dict_resultado = dict(sorted(result.items(),key=operator.itemgetter(1),reverse=True)) #Se ordena el diccionario ascendentemente utilizando el valor, es decir, la cantidad de repeticiones de la palabra
    
    return dict(dict_resultado)
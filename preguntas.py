"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open("data.csv") as file:
        file = [row.replace("\n", "") for row in file]
        file = [row.replace("\t", ",") for row in file]
        file = [row.split(",") for row in file]
        suma=0
        suma=[int(x[1]) for x in file]
        sumcolum2=sum(suma)

    return sumcolum2
    

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    with open("data.csv") as file:
        file = [row.replace("\n", "") for row in file]
        file = [row.replace("\t", ",") for row in file]
        file = [row.split(",") for row in file]
        list_tuplas={}
        letras=[letra[0] for letra in file]
        for x in letras:
            if x in list_tuplas:
                list_tuplas[x] = list_tuplas[x]+1
            else:
                list_tuplas[x] = 1
        Resultado= sorted(list_tuplas.items())
                   
            
    return Resultado


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    
    with open("data.csv") as file:
        file = [row.replace("\n", "") for row in file]
        file = [row.replace("\t", ",") for row in file]
        file = [row.split(",") for row in file]
        list_tuplas={}
        for line in file:
            rowletras=line[0]
            rownum=line[1] 
            if rowletras in list_tuplas:
                list_tuplas[rowletras] = list_tuplas[rowletras]+int(rownum)
            else:
                list_tuplas[rowletras] = int(rownum)
        Resul= sorted(list_tuplas.items())
    return Resul
    


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open("data.csv") as file:
        file = [row.replace("\n", "") for row in file]
        file = [row.replace("\t", ",") for row in file]
        file = [row.split(",") for row in file]
        countmonth={}
        date=[x[2] for x in file]
        for line in date:
            line=line.split("-")
            month=line[1]
            if month in countmonth:
                countmonth[month]=countmonth[month]+1
            else:
                countmonth[month]= 1
        Resp= sorted(countmonth.items())
    return Resp


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open("data.csv") as file:
        file = [row.replace("\n", "") for row in file]
        file = [row.replace("\t", ",") for row in file]
        file = [row.split(",") for row in file]
        list_tuplas={}
        for line in file:
            rowletras=line[0]
            rownum=line[1]
            if rowletras in list_tuplas:
                list_tuplas[rowletras].append(rownum)
            else: list_tuplas[rowletras] = [rownum]
        for key in list_tuplas: 
            list_tuplas[key] = max(list_tuplas[key]), min(list_tuplas[key])
        list_tuplas = sorted(list_tuplas.items())
        result=[]
        for item in list_tuplas:
            result.append((item[0], int(item[1][0]), int(item[1][1])))
    return result


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open("data.csv") as file:
        file = [row.replace("\n", "") for row in file]
        file = [row.replace("\t", ",") for row in file]
        file = [row.split(",") for row in file]
        l=[]
        for line in file:
            for x in line:
                if ":" in x:
                    l.append(x)
        list=[]
        for x in l:
            list.append((x[0:3],int(x[4:6])))
            
        list_tuplas={}
        for x in list:
            letras=x[0]
            num=x[1]
            if letras in list_tuplas:
                list_tuplas[letras].append(num)
            else: list_tuplas[letras] = [num]
                
        for key in list_tuplas: 
            list_tuplas[key] = min(list_tuplas[key]), max(list_tuplas[key])
            
        list_tuplas = sorted(list_tuplas.items())
        
        result=[]
        for item in list_tuplas:
            result.append((item[0], int(item[1][0]), int(item[1][1])))
    return result


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open("data.csv") as file:
        file = [row.replace("\n", "") for row in file]
        file = [row.replace("\t", ",") for row in file]
        file = [row.split(",") for row in file]
        list_tuplas={}
        for line in file:
            rowletras=line[0]
            rownum=int(line[1])
            if rownum in list_tuplas:
                list_tuplas[rownum] = list_tuplas[rownum]+ [rowletras]
            else:
                list_tuplas[rownum] = [rowletras]
        resul= sorted(list_tuplas.items())
    return resul


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open("data.csv") as file:
        file = [row.replace("\n", "") for row in file]
        file = [row.replace("\t", ",") for row in file]
        file = [row.split(",") for row in file]
        list_tuplas={}
        for line in file:
            rowletras=line[0]
            rownum=int(line[1])
            if rownum in list_tuplas:
                list_tuplas[rownum] = list_tuplas[rownum]+ [rowletras] 
            else:
                list_tuplas[rownum] = [rowletras]
        resul= sorted(list_tuplas.items())
        lista=[]
        for x in resul:
            letter=x[1]
            letter=set(letter)
            letter=sorted(letter)
            lista.append((x[0],letter))
    return lista


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return

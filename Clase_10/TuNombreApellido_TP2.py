def problema_1(lista): #lista de nueros enteros
    #dada una lista NO VACIA con numeros aleatorios enteros positivos, reemplazar a los numeros impares
    #de la lista por su consecutivo siguiente y devolver la lista con numeros pares "listaPares"
    for i in range(len(lista)):     #recorro la lista por indice
        resto = (lista[i] % 2)      #calculo el resto de dividir por dos el elemento en la posicion i
        if resto !=0:               #si el resto no es cero, entonces es impar
            lista[i]=lista[i]+1     #cambio el elemento por el consecutivo siguiente
    listaPares=lista                #aqui digo, la lista que tengo, la guardo en otra variable llamada lista pares
    return(listaPares)# listaPares es una lista

def problema_2(numeroSerie): #numero serie es una lista
    #una empresa de seguridad diseña sus claves a partir del numero de serie del producto, que 
    #es una lista con 10 numeros enteros entre 10 y 99, los numeros dentro de la lista
    #pueden cambiar pero la cantidad siempre es de 10 elementos len(numeroSerie) es 10
    #la clave generada siempre es de 8 digitos (xx,xx,xx,xx)
    #los dos primeros digitos es el promedio de toda la lista                       (xx......)
    #los dos digitos siguientes corresponden al mayor numero de la lista            (..xx....)
    #los dos que le siguen corresponden al menor de la lista                        (....xx..)
    #los ultimos dos digitos es el numero dentro de la lista mas cercana al promedio(......xx)
    clave=[]                #arranco con una lista vacia, que se va a ir llenando con las ayudas
    suma=sum(numeroSerie)
    promedio=round(suma/len(numeroSerie))
    clave.append(promedio)  #ingresa los dos primeros numeros
    maximo=max(numeroSerie)
    clave.append(maximo)    #ingresa los dos siguientes numeros
    minimo=min(numeroSerie)
    clave.append(minimo)    #ingresa los dos siguientes numeros
    numeroSerie.sort()#ordeno de menor a mayor
    numeroSerie.reverse()# queda de mayor a menor
    distancia=[]            #creo una lista vacia, donde se guardara la destancia de cada numero al promedio
    for i in numeroSerie:
        d=abs(i-promedio)   # calculo la diferencia del numero de cada celda con el promedio
        distancia.append(d)  # y lo agrego a distancia
    distanciaMasChicaAlPromedio=min(distancia) #el minimo del arreglo pertenece al numero mas cercano al promedio
    posicion=distancia.index(distanciaMasChicaAlPromedio)
    elNumero = numeroSerie[posicion]
    clave.append(elNumero)  # y finalmente los ultimos numeros
    return(clave) #clave es una lista

def problema_3(palabra):#es de tipo string
    #se espera recibir una palabra tipo string, lo que deben hacer es invertir la palabra
    #por ejemplo, si ingresa "hola", debo retornar "aloh"
    invertida=palabra[::-1]
    return(invertida) #el tipo de dato de esta variable tiene que ser STRING


def problema_4(polinomio): #polinomio de tipo lista
    #se tiene una lista llamada polinomio, de tal manera que si el polinomio es Y=aX^2 + bX + C,
    #cada uno de sus terminos estan puestos de la siguiente manera polinomio = [a ,b ,c]
    #calcular para cada polinomio las raices y guardarlo en una lista, para retornarlo como respuesta
    listaRaices=[]                          # primero creo una lista de raices vacia
    a=polinomio[0]                          # asigo a la variable a, lo que contenga en la posicion 0, de la lista polinomio
    b=polinomio[1]                          # asigo a la variable b, lo que contenga en la posicion 1, de la lista polinomio
    c=polinomio[2]                          # asigo a la variable c, lo que contenga en la posicion 2, de la lista polinomio
    discriminante = (b**2) - 4*a*c          # calculo el discriminante
    if discriminante > 0:                   # si el discriminante es mayor a cero, va a tener dos raices
        x1 = (-b+discriminante**(1/2))/(2*a)    # la primera raiz usa el positivo
        x2 = (-b-discriminante**(1/2))/(2*a)    # la segunda raiz usa el negativo
        listaRaices.append(x1)                  #agrego la primera raiz
        listaRaices.append(x2)                  #agrego la segunda raiz
    if discriminante == 0:                  # si el discriminante es cero, solo tiene una raiz
        x1=(-b)/(2*a)                           # que se calcula asi
        listaRaices.append(x1)                  #agrego la unica raiz
    return(listaRaices)# si no tiene raices, retornar listaRaices=[], si tiene una raiz
                       # retornar listaRaices=[X1], donde X1 es el valor numerico de la raiz,
                       # si tiene dos raices retornar listaRaices=[X1 ,X2], donde X1 y X2 son valores
                       # numericos de lo que se hallo como raiz.
                       #link de ayuda 1: https://www.youtube.com/watch?v=FwMCStChZnw&t=344s&ab_channel=JULIANCLASES
                       #link de ayuda 2: https://www.youtube.com/watch?v=nDxqr-aQ1TQ&ab_channel=MateLike

def problema_5(clave): #clave es de tipo string
    #dada una clave alfa-numerica, de 10 caracteres, recorrer la clave y contar cuantos de esos 
    #caracteres son numeros, para ello investigar la funcion isNumeric
    #link de ayuda: https://www.w3schools.com/python/ref_string_isnumeric.asp
    cantidad=0
    for caracter in clave:
        if caracter.isnumeric():
            cantidad=cantidad+1
    return (cantidad)   

def problema_6(lista_libros, lista_autores, eleccion): #listas de string, eleccion es de tipo string
    #El programa recibe como parámetros una lista de libros y una lista de autores de esos 
    #mismos libros estando ordenados en correlación, es decir, en la posición 4 de lista_autores está 
    #el nombre y apellido del autor que creó el libro de la posición 4 de lista_libros. La función 
    #deberá recibir el nombre de un libro y retornar un autor. 
    #Ejemplo 
    #lista_libros = [De Profundis, Hamblet, Demian]
    #lista_autores = [Oscar Wilde, Williams Shakespeare, Herman Hesse]
    #Al ingresar Hamblet, la función debe retornar "Williams Shakespeare - Hamblet".
    autor_libro=""
    if eleccion in lista_autores:
        posicion=lista_autores.index(eleccion)
        autor_libro=lista_autores[posicion]+" - "+lista_libros[posicion]
    return(autor_libro) #Variable string 

def problema_7(mes): #Número entero positivo del 1 al 12 inclusive
    #La función recibe como parámetro un mes y retorna la cantidad de días que contiene ese mes. 
    #Ejemplo, al ingresar como parámetro el mes 4 (abril) debe retornar (30). Por cuestiones de facilidad, 
    #se debe suponer que febrero tiene 28 días.
    if mes==1:
        dias=31
    elif mes==2:
        dias=28
    elif mes==3:
        dias=31
    elif mes==4:
        dias=30
    elif mes==5:
        dias=31
    elif mes==6:
        dias=30
    elif mes==7:
        dias=31
    elif mes==8:
        dias=31
    elif mes==9:
        dias=30
    elif mes==10:
        dias=31
    elif mes==11:
        dias=30
    else:
        dias=31
    return(dias) #Número entero positivo del 1 al 31 inclusive


def problema_8(texto): #lista de string
    #El programa recibirá una lista donde se encuentre el diccionario y deberá retornar una nueva 
    #lista (abecedario_sin) donde se encontrará el abecedario sin las vocales
    texto_sin = ""
    quitar = "aeiouAEIOUáéíóúüÁÉÍÓÚÜ"
    for i in texto:
        if not(i in quitar):
            texto_sin +=i
    return(texto_sin) #lista de string




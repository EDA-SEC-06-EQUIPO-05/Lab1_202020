def buenas_peliculas(catalogo:dict,nombre_director:str)-> list:
    # Las posiciones por ahora son referencias
    num= 0
    numero_peliculas_buenas: 0
    suma_votaciones= 0
    promedio_votos= 0
    while num<len(catalogo)-1:
        if catalogo[num][5]>=6 and catalogo[num][1]==nombre_director:
            numero_peliculas_buenas+= 1
            suma_votaciones+= catalogo[num][5]
        num+= 1
    promedio_votos= suma_votaciones/numero_peliculas_buenas
    return nombre_director+" tiene "+str(numero_peliculas_buenas)+" peliculas\
           con una calificación por encima de 6, y el promedio de las\
           votaciones es de "+str(promedio_votos)
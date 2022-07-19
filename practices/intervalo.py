cont_fuera_intervalo = 0
igual_limites = False
suma_dentro_intervalo = 0


lim_inf = int(input('Introduce el limite inferior del intervalo: '))
lim_sup = int(input('Introduce el limite superior del intervalo: '))


while lim_inf > lim_sup :
    print("El limite inferior no puede ser mayor al superior.")
    print("VUELVE a introducir los limites. \n ")
    
    lim_inf = int (input ('Introducir (correctamente) el limite inferior del intervalo: '))
    lim_sup = int (input ('Introducir (correctamente) el limite superior del intervalo: '))


# num = int(input (' \n Introduce un numero (0 para salir): '))
stop = False
while stop == False:
    num = int(input('Introduce un numero (0, para salir): '))

    # Pertenece al intervalo
    if num > lim_inf and num < lim_sup:
        suma_dentro_intervalo += num
    
    # No pertenece al intervalo
    if num < lim_inf or num > lim_sup:
        cont_fuera_intervalo += 1
    
    # Numero igual a alguno de los limites
    if num == lim_inf or num == lim_sup :
        igual_limites = True
    
    # Break Condition
    elif num == 0:
        stop = True
    
    


print(' \n RESULTSADOS: ')
print(f'Suma dentro de intervalo: {suma_dentro_intervalo}')
print(f'Números fuera de intervalos: {cont_fuera_intervalo}')
print(f'Iguales a los límites: {igual_limites}')




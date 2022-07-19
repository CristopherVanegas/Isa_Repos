pediatria = 50
cardiologia = 70
dermatologia = 50
sumador = 0
opcion = input('especialidades: ')

while opcion  == 'No':
    nombres = input('Nombres de Paciente: ')

    print('ESPECIALIDADES')
    print('1.- Pediatria ($50)')
    print('2.- Cardiologia ($70)')
    print('3.-Dermatologia ($50)')
    especialidad = input('Seleccionar especialidad [1-2-3]: ')

    if especialidad == '1':
        sumador = sumador + pediatria

    if especialidad == '2': 
        sumador = sumador + cardiologia

    if especialidad == '3': 
        sumador = sumador + dermatologia

    opcion = input('¿Desea ingresar otro paciente?[Si-No] ')

print(sumador)
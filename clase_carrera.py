from enum import auto
from entities.clase_auto import Auto
from entities.clase_mecanico import Mecanico
from entities.clase_piloto import Piloto
from entities.clase_equipo import Equipo
from entities.clase_jefe_equipo import JefeEquipo


class Carrera:
    def __init__(self):
        self.empleados = []
        self.autos = []
        self.equipos = []

    def alta_empleado(self):

        try:
            print("\n----- Alta de Empleado -----")
            cedula = input("Ingrese cedula: ")
            nombre = input("Ingrese nombre: ")
            fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
            nacionalidad = input("Ingrese nacionalidad: ")
            salario = float(input("Ingrese salario: "))
            print("Ingrese cargo:")
            print("1. Piloto")
            print("2. Piloto de reserva")
            print("3. Mecánico")
            print("4. Jefe de equipo")
            cargo = input("Seleccione el cargo (1-4): ")

            if cargo not in ["1", "2", "3", "4"]:
                raise ValueError("Cargo no válido.")

            if cargo in ["1", "2"]:
                score = int(input("Ingrese score: "))
                num_auto = input("Ingrese número de auto: ")
                nuevo_empleado = Piloto(cedula, nombre, fecha_nacimiento, nacionalidad, salario, cargo, score, num_auto)
            elif cargo == "3":
                score = int(input("Ingrese score: "))
                nuevo_empleado = Mecanico(cedula, nombre, fecha_nacimiento, nacionalidad, salario, cargo, score)
            elif cargo == "4":
                nuevo_empleado = JefeEquipo(cedula, nombre, fecha_nacimiento, nacionalidad, salario, cargo)

            self.empleados.append(nuevo_empleado)
            print("Empleado agregado con éxito.")
        except Exception as e:
            print(f"Error: {e}")

    def alta_auto(self):
        try:
            print("\n----- Alta de Auto -----")
            modelo = input("Ingrese modelo: ")
            año = int(input("Ingrese año: "))
            score = int(input("Ingrese score: "))
            nuevo_auto = Auto(modelo, año, score)
            self.autos.append(nuevo_auto)
            print("Auto agregado con éxito.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error: {e}")

    def alta_equipo(self):
        try:
            print("\n----- Alta de Equipo -----")
            nombre_equipo = input("Ingrese nombre del equipo: ")
            modelo_auto = input("Ingrese modelo de auto: ")

            empleados_equipo = []
            for i in range(12):
                print(f"Ingrese cedula del empleado {i+1}:")
                cedula_empleado = input()
                empleado = next((emp for emp in self.empleados if emp.cedula == cedula_empleado), None)
                if empleado:
                    empleados_equipo.append(empleado)
                else:
                    raise ValueError("Empleado no encontrado.")

            nuevo_equipo = Equipo(nombre_equipo, modelo_auto, empleados_equipo)
            self.equipos.append(nuevo_equipo)
            print("Equipo agregado con éxito.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error: {e}")

    def simular_carrera(self):
        try:
            print("\n----- Simular Carrera -----")
            pilotos_lesionados = input("Ingrese nro de auto de todos los pilotos lesionados: ")
            pilotos_abandonan = input("Ingrese nro auto de todos los pilotos que abandonan: ")
            pilotos_errores_pits = input("Ingrese nro de auto de todos los pilotos que cometen error en pits: ")
            pilotos_penalidad = input("Ingrese nro de auto de todos los pilotos que reciben penalidad: ")

            pilotos_lesionados = pilotos_lesionados.split(',') if pilotos_lesionados else []
            pilotos_abandonan = pilotos_abandonan.split(',') if pilotos_abandonan else []
            pilotos_errores_pits = pilotos_errores_pits.split(',') if pilotos_errores_pits else []
            pilotos_penalidad = pilotos_penalidad.split(',') if pilotos_penalidad else []

            for piloto in self.pilotos_titulares:
                if piloto.num_auto in pilotos_lesionados:
                    piloto.lesionado = True
                if piloto.num_auto in pilotos_abandonan:
                    piloto.abandonar()
                if piloto.num_auto in pilotos_errores_pits:
                    piloto.errores_pits += 1
                if piloto.num_auto in pilotos_penalidad:
                    piloto.penales += 1
                    
                    resultados_carrera = self.simular_carrera_real()

            print("\n----- Resultados de la Carrera -----")
            for i, (piloto, _) in enumerate(resultados_carrera, start=1):
                print(f"{i}. {piloto.nombre} - Auto {piloto.num_auto}")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error: {e}")


    def realizar_consultas(self):
        try:
            print("\n----- Realizar Consultas -----")
            print("1. Top 10 pilotos con más puntos en el campeonato")
            print("2. Resumen campeonato de constructores (equipos)")
            print("3. Top 5 pilotos mejores pago")
            print("4. Top 3 pilotos más habilidosos")
            print("5. Retornar jefes de equipo")

            opcion_consulta = int(input("Seleccione una consulta (1-5): "))

            if opcion_consulta == 1:
                top_10_pilotos = self.top_10_pilotos()
                print("\n----- Top 10 Pilotos con más puntos en el campeonato -----")
                for i, piloto in enumerate(top_10_pilotos, start=1):
                    print(f"{i}. {piloto.nombre} - Puntos: {piloto.puntaje_campeonato}")
            elif opcion_consulta == 2:
                resumen_constructores = self.resumen_campeonato_constructores()
                print("\n----- Resumen Campeonato de Constructores -----")
                for equipo, puntos in resumen_constructores:
                    print(f"{equipo.nombre} - Puntos: {puntos}")
            elif opcion_consulta == 3:
                top_5_mejores_pago = self.top_5_pilotos_mejores_pago()
                print("\n----- Top 5 Pilotos Mejor Pagados -----")
                for i, piloto in enumerate(top_5_mejores_pago, start=1):
                    print(f"{i}. {piloto.nombre} - Salario: {piloto.salario}")
            elif opcion_consulta == 4:
                top_3_habilidosos = self.top_3_pilotos_mas_habilidosos()
                print("\n----- Top 3 Pilotos Más Habilidosos -----")
                for i, piloto in enumerate(top_3_habilidosos, start=1):
                    print(f"{i}. {piloto.nombre} - Score: {piloto.score}")
            elif opcion_consulta == 5:
                jefes_equipo = self.retornar_jefes_de_equipo()
                print("\n----- Jefes de Equipo -----")
                for jefe, equipo in jefes_equipo:
                    print(f"{jefe.nombre} - Equipo: {equipo}")
            else:
                print("Opción de consulta no válida.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error: {e}")

# Ejemplo de uso
carrera = Carrera.simular_carrera(4)
consultas = Carrera.realizar_consultas(3)

#Datos
empleados = [
    Piloto("12345678", "Juan","01/10/1980", "uru","100","piloto","70","2"),
    Piloto("12345671", "Juan","12/10/1980", "uru","100","piloto","70","2"),
    Piloto("12345672", "Juan","13/10/1980", "uru","100","piloto","70","2"),
    Piloto("12345673", "Juan","14/10/1980", "uru","100","piloto","70","2"),
    Piloto("12345674", "Juan","15/10/1980", "uru","100","piloto","70","2"),
    Piloto("12345675", "Juan","16/10/1980", "uru","100","piloto","70","2"),
    Piloto("12345676", "Juan","17/10/1980", "uru","100","piloto","70","2"),
    Piloto("12345677", "Juan","18/10/1980", "uru","100","piloto","70","2"),
    Piloto("12345678", "Juan","19/10/1980", "uru","100","piloto","70","2"),
    Piloto("12345679", "Juan","20/10/1980", "uru","100","piloto","70","2"),
    Mecanico("24611022","Luis","08/07/1997", "arg","70","mecanico","34"),
    Mecanico("24621022","Luis","09/07/1997", "arg","70","mecanico","50"),
    Mecanico("24631022","Luis","10/07/1997", "arg","70","mecanico","45"),
    Mecanico("24641022","Luis","11/07/1997", "arg","70","mecanico","33"),
    Mecanico("24651022","Luis","12/07/1997", "arg","70","mecanico","21"),
    Mecanico("24661022","Luis","13/07/1997", "arg","70","mecanico","37"),
    Mecanico("24671022","Luis","14/07/1997", "arg","70","mecanico","21"),
    Mecanico("24681022","Luis","15/07/1997", "arg","70","mecanico","76"),
    Mecanico("24691022","Luis","16/07/1997", "arg","70","mecanico","54"),
    Mecanico("24331022","Luis","17/07/1997", "arg","70","mecanico","31"),
    Mecanico("21681022","Luis","18/07/1997", "arg","70","mecanico","34"),
    JefeEquipo("1357913", "Carlos", "01/01/1974", "bra", "150", "jefe de equipo"),
    JefeEquipo("2257913", "Carlos", "02/01/1974", "bra", "150", "jefe de equipo"),
    JefeEquipo("1358813", "Carlos", "03/01/1974", "bra", "150", "jefe de equipo"),
    JefeEquipo("1357944", "Carlos", "04/01/1974", "bra", "150", "jefe de equipo"),
    JefeEquipo("1356913", "Carlos", "05/01/1974", "bra", "150", "jefe de equipo"),
    JefeEquipo("1557913", "Carlos", "06/01/1974", "bra", "150", "jefe de equipo"),
    JefeEquipo("1357913", "Carlos", "07/01/1974", "bra", "150", "jefe de equipo"),
    JefeEquipo("1377913", "Carlos", "08/01/1974", "bra", "150", "jefe de equipo"),
    JefeEquipo("1357993", "Carlos", "09/01/1974", "bra", "150", "jefe de equipo"),
    JefeEquipo("1457913", "Carlos", "10/01/1974", "bra", "150", "jefe de equipo"),
]
autos = [
    Auto("suzuki","2011", "56"),
    Auto("chevrolet","2012", "32"),
    Auto("ford","2013", "45"),
    Auto("nissan","2014", "48"),
    Auto("suzuki","2015", "32"),
    Auto("chevrolet","2016", "14"),
    Auto("ford","2017", "89"),
    Auto("nissan","2018", "31"),
    Auto("suzuki","2019", "78"),
    Auto("chevrolet","2010", "53"),
    
]

equipos = [
    Equipo("Hola","chevrolet","7"),
    Equipo("Chau","suzuki","7"),
    Equipo("Coso","ford","7"),
    Equipo("Dioni","nissan","7"),
    Equipo("Cualca","nissan","7"),

]



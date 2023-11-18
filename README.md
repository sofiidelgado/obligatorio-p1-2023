# obligatorio-p1-2023
Proyecto de Simulación de Carreras de Automovilismo

Este proyecto implementa un sistema de gestión para simular carreras
de automovilismo. Los equipos cuentan con pilotos, mecánicos,
directores de equipo y autos con modelos y scores específicos para
cada temporada.

Estructura del Proyecto

La estructura del proyecto es la siguiente:

proyecto/
|-- clase_carrera.py
|-- entities/
|   |-- __init__.py
|   |-- Auto.py
|   |-- Empleado.py
|   |-- JefeEquipo.py
|   |-- Mecanico.py
|   |-- Piloto.py
|   |-- Equipo.py
|-- README.md

clase_carrera.py: Archivo principal que contiene la lógica principal y el menú
del programa.
entities/: Directorio que contiene las clases relacionadas con el
modelo de negocio.

Auto.py: Clase que representa el modelo de un auto.
Empleado.py: Clase base para representar a los empleados.
JefeEquipo.py: Clase que representa al director de un equipo.
Mecanico.py: Clase que representa a un mecánico.
Piloto.py: Clase que representa a un piloto.
Equipo.py: Clase que representa a un equipo.

Instrucciones de Uso

Clona el repositorio: git clone https://github.com/tu-usuario/tu-proyecto.git
Navega al directorio del proyecto: cd tu-proyecto

Funcionalidades Principales

Alta de Empleado: Permite ingresar la información de un nuevo
empleado, incluyendo pilotos, mecánicos y directores de equipo.

Alta de Auto: Permite ingresar la información de un nuevo auto para la
temporada.

Alta de Equipo: Permite ingresar la información de un nuevo equipo,
asociando empleados y un modelo de auto.

Simular Carrera: Permite simular una carrera ingresando información
sobre pilotos lesionados, abandonos, errores en pits y penalidades.

Realizar Consultas: Proporciona consultas como el top 10 de pilotos
con más puntos en el campeonato, resumen del campeonato de
constructores, etc.

Finalizar Programa: Cierra la aplicación.

Requisitos

Python 3.x

Autoras

Leticia Damborena, Sofia Delgado, Belen Varela

Contribuciones
Decidimos trabajar en una sola computadora pero haciendo el metodo de Pair Programming, es por eso que los commits figuran desde una sola cuenta.
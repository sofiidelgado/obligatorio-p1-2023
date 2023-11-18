from abc import ABC

class Empleado(ABC):
    empleados = 0
    def __init__(self, cedula, nombre, fecha_nacimiento, nacionalidad, salario, cargo):
        self.empleados += 1
        self.cedula = cedula
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad
        self.salario = salario
        self.cargo = cargo
        
    @property
    def cedula(self):
        return self.cedula 
    
    @property
    def nombre(self):
        return self.nombre

    @property
    def fecha_nacimiento(self):
        return self.fecha_nacimiento
    
    @property
    def nacionalidad(self):
        return self.nacionalidad
    
    @property
    def salario(self):
        return self.salario

    @property
    def cargo(self):
        return self.cargo
        
    @cedula.setter
    def cedula(self,cedula):
        self.cedula = cedula


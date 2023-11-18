from entities.clase_empleado import Empleado

class JefeEquipo(Empleado):
    def __init__(self, cedula, nombre, fecha_nacimiento, nacionalidad, salario, cargo):
        super().__init__(cedula, nombre, fecha_nacimiento, nacionalidad, salario, cargo)

    @property
    def cedula(self):
     return self._cedula 
    
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


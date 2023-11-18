from entities.clase_empleado import Empleado

class Mecanico(Empleado):
    def __init__(self, cedula, nombre, fecha_nacimiento, nacionalidad, salario, cargo, score):
        super().__init__(cedula, nombre, fecha_nacimiento, nacionalidad, salario, cargo)
        self.score = score

    @property
    def score(self):
        return self.score
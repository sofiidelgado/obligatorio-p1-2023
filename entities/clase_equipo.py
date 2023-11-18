class Equipo:
    def __init__(self, nombre, modelo_auto, empleados):
        self.nombre = nombre
        self.modelo_auto = modelo_auto
        self.empleados = empleados

    @property
    def nombre(self):
        return self.nombre
    
    @property
    def modelo_auto(self):
        return self.modelo_auto
    
    @property
    def empleados(self):
        return self.empleados
    
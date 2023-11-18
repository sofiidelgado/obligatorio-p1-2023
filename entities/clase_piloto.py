from entities.clase_empleado import Empleado

class Piloto(Empleado):
    def __init__(self, cedula, nombre, fecha_nacimiento, nacionalidad, salario, cargo, score, num_auto):
        super().__init__(cedula, nombre, fecha_nacimiento, nacionalidad, salario, cargo)
        self.score = score
        self.num_auto = num_auto
        self.puntaje_campeonato = 0
        self.lesionado = False
        self.errores_pits = 0
        self.penales = 0

    @property
    def score(self):
        return self.score
    
    @property
    def cedula(self):
        return self.cedula
    
    @property
    def num_auto(self):
        return self.num_auto

    @property
    def puntaje_campeonato(self):
        return self.puntaje_campeonato
    
    @property
    def lesionado(self):
        return self.lesionado
    
    @property
    def errores_pits(self):
        return self.errores_pits
    
    @property
    def penales(self):
        return self.penales
        
    @cedula.setter
    def cedula(self,cedula):
        self.cedula = cedula


    @puntaje_campeonato.setter
    def puntaje_campeonato(self,puntaje_campeonato):
        self._puntaje_campeonato = puntaje_campeonato
    
    @lesionado.setter
    def lesionado(self, lesionado):
        self.lesionado = lesionado
    
from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo=None,asignaturas=[],estudiantes=[]):
        self._asignaturas  =  asignaturas
        if grupo is None:
            self._grupo = "grupo predeterminado"
        else:
            self._grupo = grupo
        self.listadoAlumnos = estudiantes
        
    

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if  lista is  None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista
      

    def __str__(self):
         return "Grupo de Estudiantes: "+  self._grupo

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
      
        cls.grado = nombre
        
  

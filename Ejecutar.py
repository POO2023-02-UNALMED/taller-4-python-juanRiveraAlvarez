from classroom.asignatura import Asignatura
from classroom.grupo import Grupo


Grupo.asignarNombre()
nombre1 = Grupo.grado

Grupo.asignarNombre("Grado 34")
nombre2 = Grupo.grado

Grupo.asignarNombre("otra grado")
    
ok = False
if nombre1 == "Grado 6" and nombre2 == "Grado 34" and Grupo.grado == "otra grado":
    ok = True

print(ok)
    
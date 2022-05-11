
from gestionAlumnos.models import Alumnos

nombres = [
        "JOHAN ESTIBEN ACARO MASACHE",
        "JOSE JAVIER ALAMO MORGADO",
        "SERGIO CAMINO SAIZ",
        "IOANA-ADRIANA COADA",
        "ASTRID CAROLINA CRUCES HUAMANI",
        "JUAN DEL CAMPO CRUZ",
        "ALBERTO CARLOS DIAZ LAZARO",
        "DANIEL FERNANDEZ GARCIA-CARPINTERO",
        "IKER GOMEZ ADAN",
        "JAVIER GOMEZ DE MARCOS LOPEZ",
        "DIEGO GÓMEZ GONZÁLEZ",
        "JUAN SEBASTIAN GONZALEZ LOPEZ",
        "JAVIER GUTIERREZ GUTIERREZ",
        "JOHN BRYAN LEINES CAMALLE",
        "ANGEL LOPEZ MELERO",
        "MARIO LUQUERO IÑIGUEZ",
        "JAVIER MARTIN ARROYO",
        "RAFAEL MARTINEZ LINARES",
        "FRANCISCO JAVIER NOVAL TOLDOS",
        "ISLA PEINADO HENRIQUEZ",
        "JUAN MARCIAL PORTILLA ZAMBRANO",
        "JAVIER SANCHEZ CARRIZO",
        "VICTOR SANCHEZ GRANDE",
        "ADRIAN TAUSTE SAIZ",
        "MARIO VALVERDE DIAZ - MALAGUILLA",
        "DAVID VALVERDE FERNANDEZ",
        "JAVIER VILLALOBOS PASTOR", 
        "IVAN GONZALZ GORDO"
    ]

for x in nombres:
    al = Alumnos(nombre=x)
    bus = Alumnos.objects.filter(nombre__iexact=x)
    if not bus:
        al.save()
        alertas = "Alumno registrado correctamente!"
    else:
        alertas = "Alumno ya existente!"

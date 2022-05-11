todos = [
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
usuarios = []
nombres = []

for x in range(len(todos)):
    username = ""
    name = todos[x].__str__()
    nombres.append(name)
    #print(len(name))
    for y in range(len(name)):
        if name[y] != " ":
            #print(x[y])
            username += name[y]
        else:
            break
    username += "."
    
    for z in range(3):
            username += name[z+y+1]
    usuarios.append(username.lower())

from django.contrib.auth.models import User

for x in range(len(usuarios)):
    #user = User(username=x, password="campusfp")
    print(x)
    user = User.objects.create_user(str(usuarios[x]), '', 'campusfp')
    user.first_name = str(nombres[x])
    user.save()
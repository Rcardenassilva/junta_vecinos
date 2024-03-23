import random
import string

# Lista de nombres de usuarios
nombres = ["Usuario 1", "Usuario 2", "Usuario 3", "Usuario 4", "Usuario 5",
           "Usuario 6", "Usuario 7", "Usuario 8", "Usuario 9", "Usuario 10"]

# Función para generar una contraseña aleatoria
def generar_contrasena():
  longitud = 12
  contrasena = " ".join(random.choice(caracteres) for _ in range(longitud))
  return contrasena

# Diccionario para almacenar las cuentas
cuentas = {}

# Bucle para crear las cuentas
for nombre in nombres:
  # Generar contraseña aleatoria
  contrasena = generar_contrasena()

  # Pedir número de teléfono
  while True:
    telefono = input(f"Introduzca el número de teléfono para {nombre}: ")
    if telefono.isdigit() and len(telefono) == 8:
      break
    print("El número de teléfono debe tener 8 dígitos numéricos.")

  # Almacenar la cuenta
  cuentas[nombre] = {"contrasena": contrasena, "telefono": telefono}

# Mostrar las cuentas
for nombre, cuenta in cuentas.items():
  print(f"Nombre: {nombre}")
  print(f"Contraseña: {cuenta['contrasena']}")
  print(f"Teléfono: {cuenta['telefono']}")

# Mensaje final
print("Todas las cuentas han sido creadas.")
import random
import timeit

# Representación de usuario con una clase
class Usuario:
    def __init__(self, user_id, nombre, edad):
        self.id = user_id
        self.nombre = nombre
        self.edad = edad
    
    def __repr__(self):
        return f"Usuario({self.id}, {self.nombre}, {self.edad})"

# Generar 100,000 usuarios automáticamente
nombres = ["Carlos", "Ana", "Luis", "Maria", "Jorge", "Elena", "Pablo", "Lucia"]
usuarios = [Usuario(i, random.choice(nombres), random.randint(18, 80)) for i in range(100000)]

# Búsqueda lineal
def busqueda_lineal(usuarios, user_id):
    for usuario in usuarios:
        if usuario.id == user_id:
            return usuario
    return None

# Búsqueda binaria (requiere lista ordenada)
def busqueda_binaria(usuarios, user_id):
    izquierda, derecha = 0, len(usuarios) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if usuarios[medio].id == user_id:
            return usuarios[medio]
        elif usuarios[medio].id < user_id:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None

# Ordenar usuarios por ID para búsqueda binaria
usuarios.sort(key=lambda x: x.id)

# Permitir al usuario ingresar un ID para buscar
target_id = int(input("Ingrese el ID a buscar: "))

# Medir tiempos
tiempo_lineal = timeit.timeit(lambda: busqueda_lineal(usuarios, target_id), number=1)
tiempo_binaria = timeit.timeit(lambda: busqueda_binaria(usuarios, target_id), number=1)

usuario_encontrado_lineal = busqueda_lineal(usuarios, target_id)
usuario_encontrado_binaria = busqueda_binaria(usuarios, target_id)

print(f"Tiempo búsqueda lineal: {tiempo_lineal:.6f} segundos")
print(f"Tiempo búsqueda binaria: {tiempo_binaria:.6f} segundos")

if usuario_encontrado_lineal:
    print(f"Usuario encontrado: {usuario_encontrado_lineal}")
else:
    print("Usuario no encontrado.")

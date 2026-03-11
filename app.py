heroes = [
    {"nombre": "Spider-Man", "universo": "Marvel", "poder": "Agilidad", "nivel": 85},
    {"nombre": "Iron Man", "universo": "Marvel", "poder": "Tecnologia", "nivel": 90},
    {"nombre": "Batman", "universo": "DC", "poder": "Inteligencia", "nivel": 88},
    {"nombre": "Superman", "universo": "DC", "poder": "Fuerza", "nivel": 98}
]

equipo = []
suma_nivel = 0
marvel = 0
dc = 0

print("\n------- Bienvenido, vamos a crear nuestro equipo para la batalla! -------\n")

for i, heroe in enumerate(heroes, start=1):
    print(f"{i}. {heroe['nombre']}")
    print(f"   Universo: {heroe['universo']}")
    print(f"   Poder: {heroe['poder']}")
    print(f"   Nivel: {heroe['nivel']}")

print("\nVamos a armar el equipo!")

while True:

    print("\nHéroes disponibles:\n")

    for i, heroe in enumerate(heroes, start=1):
        print(f"{i}. {heroe['nombre']}")

    opcion = int(input("Elige un héroe (0 para terminar): "))

    if opcion == 0:
        break

    if opcion < 1 or opcion > len(heroes):
        print("0 Opción inválida.")
        continue

    heroe_elegido = heroes[opcion - 1]

    # VALIDAR QUE NO SE REPITA
    if heroe_elegido in equipo:
        print(" Ese héroe ya está en tu equipo.")
        continue

    equipo.append(heroe_elegido)

    print(f" {heroe_elegido['nombre']} agregado al equipo")

print("\n----------- TU EQUIPO -----------\n")

for heroe in equipo:
    print(f"Heroe: {heroe['nombre']}")
    print(f"Universo: {heroe['universo']}")
    print(f"Habilidad: {heroe['poder']}")
    print(f"Nivel: {heroe['nivel']}")
    print("-------------------")

    suma_nivel += heroe["nivel"]

    if heroe["universo"] == "Marvel":
        marvel += 1
    else:
        dc += 1

print("\nNivel total del equipo:", suma_nivel)
print("Héroes de Marvel:", marvel)
print("Héroes de DC:", dc)

print("\n--------- ESTAMOS LISTOS PARA LA BATALLA ---------\n")
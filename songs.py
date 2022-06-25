def cancion(num):
    match num:
        case 1:
            return"I want to break free, I want to break free I want to break free from your lies"
        case 2:
            return "Quiero que se repita la ocacion"
        case 3:
            return "Te Felicito que bien actuas"
        case _:
            return "La opcion que buscas no se encuentra"
print(cancion(1))
print(cancion(2))
print(cancion(3))
print(cancion(10))

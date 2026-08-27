class Scooter :
    def __init__(sctr ,id : str = "Sin id",bateria : int = "100", disponibilidad : bool = True ) :
        #ATRIBUTOS PREDEFINIDOS DE LA CLASE SCOOTER
        sctr.__id = id
        sctr.__bateria = bateria
        sctr.__disponibilidad = disponibilidad

    #Decidi adelantarme con los getters jeje
    def getId(sctr) -> str:
        return sctr.__id

    def getBateria(sctr) -> int:
        return sctr.__bateria

    def getDisponibilidad(sctr) -> bool:
        return sctr.__disponibilidad


class Usuario :
    #ATRIBUTOS PREDEFINIDOS DE LA CLASE USUARIO
    def __init__(user,nombre : str = "Sin nombre", saldo : float = "0.0") :
        user.__nombre = nombre
        user.__saldo = saldo  

    #Aca tambien 
    def getNombre(user) -> str:
        return user.__nombre
    def getSaldo(user) -> float:
        return user.__saldo

#Quiero ver si me quedo bien

scooter1 = Scooter()

scooter2 = Scooter("S-302",65,False)

usuario1 = Usuario()

usuario2 = Usuario("Rafa",1000)

print("=========SCOOTERS=========")
print(f"Scooter 1 : {scooter1.getId()} | {scooter1.getBateria()} | {scooter1.getDisponibilidad()}")
print(f"Scooter 2 : {scooter2.getId()} | {scooter2.getBateria()} | {scooter2.getDisponibilidad()}\n")

print("=========USUARIOS=========")
print(f"usuario 1 : {usuario1.getNombre()} | {usuario1.getSaldo()}")
print(f"usuario 2 : {usuario2.getNombre()} | {usuario2.getSaldo()}")

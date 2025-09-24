class Animal:
    def __init__(self, species: str , sound: str = ""):  # construtor
        self.species = species
        self.sound = sound
        self.age = 0

    def speak(self):
        return f"{self.species} makes a sound."
    def __str__(self):
        return f"{self.species}:{self.age}:{self.sound}"
    def isage(self) -> str:
        if self.age == 0:
            return "filhote"
        if self.age == 1:
            return "crianca"
        if self.age == 2:
            return "adulto"
        if self.age == 3:
            return "idoso"
        if self.age == 4:
            return "morto"
        else:
            return "invalido"
        
    
    
def main():   
    animal: Animal = Animal("", "")  # 2: criar um obj com qq valor inicial
    while True:  # 3: loop infinito

        line: str = input()  # 4: perguntar ao usuario
        print("$" + line)  # echo
        args: list[str] = line.split(" ")  # 5: separar argumentos

        if args[0] == "end":
            break
        
        elif args[0] == "grow":
                animal.age += int(args[1])
        elif args[0] == "init":  # species age sound
            species: str = args[1]
            sound: str = args[2]
            animal = Animal(species, sound)
        elif args[0] == "sound":
            print(animal.speak())
        elif args[0] == "age":
            print(animal.isage())
        elif args[0] == "show":
            print(animal)
        else:  # 7: erro
            print("fail: comando não encontrado")
main()
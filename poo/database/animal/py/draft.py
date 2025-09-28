class Animal:
    def __init__(self, species: str, sound: str = ""):
        self.species = species
        self.sound = sound
        self.age = 0  # filhote

    def __str__(self):
        return f"{self.species}:{self.age}:{self.sound}"

    def ageBy(self, increment: int):
        if self.age == 4:
            print(f"warning: {self.species} morreu")
            return
        self.age += increment
        if self.age >= 4:
            self.age = 4
            print(f"warning: {self.species} morreu")

    def makeSound(self):
        if self.age == 0:
            return "---"  # filhote
        elif self.age == 4:
            return "RIP"  # morto
        else:
            return self.sound  # som característico

    def isage(self) -> str:
        if self.age == 0:
            return "filhote"
        elif self.age == 1:
            return "crianca"
        elif self.age == 2:
            return "adulto"
        elif self.age == 3:
            return "idoso"
        elif self.age == 4:
            return "morto"
        else:
            return "invalido"

def main():
    animal = Animal("", "")
    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "init":
            species = args[1]
            sound = args[2]
            animal = Animal(species, sound)
        elif args[0] == "grow":
            animal.ageBy(int(args[1]))
        elif args[0] == "noise":
            print(animal.makeSound())
        elif args[0] == "age":
            print(animal.isage())
        elif args[0] == "show":
            print(animal)
        else:
            print("fail: comando não encontrado")

if __name__ == "__main__":
    main()

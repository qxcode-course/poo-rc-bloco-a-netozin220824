class Carro:
    def __init__(self) -> None:
        self.pass_: int = 0
        self.gas: int = 0
        self.km: int = 0
        self.passMax: int = 2
        self.gasMax: int = 100

    def __str__(self) -> str:
        return f"pass: {self.pass_}, gas: {self.gas}, km: {self.km}"

    def show(self) -> None:
        print(self)

    def enter(self) -> None:
        if self.pass_ < self.passMax:
            self.pass_ += 1
        else:
            print("fail: limite de pessoas atingido")

    def leave(self) -> None:
        if self.pass_ > 0:
            self.pass_ -= 1
        else:
            print("fail: nao ha ninguem no carro")

    def fuel(self, amount: int) -> None:
        self.gas += amount
        if self.gas > self.gasMax:
            self.gas = self.gasMax

    def drive(self, distance: int) -> None:
        if self.pass_ == 0:
            print("fail: nao ha ninguem no carro")
            return
        if self.gas == 0:
            print("fail: tanque vazio")
            return
        if self.gas >= distance:
            self.gas -= distance
            self.km += distance
        else:
            km_possivel: int = self.gas
            self.km += km_possivel
            self.gas = 0
            print(f"fail: tanque vazio apos andar {km_possivel} km")

def main() -> None:
    carro = Carro()
    while True:
        try:
            line: str = input()
        except EOFError:
            break

        print("$" + line)
        args: list[str] = line.split()

        if len(args) == 0:
            continue

        cmd: str = args[0]

        if cmd == "end":
            break
        elif cmd == "show":
            carro.show()
        elif cmd == "enter":
            carro.enter()
        elif cmd == "leave":
            carro.leave()
        elif cmd == "fuel":
            if len(args) < 2:
                print("fail: informe a quantidade de combustível")
                continue
            amount: int = int(args[1])
            carro.fuel(amount)
        elif cmd == "drive":
            if len(args) < 2:
                print("fail: informe a distância")
                continue
            distance: int = int(args[1])
            carro.drive(distance)
        else:
            print("fail: comando não encontrado")

if __name__ == "__main__":
    main()



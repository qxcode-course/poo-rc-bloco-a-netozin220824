class Calculadora:
    def __init__(self, batteryMax: int):
        self.batteryMax: int = batteryMax
        self.display: float = 0
        self.battery : int = 0

    def __str__(self) -> str:
        return f"display = {self.display:.2f}, battery = {self.battery}"
    def show(self) -> None:
        print(self)
    def charge(self, amount: int) -> None:
        self.battery += amount
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax
    def ret(self) -> bool:
        if self.battery == 0:
            print("fail: bateria insuficiente")
            return False
        self.battery -= 1
        return True
    def sum(self, a: float, b: float) -> None:
        if not self.ret():
            return
        self.display = a + b
    def sub(self, a: float, b: float) -> None:
        if not self.ret():
            return
        self.display = a - b
    def mul(self, a: float, b: float) -> None:
        if not self.ret():
            return
        self.display = a * b
    def div(self, a: float, b: float) -> None:
        if not self.ret():
            return
        if b == 0:
            print("fail: divisao por zero")
            return
        self.display = a / b
def main() -> None:
        calc=Calculadora(0)
        while True:
                line: str = input()
                if line == "end":
                    print("$end")
                    break
                print("$" + line)
                args: list[str] = line.split()
                if args[0] == "init":
                       calc=Calculadora(int(args[1]))
                elif args[0]=="show":
                       calc.show()
                elif args[0]=="charge":
                       calc.charge(int(args[1]))
                elif args[0] == "sum":
                       calc.sum(float(args[1]), float(args[2]))
                elif args[0] == "sub":
                       calc.sub(float(args[1]), float(args[2]))
                elif args[0] == "div":
                       calc.div(float(args[1]), float(args[2]))
                elif args[0] == "mul":
                       calc.mul(float(args[1]), float(args[2]))

main()

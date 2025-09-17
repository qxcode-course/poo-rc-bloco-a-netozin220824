class Towel:#classe
    def __init__(self,color: str,size:str):#construtor 
        self.color: str = color #atributo
        self.size: str = size
        self.wetness:int = 0

#referencias
print("qual a cor da sua toalha, é o tamanho")
color = input()
size = input()
minha: Towel = Towel(color, size)
print(f"sua toalha é {minha.color} e o tamanho é {minha.size}")
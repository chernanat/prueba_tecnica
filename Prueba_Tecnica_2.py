import re
class Objeto():
    Estado = 0
    def Operation(self,Cadena):
        for i in Cadena:
            if i == '+' or i == '-' or i == '*' or i == '/':
                Estado = 1
                return True
                break
            else:
                return False
    def Compute(self,Cadena):
        Estado = 0
        if Estado == 1:
            for i in Cadena:
                valor = Cadena
                return print(int(valor))
        else:
            return False

a = "Hello world" 
b = "2+10/2-20" 
c = "(2 + 10) / 2 - 20" 
d = "(2 + 10 / 2 - 20"

clase = Objeto()
print(clase.Operation(a))
print(clase.Operation(b))
print(clase.Operation(c))
print(clase.Operation(d))

clase.Compute(a)
clase.Compute(b)
clase.Compute(c)
clase.Compute(d)



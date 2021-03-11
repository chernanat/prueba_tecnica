import numpy as np
a = np.array([1,2])
b = np.array([[1,2],[2,4]])
c = np.array([[1,2],[2,4],[2,4]])
d = np.array([[[3,4],[6,5]]])
f = np.array([[[1, 2, 3], [2, 3, 4]], [[5, 6, 7], [5, 4, 3]], [[3, 5, 6], [4, 8, 3]]])
class MiMatriz():
    #metodos dimension, compute y straight respectivamente
    #funcion la cual retorna la dimension del arreglo
    def Dimension(self,matrix):
        return matrix.ndim
    #metodo que retorna la suma de una matriz
    def Compute(self,matrix): 
        return np.sum(matrix)
o = MiMatriz()
#Salida de pantalla para las dimensiones de cada arreglo
print("Dimension Vector A:",o.Dimension(a))
print("Dimension Vector B:",o.Dimension(b))
print("Dimension Vector C:",o.Dimension(c))
print("Dimension Vector D:",o.Dimension(d))
print("Dimension Vector F:",o.Dimension(f))

#Salida de pantalla para las sumas de cada arreglo
print("La suma de los elementos Vector A:",o.Compute(a))
print("La suma de los elementos Vector B:",o.Compute(b))
print("La suma de los elementos Vector C:",o.Compute(c))
print("La suma de los elementos Vector D:",o.Compute(d))
print("La suma de los elementos Vector F:",o.Compute(f))









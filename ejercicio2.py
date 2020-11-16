'''
-----------------------------
 EJERCICIO N°2
 Calculando el IMC
-----------------------------
¿Cómo podríamos asegurarnos de que los valores en los argumentos tienen sentido?
-----------------------------
'''
def imc(peso, altura):
  return peso / altura ** 2

print(imc(52.5, 1.65))

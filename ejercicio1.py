'''
-----------------------------
 EJERCICIO N°1
 Alcances (scopes)
-----------------------------
'''
def miFuncion():
  print("¿Conozco a la variable?", var)

var = 1
miFuncion()
print(var)

'''
-----------------------------
1. Agrega "var = 2" a la función y observa lo que ocurre
2. Ahora agrega "global var"
'''

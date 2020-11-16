'''
-----------------------------
 EJERCICIO N°3
 Triángulos
-----------------------------
'''
def esUnTriangulo(a, b, c):
  if a + b <= c:
    return False
  if b + c <= a:
    return False
  if c + a <= b:
    return False
  return True

# La función se puede compactar aún más?
print(esUnTriangulo (1, 1, 1))
print(esUnTriangulo (1, 1, 3))


'''
def esUnTrianguloRectangulo(a, b, c):
  if not esUnTriangulo  (a, b, c):
    return False
  if a > b and a > c:
    return a ** 2 == b ** 2 + c ** 2
  if b > a and b > c:
    return b ** 2 == a ** 2 + c ** 2
  if c > a and c > b:
    return c ** 2 == a ** 2 + b ** 2

# Entradas del usuario
a = float(input("Ingresa la longitud del primer lado: "))
b = float(input("Ingresa la longitud del segundo lado: "))
c = float(input("Ingresa la longitud del tercer lado: "))

# Código principal
if esUnTrianguloRectangulo(a, b, c):
  print("Felicidades, es un triángulo rectángulo.")
else:
  print("Lo siento, no puede ser un triángulo rectángulo.")

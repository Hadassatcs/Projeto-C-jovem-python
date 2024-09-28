def area_quadrado(lado):
  """Calcula a área de um quadrado."""
  return lado * lado

def area_retangulo(base, altura):
  """Calcula a área de um retângulo."""
  return base * altura

# Calculando a área de um quadrado de lado 4
lado_quadrado = 4
area_quad = area_quadrado(lado_quadrado)
print("A área do quadrado é:", area_quad)

# Definimos as medidas de um retângulo
base = 5
altura = 3
# Chamamos a função para calcular a área
area = area_retangulo(base, altura)
# Imprimimos o resultado
print("A área do retângulo é:", area)


PS C:\Users\Usuario\Desktop\PROJETO 1> & C:/Users/Usuario/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/Usuario/Desktop/PROJETO 1/figuras_geométricas.py"
A área do quadrado é: 16
A área do retângulo é: 15

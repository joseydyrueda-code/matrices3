def suma_matrices(A, B):
  filas = len(A)
  columnas = len(A[0])
  if filas != len(B) or columnas != len(B[0]):
    return "Error, las matrices no tienen las mismas dimensiones."
  else:
    resultado = []
    for i in range(filas):
      fila = []
      for j in range(columnas):
        fila.append(A[i][j] + B[i][j])
      resultado.append(fila)
    return resultado

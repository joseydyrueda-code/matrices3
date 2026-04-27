def producto_kronecker(A, B):
       filas_A = len(A)
       columnas_A = len(A[0])
       filas_B = len(B)
       columnas_B = len(B[0])
       resultado = []
       for i in range(filas_A):
            for k in range(filas_B):
                  fila = []
                  for j in range(columnas_A):
                        for l in range(columnas_B):
                              fila.append(A[i][j] * B[k][l])
                  resultado.append(fila)
            return resultado

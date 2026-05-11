from proyecto_matrices.entrada import ingresar_matriz, mostrar_matriz
from proyecto_matrices.menu import pedir_opcion
from proyecto_matrices.operacion_matrices import (
    suma_matrices,
    multiplicar_matrices,
    producto_hadamard,
    producto_kronecker
)

def ejecutar_programa():
    while True:
        opcion = pedir_opcion()

        if opcion == 5:
            print("¡Hasta luego!")
            break

        print("\nIngrese los datos de la Matriz A:")
        A = ingresar_matriz()

        print("\nIngrese los datos de la Matriz B:")
        B = ingresar_matriz()

        if opcion == 1:
            resultado = suma_matrices(A, B)
            print("\nResultado de la suma:")
            mostrar_matriz(resultado)

        elif opcion == 2:
            resultado = multiplicar_matrices(A, B)
            print("\nResultado de la multiplicación:")
            mostrar_matriz(resultado)

        elif opcion == 3:
            resultado = producto_hadamard(A, B)
            print("\nResultado del producto de Hadamard:")
            mostrar_matriz(resultado)

        elif opcion == 4:
            resultado = producto_kronecker(A, B)
            print("\nResultado del producto de Kronecker:")
            mostrar_matriz(resultado)

        input("\nPresione Enter para continuar...")


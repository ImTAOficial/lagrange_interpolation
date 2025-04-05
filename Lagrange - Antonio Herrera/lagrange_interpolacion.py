# requisitos tener instalado pthon 3.8 o superior
# y tener instaladas las librerias: sympy matplotlib numpy
# de no tenerlas aca les dejo los comandos para su instalacion global: 
# pip install sympy matplotlib numpy

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, expand, latex, lambdify, Rational, fraction, cancel

def lagrange_interpolation():
    # Solicitar datos
    n = int(input("Ingresa el número de puntos (n): "))
    i = n - 1  
    
    # Inicialice listas para almacenar los puntos
    xi = []
    fxi = []
    
    print("\nIngrese los puntos (xi, f(xi)):")
    for j in range(n):
        x_val = input(f"x{j} = ")
        fx_val = input(f"f(x{j}) = ")
        
        # Para Convertir a fracción si es posible
        try:
            xi.append(Rational(x_val))
        except:
            xi.append(float(x_val))
        
        try:
            fxi.append(Rational(fx_val))
        except:
            fxi.append(float(fx_val))
    
    # Mostrar los puntos ingresados
    print("\nPuntos brindados:")
    for j in range(n):
        print(f"(x{j}, y{j}) = ({xi[j]}, {fxi[j]})")
    
    # Calcular los coeficientes de Lagrange
    x = symbols('x')
    polinomio = 0
    
    print("\nCálculo de los polinomios base de Lagrange L_i(x):")
    for k in range(n):
        # Calcular el polinomio base L_k(x)
        Lk = 1
        print(f"\nCalculo de L_{k}(x):")
        
        for j in range(n):
            if j != k:
                term = cancel((x - xi[j]) / (xi[k] - xi[j]))
                print(f"  (x - x{j})/(x{k} - x{j}) = (x - {xi[j]})/({xi[k]} - {xi[j]}) = {term}")
                Lk = cancel(Lk * term)
        
        print(f"\nL_{k}(x) = {Lk}")
        
        # Agregar al polinomio final
        termino = cancel(fxi[k] * Lk)
        print(f"\nTérmino {k}: y{k}*L_{k}(x) = {fxi[k]} * {Lk} = {termino}")
        polinomio = cancel(polinomio + termino)
    
    # Simplificar el polinomio
    polinomio_simplificado = expand(polinomio)
    
    # Mostrar resultados
    print("\n\nRESULTADO FINAL:")
    print("Polinomio de Lagrange (forma desarrollada):")
    print(polinomio)
    print("\nPolinomio de Lagrange simplificado:")
    print(polinomio_simplificado)
    
    # Convertir a función numérica para graficar
    polinomio_numerico = lambdify(x, polinomio_simplificado, 'numpy')
    
    # Graficar
    graficar_polinomio(xi, fxi, polinomio_numerico, polinomio_simplificado)

def graficar_polinomio(xi, fxi, polinomio_func, polinomio_expr):
    # Convertir xi a floats para graficar
    xi_float = [float(x) for x in xi]
    fxi_float = [float(y) for y in fxi]
    
    # Determinar rango de x para la gráfica
    x_min = min(xi_float) - 1
    x_max = max(xi_float) + 1
    x_vals = np.linspace(x_min, x_max, 400)
    y_vals = polinomio_func(x_vals)
    
    # Crear figura
    plt.figure(figsize=(10, 6))
    
    # Graficar polinomio
    plt.plot(x_vals, y_vals, label=f'P(x) = ${latex(polinomio_expr)}$', color='blue')
    
    # Graficar puntos de interpolación
    plt.scatter(xi_float, fxi_float, color='red', zorder=5, label='Puntos dados')
    
    # Ajustar ejes automáticamente
    y_min = min(min(y_vals), min(fxi_float)) - 0.5
    y_max = max(max(y_vals), max(fxi_float)) + 0.5
    plt.ylim(y_min, y_max)
    
    # Añadir elementos de la gráfica
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.title('Interpolación de Lagrange')
    plt.legend()
    
    # Mostrar gráfica
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("Antonio Herrera")
    print("SOLUCIONADOR DE POLINOMIO DE LAGRANGE")
    print("--------------------------------------------------------------")
    lagrange_interpolation()
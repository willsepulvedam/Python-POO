import sympy as sp

def calculator():
    print("Calculadora Matemática")
    print("Ingrese una expresión matemática:")
    expression = input()
    
    try:
        # Parseamos la expresión matemática
        expr = sp.sympify(expression)
        
        # Resolvemos la expresión
        result = sp.solve(expr)
        
        # Mostramos la solución
        print("Solución:", result)
        
        # Mostramos el procedimiento paso a paso
        steps = sp.solve(expr, dict=True)
        print("\nProcedimiento:")
        for step in steps:
            for variable, value in step.items():
                print(f"{variable} = {value}")
            
    except Exception as e:
        print("Error al resolver la expresión:", e)

if __name__ == "__main__":
    calculator()

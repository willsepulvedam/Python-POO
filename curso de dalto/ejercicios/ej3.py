class Calculadora:
    def __init__(self):
        self.valor1 = int(input("Ingrese el primer valor: "))
        self.valor2 = int(input("Ingrese el segundo valor: "))
       
    def suma(self):
        return (self.valor1 + self.valor2)
    
    def resta(self):
        return (self.valor1 - self.valor2)
    
    def multiplicacion(self):
        return (self.valor1 * self.valor2)
    
    def division(self):
        return (self.valor1 / self.valor2)
    
calcular = Calculadora()

calcular.suma()   

        
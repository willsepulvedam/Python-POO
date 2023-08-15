
#en LSP si yo tengo un clase padre, todas las clases que hereden esa clase deben poder
#hacer todo lo que esa clase padre haga.
class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return "estoy volando..."
    
class AveNoVoladora(Ave):
    pass

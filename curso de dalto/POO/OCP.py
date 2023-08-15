#creamos una clase padre la cual nos brinde los atributos usuario y mensaje
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    
    #aqui creamos la funcion notificar en la clase padre para que el usuario sepa
    #que si no crea la clase noticifar o le saltara un error de que no se imnplemento
    def notificar(self):
        raise NotImplementedError
    
#creamos las clases hijas llamando a la clase padre para poder notificar algo en especifico
#aqui en email   
class NotificarEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por Mail a {self.usuario.email}")
  
#aqui en SMS
class NotificarSMS(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por SMS a {self.usuario.sms}")

#aqui en WhatsApp
class NotificarWhatsApp(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por WhatsApp a {self.usuario.whatsapp}")
    
#aqui en Twitter
class NotificarTwitter(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por Twitter a {self.usuario.twitter}")
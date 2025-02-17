from controlador.menu import *
from configuracion.app import *
if __name__=="__main__":
    app=App('./proyecto/datux.db')
    menu(app)
    pass
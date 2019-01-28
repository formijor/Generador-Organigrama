


class Objeto(object):
    def __init__(self, id_objeto, nombre):
        self.id_objeto = id_objeto
        self.nombre = nombre
        self.puertos = {}
        self.coordenadas_puertos = {}
        self.conexiones_puertos = {}
        self.conexiones_puertos_init()
        
    def get_id_objeto(self):
        return self.id_objeto
        
    def conexiones_puertos_init(self):
        self.conexiones_puertos = {'arriba': []}#, 'abajo': [], 'izquierda': [], 'derecha': []}
        
    def set_conexion_puerto(self, puerto, objeto_id):
        self.conexiones_puertos.get(puerto).append(objeto_id)
        
    def delete_conexion_puerto(self, puerto, objeto_id):
        self.conexiones_puertos.get(puerto).remove(objeto_id)
    
    def get_conexiones_puertos(self):
        return self.conexiones_puertos
            
    def get_puertos(self):
        return self.puertos #{'arriba' : self.__arriba, 'abajo': self.__abajo,
                #'izquierda': self.__izquierda, 'derecha': self.__derecha}
        
    def get_coordenadas_puerto(self, puerto):
        self.get_coordenadas_puertos(True)
        return self.coordenadas_puertos.get(puerto)
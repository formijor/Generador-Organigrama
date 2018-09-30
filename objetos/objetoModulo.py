


class Objeto(object):
    def __init__(self, id_objeto, nombre):
        self.id_objeto = id_objeto
        self.nombre = nombre
        self.puertos = {}
        self.__crear_puertos()
        self.coordenadas_puertos = {}
        self.conexiones_puertos = {}
        self.conexiones_puertos_init()
        
    def get_id_objeto(self):
        return self.id_objeto
    
    def __crear_puertos(self):
        size = self.GetSize()
        self.__arriba = size[0] / 2
        self.__abajo = size[0] / 2
        self.__izquierda = size[1] / 2
        self.__derecha = size[1] / 2
        self.puertos = {'arriba': self.__arriba, 'abajo': self.__abajo, 
                        'izquierda': self.__izquierda, 'derecha': self.__derecha}
        self.get_coordenadas_puertos(True)
    
    def conexiones_puertos_init(self):
        self.conexiones_puertos = {'arriba': []}#, 'abajo': [], 'izquierda': [], 'derecha': []}
        
    def set_conexion_puerto(self, puerto, objeto_id):
        self.conexiones_puertos.get(puerto).append(objeto_id)
        
    def delete_conexion_puerto(self, puerto, objeto_id):
        self.conexiones_puertos.get(puerto).remove(objeto_id)
    
    def get_conexiones_puertos(self):
        return self.conexiones_puertos
    
    def get_coordenadas_puertos(self, relativo):       
        puertos = self.get_puertos()        
        pos = self.GetPosition()
        arriba = (pos[0] + puertos.get('arriba'), pos[1])
        abajo = (pos[0] + puertos.get('abajo'), pos[1] + self.GetSize()[1])
        izquierda = (pos[0], pos[1] + puertos.get('izquierda'))
        derecha = (pos[0]) + self.GetSize()[0], pos[1] + puertos.get('derecha')
        self.coordenadas_puertos = {'arriba' : arriba, 'abajo': abajo,
                                    'izquierda': izquierda, 'derecha': derecha}
        if relativo:
            return self.coordenadas_puertos
        elif not relativo:
            return puertos
        
    def get_puertos(self):
        return self.puertos #{'arriba' : self.__arriba, 'abajo': self.__abajo,
                #'izquierda': self.__izquierda, 'derecha': self.__derecha}
        
    def get_coordenadas_puerto(self, puerto):
        self.get_coordenadas_puertos(True)
        return self.coordenadas_puertos.get(puerto)
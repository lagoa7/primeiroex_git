from pygame import init


class Gato():
    def __init__(self,nome):
        self.nome = nome
        
    def fala_algo(self):
        return f"OI! Meu nome eh {self.nome}"
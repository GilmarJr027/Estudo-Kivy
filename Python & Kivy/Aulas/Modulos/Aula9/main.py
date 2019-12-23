import mod_a 
import importlib

del (mod_a.b)

mod_a.a = 0

#Faz o recarregamento do modulo com todas propriedades restauradas
importlib.reload(mod_a)

from pprint import pprint

pprint(mod_a.__dict__)

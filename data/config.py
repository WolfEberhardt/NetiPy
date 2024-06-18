
from . import langs 

got = langs.get_lang()

lang = got if got in ["de_DE","en_US"] else "de_DE"
# Local Imports
from logs.loger import Loger

import data.langs as langs
import data.config as config
import data.results as result

class Interface:
    activ = result.activ_interface()

print(Interface.activ)
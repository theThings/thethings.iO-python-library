from thethings import ThethingsAPI
from random import randrange

thethings = ThethingsAPI("yourThingToken")
thethings.addVar("hello", randrange(0, 9))
thethings.write()


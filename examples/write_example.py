from thethingsAPI import ThethingsAPI

thethings = ThethingsAPI("yourThingToken")
thethings.addVar("hello", 1);
thethings.write()


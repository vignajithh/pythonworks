#overrideing

class car:
    def start(self):
        print("key start")

    def brake(self):
        print("drum brake")

    def tramission(self):
        print("mannuel")

class ambasdoor(car):
    pass

class maruthi(car):
    def brake(self):
        print("disc brake")

    def tramission(self):
        print("no jear box")



obj=ambasdoor()
obj.start()

mobj=maruthi()
mobj.brake()
mobj.tramission()
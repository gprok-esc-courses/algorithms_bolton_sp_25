
class Airplane:
    def __init__(self, id, type):
        self.id = id
        self.type = type
        self.state = "Landed"
        self.emergency = False 

    def take_off(self):
        self.state = "Flying"

    def land(self):
        self.state = "Landed"

    def set_emergency(self, value):
        self.emergency = value 

    def __str__(self):
        return self.id + " " + self.type


a = Airplane("ZY890", "Airbus 300")
a.set_emergency(True)
a.take_off()

print(a)
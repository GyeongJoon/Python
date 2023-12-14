class Unit:
    def __init__(self):
        print("Unit 생성자")
    
class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable,Unit):
    def __init__(self):
        # super().__init__()
        Flyable.__init__(self)

class FlyableUnit(Unit,Flyable):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)

# 드랍쉽
dropship = FlyableUnit()
        
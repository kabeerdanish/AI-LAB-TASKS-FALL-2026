class UAV:
    def __init__(self,id,model):
        self.id=id
        self.model =model
        self._battery_level=100 

    def set_battery_level(self,level):
        if level>=0 and level<=100:
            self._battery_level =level
        else:
            print("invalid batt level")

    def get_battery_level(self):
        return self._battery_level

    def display_info(self):
        print("id:",self.id,"model:",self.model,"batt:",self._battery_level)

u1 =UAV(1,"droneX")
u2=UAV(2,"quadC")

u1.display_info()
u1.set_battery_level(45)
print("new batt is",u1.get_battery_level())

u2.set_battery_level(150)
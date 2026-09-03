class Threat:
    def __init__(self,threat_id,name,severity):
        self.thrt_id=threat_id
        self.name=name
        self.severity= severity

class CropDiseaseThreat(Threat):
    def detect_disease(self):
        print("detecting disese in",self.name) # disese

class PestThreat(Threat):
    def detect_pests(self):
        print("checking pests for",self.name)

class WaterStressThreat(Threat):
    def check_soil_moisture(self):
        print("moisture chk for",self.name)

t1=CropDiseaseThreat(101,"wheat","high")
t2=PestThreat(102,"corn","low")
t3=WaterStressThreat(103,"rice","medium")

t1.detect_disease()
t2.detect_pests()
t3.check_soil_moisture()
class HealthcareAgent:
    def __init__(self,agent_id,patient_name,status):
        self.agent_id=agent_id
        self.patinet_name=patient_name
        self.status =status

class HeartMonitoringAgent(HealthcareAgent):
    def monitor_heart_rate(self):
        print("monitoring heart rat for",self.patinet_name)

class MedicineReminderAgent(HealthcareAgent):
    def remind_medicine(self):
        print(self.patinet_name,"take ur meds")

class HealthPredictionAgent(HealthcareAgent):
    def predict_health_risk(self):
        print("analyzing data for risk of",self.patinet_name)

a1=HeartMonitoringAgent(1,"ali","stable")
a2=MedicineReminderAgent(2,"ahmed","recovering")
a3=HealthPredictionAgent(3,"sara","critical")

a1.monitor_heart_rate()
a2.remind_medicine()
a3.predict_health_risk()
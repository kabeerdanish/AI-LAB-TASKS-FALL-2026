class ResponseAgent:
    def execute_response(self):
        pass

class AlertAgent(ResponseAgent):
    def execute_response(self):
        print("seding alert notifs")

class BlockAgent(ResponseAgent):
    def execute_response(self):
        print("blocking malicious activty") 

class RecoverAgent(ResponseAgent):
    def execute_response(self):
        print("restoring the sys")

agnts=[AlertAgent(),BlockAgent(),RecoverAgent()]
for ag in agnts:
    ag.execute_response()
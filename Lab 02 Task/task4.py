class Employee:
    def work(self):
        pass

class Manager(Employee):
    def work(self):
        print("manger is managing")

class Developer(Employee):
    def work(self):
        print("dev writing code")

class Designer(Employee):
    def work(self):
        print("designer making ui")

emps= [Manager(),Developer(),Designer()]
for e in emps:
    e.work()
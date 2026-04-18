class Laptop: 
    def Build(self):
        print("Building Laptop")

class Alien:
    def code(self, machine:Laptop):
        print("Coding Alien")
        machine.Build()

class Desktop:
    def Build(self):
        print("Desktop building")
class Tablet:
    def open_def(self):
        print("opening Pdf")
navin=Alien()
# navin.code(Laptop())
navin.code(Desktop())
navin.code(Tablet())

from papirus import PapirusComposite

class PiDisplay:

    def initialize_display(self):
        self.display.WriteAll()


    def update(self):
        self.display = PapirusComposite(False)
        self.initialize_display()
        self.display.AddText("testing")

PI = PiDisplay()

while True:
    PI.update()
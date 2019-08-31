import os

from papirus import PapirusComposite

class PiDisplay:

    def update(self):
        self.display = PapirusComposite(False)
        self.display.AddText("testing", 0, 0, size=12, Id="lineOne")
        self.display.WriteAll()

PI = PiDisplay()


PI.update()
# while True:
#     PI.update()
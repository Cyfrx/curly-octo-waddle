import os

from papirus import PapirusComposite

DIRECTORY = os.path.dirname(os.path.realpath(__file__))

class PiDisplay:

    def update(self):
        self.display = PapirusComposite(False)
        self.display.AddText("testing", 0, 0, size=12, Id="lineOne")
        self.display.WriteAll()
        # self.display.AddImg(os.path.join(DIRECTORY, 'test', 'images', self.placeholder),0,0, (100,100), Id = "prototype")
        self.display.AddImg(self.placeholder, 1, 63, (32, 32), Id="ForecastIconOne")

PI = PiDisplay()


PI.update()
# while True:
#     PI.update()
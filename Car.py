class Car(object):
    def __init__ (self,speedLimit,company,color,model):
        self.speedLimit = speedLimit
        self.company = company
        self.color = color
        self.model = model

    def start(self):
        print('Started')

    def stop(self):
        print('Stopped')

    def accelarate(self):
        print("Accelarating")        

    def gearChanged(self):
        print('Gear changed')


Laferrari = Car(200,'Ferrari','red','Laferrari')

print(Laferrari.speedLimit)

Laferrari.start()

Laferrari.accelarate()

Laferrari.gearChanged()

Laferrari.stop()
class car:
    count=0
    speed=0

    def speedChange(self,v):
        car.count+=1
        self.speed=v
bmw=car()
benz=car()
bmw.speedChange(100)
print('BMW speed : ',bmw.speed)
print('Number of speedChange : ',car.count)

benz.speedChange(120)
print('Benz speed : ',benz.speed)
print('Number of speedChange : ',car.count)
class Car:
    model='BMW'
    color='white'
    def speedChange(self,v):
        print('speedChange', v)
bmw=Car()
benz=Car()

bmw.speedChange(20)
benz.model='Benz'
benz.color='black'

print(bmw.model)
print(bmw.color)
print(benz.model)
print(benz.color)
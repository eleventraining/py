
class computer :

    def __init__(self,cpu='',ram=''):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print('config is ',self.cpu,self.ram)


com1=computer('i3','4')
com2=computer('r3','6')
print(type(com1))
#print('config : ',end='')

#one way to call method
#computer.config(com1)
#computer.config(com2)

#second way to call method
com1.config()
com2.config()
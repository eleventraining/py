
class computer1 :

    def __init__(self,cpu):
        self.cpu = cpu

    def config(self):
        print('config is ',self.cpu)


com1=computer1()

#print(type(com1))
#print('config : ',end='')

#second way to call method
com1.config('i3')

class Vehicle:
    def __init__(self, number='12345', admin='Xiaoming'):
        self.number=number
        self.admin=admin
    def load(self,origin, destination):
        print(origin)
        
class Track(Vehicle):
    def load(self, weight, origin, destination):
        print('载货重量：%s，出发地：%s，目标地：%s'%(weight,origin,destination))
class Bus(Vehicle):
    def load(self, linenum, origin, destination):
        print('线路：%s，出发地：%s，目标地：%s'%(linenum,origin,destination))
if __name__=='__main__':
    track=Track()
    bus=Bus()
    track.load(50,'北京','上海')
    bus.load(84,'新宫','西红门')

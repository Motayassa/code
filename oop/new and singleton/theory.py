class Point:
    def __new__(cls, *args, **kwargs):
        print("вызов __new__ для " + str(cls))
 
    def __init__(self, x=0, y=0):
        print("вызов __init__ для " + str(self))
        self.x = x
        self.y = y
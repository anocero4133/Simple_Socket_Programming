class Assign7Data(object):
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def AddVars(self):
        a = self.x
        b = self.y
        c = a + b
        return c
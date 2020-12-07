class FourPoint(object):
    def __init__(self, flag, dic, slow, shigh, blow, bhigh, index, count):
        self.flag = flag
        self.dic = dic
        self.slow = slow
        self.shigh = shigh
        self.blow = blow
        self.bhigh = bhigh
        self.count  = count
        self.index = index

    def setCurrentFalse(self):
        self.flag = False
        self.dic[self.index] = -2
        return self
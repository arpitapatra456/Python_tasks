class box:
    def __init__(self):
        self.a = 10
        print('welcome')
    def __del__(self):
        print('goodbye')
        del(self.a)

obj = box()
del obj
exit()

class base():
    def __init__(self):
        print("In the base class")
        self.s1 = "base class vara"

class derived(base):
    def __init__(self):
        super().__init__()
        print("In the derived class")
        self.s2= "derived class var"
        # super().__init__()


a=derived()
print(a.s1)
print(a.s2)
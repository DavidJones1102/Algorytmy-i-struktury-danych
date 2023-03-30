class Employee:
    def __init__(self, fun):
        self.fun = fun
        self.emp = []
        self.f = -1
        self.g = -1
    def __str__(self):
        return f'{self.fun}'
    
    #show fun of employees
    def show(self):
        for u in self.emp:
            print(u, end=" ")

#Best party rooted in v
def f(v):
    if v.f != -1: return v.f

    f1 = v.fun
    f2 = g(v)
    for u in v.emp:
        f1+=g(u)
    v.f = max(f1,f2)
    return v.f

#Party when v isn't going 
def g(v):
    if v.g != -1: return v.g

    v.g = 0
    for u in v.emp:
        v.g+=f(u)
    return v.g

e1=Employee(10)

e2=Employee(8)
e3=Employee(5)
e4=Employee(3)

e5=Employee(400)
e6=Employee(0)
e7=Employee(10)

e8=Employee(400)

e1.emp = [e2,e3,e4]
e2.emp = [e5,e6,e7]
e6.emp = [e8]

best = f(e1)
print(best)
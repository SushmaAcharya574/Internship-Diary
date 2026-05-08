class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):   # Multiple Inheritance
    pass

# Driver Code
d = D()
d.show()

# Print MRO
print(D.mro())

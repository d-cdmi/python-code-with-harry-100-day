# day 81 main File
# Hybrid Inheritance
class BaseClass:
    pass
class Derived1 (BaseClass):
    pass
class Derived2 (BaseClass):
    pass
class Derived2 (Derived1,Derived2):
    pass
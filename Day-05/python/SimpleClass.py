from pyuvm import *

class SimpleClass(UVMObject):                          # UVMObject is equalent to uvm_object
    def __init__(self, value=0, name="SimpleClass"):   # __init__ is equalent to new
        super().__init__(name)               # super.new(name)
        self.value = value                   # this.value = value

# attrgettersetter

Python provides a great operator.attrgetter method, but it doesn't support default values and there's no similar attrsetter method.

This module provides those two convenience functions

# Example

    class A(object):
        def __init__(self):
            self.b = B()
            self.name = "A"

    class B(object):
        def __init__(self):
            self.name = "B"

    class C(object):
        pass


    # getter 
    name = attrgetter("name")
    remote_name = attrgetter("b.name")
    a = A()
    b = B()
    c = C()

    self.assertEquals(name(a), "A")
    self.assertEquals(name(b), "B")
    self.assertEquals(remote_name(a), "B")
    self.assertEquals(name(c), None)

    # setter
    name = attrsetter("name")
    remote_name = attrsetter("b.name")


    a = A()
    a.b = B()

    name(a, "A-1")
    remote_name(a, "B-1")
    self.assertEquals(a.name, "A-1")
    self.assertEquals(a.b.name, "B-1")


# License

MIT

# Contact

@bradjasper

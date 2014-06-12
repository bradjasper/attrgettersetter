from attrgettersetter import attrgetter, attrsetter

import unittest

class A(object):
    def __init__(self):
        self.b = B()
        self.name = "A"

class B(object):
    def __init__(self):
        self.name = "B"

class C(object):
    pass

class OperatorTests(unittest.TestCase):
    """Test various custom operators"""

    def test_attrgetter(self):

        name = attrgetter("name")
        remote_name = attrgetter("b.name")
        a = A()
        b = B()
        c = C()

        self.assertEquals(name(a), "A")
        self.assertEquals(name(b), "B")
        self.assertEquals(remote_name(a), "B")
        self.assertEquals(name(c), None)

    def test_attrsetter(self):

        name = attrsetter("name")
        remote_name = attrsetter("b.name")


        a = A()
        a.b = B()

        name(a, "A-1")
        remote_name(a, "B-1")
        self.assertEquals(a.name, "A-1")
        self.assertEquals(a.b.name, "B-1")


if __name__ == "__main__":
    unittest.main()

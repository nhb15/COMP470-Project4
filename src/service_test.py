import service

def test_plus():
    assert(service.plus(2, 2) == 4)

def test_minus():
    assert(service.minus(2, 2) == 0)

def test_multiply():
    assert(service.multiply(2, 2) == 4)

def test_divide():
    assert(service.divide(2, 2) == 1)
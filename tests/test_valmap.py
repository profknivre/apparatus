from apparatus import valmap


def test_valmap():
    assert valmap(5,0,10,10,0) == 5
    assert valmap(0, 0, 10, 10, 0) == 10
    assert valmap(10, 0, 10, 10, 0) == 0
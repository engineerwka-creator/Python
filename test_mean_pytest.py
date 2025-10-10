import pytest
import means


def test_mean_arthmetic():
    sum4 = means.mean_arthmetic2([1, 2, 3, ])
    assert sum4 == 2

def test_mean_geometric():
    sum4 = means.mean_geometric([1, 2, 3, ])
    assert sum4 == 1.8171205928321397
    
import unittest
import means

class TestMeans(unittest.TestCase):
    def test_arthmetic_means(self):
        sum4 = means.mean_arthmetic2([1, 2, 3, ])
        self.assertEqual(sum4, 2)
    def test_mean_geometric(self):
        sum4 = means.mean_geometric([1, 2, 3, ])
        self.assertEqual(sum4, 1.8171205928321397)

if __name__ == '__main__':
    unittest.main()






















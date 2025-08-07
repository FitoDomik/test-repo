import unittest
from src.feature_323 import calculate_feature_323, validate_feature_323
class TestFeature323(unittest.TestCase):
    def test_calculation(self):
        data = [1, 2, 3, 4, 5]
        result = calculate_feature_323(data)
        self.assertEqual(result, [2, 4, 6, 8, 10])
    def test_validation(self):
        valid_data = [1, 2, 3]
        invalid_data = [1, '2', 3]
        self.assertTrue(validate_feature_323(valid_data))
        self.assertFalse(validate_feature_323(invalid_data))
if __name__ == '__main__':
    unittest.main()
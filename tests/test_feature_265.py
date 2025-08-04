import unittest
from src.feature_265 import calculate_feature_265, validate_feature_265
class TestFeature265(unittest.TestCase):
    def test_calculation(self):
        data = [1, 2, 3, 4, 5]
        result = calculate_feature_265(data)
        self.assertEqual(result, [2, 4, 6, 8, 10])
    def test_validation(self):
        valid_data = [1, 2, 3]
        invalid_data = [1, '2', 3]
        self.assertTrue(validate_feature_265(valid_data))
        self.assertFalse(validate_feature_265(invalid_data))
if __name__ == '__main__':
    unittest.main()
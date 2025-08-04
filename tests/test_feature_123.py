import unittest
from src.feature_123 import calculate_feature_123, validate_feature_123
class TestFeature123(unittest.TestCase):
    def test_calculation(self):
        data = [1, 2, 3, 4, 5]
        result = calculate_feature_123(data)
        self.assertEqual(result, [2, 4, 6, 8, 10])
    def test_validation(self):
        valid_data = [1, 2, 3]
        invalid_data = [1, '2', 3]
        self.assertTrue(validate_feature_123(valid_data))
        self.assertFalse(validate_feature_123(invalid_data))
if __name__ == '__main__':
    unittest.main()
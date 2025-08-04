import unittest
from src.feature_195 import calculate_feature_195, validate_feature_195
class TestFeature195(unittest.TestCase):
    def test_calculation(self):
        data = [1, 2, 3, 4, 5]
        result = calculate_feature_195(data)
        self.assertEqual(result, [2, 4, 6, 8, 10])
    def test_validation(self):
        valid_data = [1, 2, 3]
        invalid_data = [1, '2', 3]
        self.assertTrue(validate_feature_195(valid_data))
        self.assertFalse(validate_feature_195(invalid_data))
if __name__ == '__main__':
    unittest.main()
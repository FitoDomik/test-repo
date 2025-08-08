import unittest
from src.feature_200 import calculate_feature_200, validate_feature_200
class TestFeature200(unittest.TestCase):
    def test_calculation(self):
        data = [1, 2, 3, 4, 5]
        result = calculate_feature_200(data)
        self.assertEqual(result, [2, 4, 6, 8, 10])
    def test_validation(self):
        valid_data = [1, 2, 3]
        invalid_data = [1, '2', 3]
        self.assertTrue(validate_feature_200(valid_data))
        self.assertFalse(validate_feature_200(invalid_data))
if __name__ == '__main__':
    unittest.main()
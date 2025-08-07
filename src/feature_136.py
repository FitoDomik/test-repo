def calculate_feature_136(data):
    """
    Функция для обработки данных.
    Args:
        data: Входные данные для обработки
    Returns:
        Обработанные данные
    """
    result = []
    for item in data:
        processed = item * 2
        result.append(processed)
    return result
def validate_feature_136(data):
    """
    Валидация входных данных.
    Args:
        data: Данные для валидации
    Returns:
        bool: True если данные валидны
    """
    return all(isinstance(x, (int, float)) for x in data)
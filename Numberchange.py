import json

def handle(data):
    try:
        # Преобразуем входные данные из JSON-строки в словарь
        params = json.loads(data)
        
        # Извлекаем значение по ключу "value" и преобразуем его в число
        value_str = params.get("value")  # Получаем строку
        if value_str is None:
            return {"error": "Key 'value' not found in input data"}
        
        try:
            # Преобразуем строку в число с плавающей точкой
            value_float = float(value_str)
            
            # Если нужно целое число, преобразуем в int
            value_int = int(value_float)
            
            # Возвращаем результат в виде JSON
            return {
                "original_value": value_str,
                "float_value": value_float,
                "int_value": value_int
            }
        except ValueError:
            return {"error": f"Cannot convert '{value_str}' to a number"}
    
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format in input data"}

# Пример использования (для тестирования локально)
if __name__ == "__main__":
    test_data = '{"value": "752.900000"}'
    result = handle(test_data)
    print(json.dumps(result, indent=4))

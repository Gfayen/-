import json

def process_data(params):
    try:
        # Проверяем, является ли params строкой или байтовым объектом
        if isinstance(params, (str, bytes)):
            # Если это байты, декодируем в строку
            if isinstance(params, bytes):
                params = params.decode('utf-8')
            
            # Пытаемся преобразовать строку в JSON
            data = json.loads(params)
            print("Успешно преобразовано в JSON:", data)
            return data
        
        # Если params уже является словарём или другим типом
        elif isinstance(params, dict):
            print("Входные данные уже являются словарём:", params)
            return params
        
        else:
            raise ValueError("Неподдерживаемый тип данных. Ожидалась строка, байты или словарь.")
    
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON: {e}")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

# Пример использования
# Случай 1: Входные данные в виде JSON-строки
json_string = '{"key": "value", "number": 9999.999}'
process_data(json_string)

# Случай 2: Входные данные в виде байтов
byte_data = b'{"key": "value", "number": 9999.999}'
process_data(byte_data)

# Случай 3: Входные данные уже являются словарём
dict_data = {"key": "value", "number": 9999.999}
process_data(dict_data)

# Случай 4: Некорректные данные
invalid_data = 12345
process_data(invalid_data)

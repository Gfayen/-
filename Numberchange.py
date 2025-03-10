def convert_to_number(data):
    try:
        # Преобразуем строку в число с плавающей точкой
        number = float(data)
        print(f"Преобразованное значение: {number} (тип: {type(number)})")
        return number
    except ValueError:
        print(f"Ошибка: Значение '{data}' не может быть преобразовано в число.")
        return None

# Пример использования
input_data = "9999.999"
result = convert_to_number(input_data)

# Если нужно преобразовать в целое число (отбросив дробную часть)
if result is not None:
    integer_result = int(result)
    print(f"Целочисленное значение: {integer_result} (тип: {type(integer_result)})")

def input_data():
    """Функция для ввода массива и числа."""
    array = input("Введите элементы массива, разделенные пробелом: ")
    number = int(input("Введите число для проверки: "))
    
    # Преобразуем строку в массив целых чисел
    array = list(map(int, array.split()))
    return array, number

def find_subarrays(array):
    """Функция для нахождения всех подмассивов."""
    subarrays = []
    n = len(array)
    
    # Генерация подмассивов
    for i in range(n):
        for j in range(i, n):
            subarrays.append(array[i:j+1])    
    return subarrays

def count_subarrays_with_sum(subarrays, target_sum):
    """Функция для подсчета подмассивов, сумма которых равна заданному числу."""
    count = 0
    
    for subarray in subarrays:
        if sum(subarray) == target_sum:
            count += 1
    return count

def main_menu():
    """Главное меню приложения."""
    while True:
        print("\nМеню:")
        print("1) Ввод массива и числа")
        print("2) Обработка значений")
        print("3) Вывод результата")
        print("0) Завершение работы")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            array, target_sum = input_data() 
        
        elif choice == '2':
            if  'array' not in locals() and 'number' not in locals():
                print("Ошибка: Необходимо сначала ввести значения.")
                continue
                
            subarrays = find_subarrays(array)  # Находим все подмассивы
            result = count_subarrays_with_sum(subarrays, target_sum)  # Считаем подмассивы с нужной суммой
        
        elif choice == '3':
            if  'array' not in locals() and 'number' not in locals():
                print("Ошибка: Необходимо сначала ввести значения.")
                continue
                
                print(f"Количество подмассивов, сумма которых равна {target_sum}: {result}")
        
        elif choice == '0':
            print("Завершение работы программы.")
            break
        
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()

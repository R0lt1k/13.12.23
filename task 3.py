def access_array_element(array, index):
    try:
        element = array[index]
        print("Элемент с индексом", index, ":", element)
    except IndexError:
        print("Индекс за пределами массива.")
        
arr = [1, 2, 3, 4, 5]
access_array_element(arr, 10)
access_array_element(arr, 3)

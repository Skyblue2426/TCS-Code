def non_adjacent_values(array):
    result = []
    for i in range(0, len(array), 2): 
        result.append(array[i])
    return result
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
non_adjacent = non_adjacent_values(array)
print(f"Original array: {array}")
print(f"Non-adjacent values: {non_adjacent}")

                                                                                                                                                                                                

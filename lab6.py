def insertion_sort(arr, col):
    #using insertion_sort to sort our matrix by col
    for i in range(1, len(arr)):
        key = arr[i][col]
        j = i - 1
        while j >= 0 and arr[j][col] < key:
            arr[j + 1][col] = arr[j][col]
            j -= 1
        arr[j + 1][col] = key

def max_el_in_row(row):
    #finding max el in each row
    max_value = row[0]
    for value in row:
        if value > max_value:
            max_value = value
    return max_value

def sum_list(lst):
    #calculating sum of the biggest el of each row
    total = 0
    for number in lst:
        total += number
    return total

def main():
    #our matrix idk
    matrix = [
        [-12, 7, 23, 13, 4],
        [67, 15, 34, -5, 9],
        [2, 5, 17, -23, 45],
        [26, -6, 23, -5, -9],
        [18, 37, -8, 26, 12]
    ]
    
    max_elements = []
    for row in matrix:
        max_elements.append(max_el_in_row(row))
    
    print("max element for each row:", max_elements)
    
    for col in range(len(matrix[0])): 
        insertion_sort(matrix, col)
    
    print("matrix after sorting:")
    for row in matrix:
        print(row)
    
    total_sum = sum_list(max_elements)
    print("sum of max elements:", total_sum)

if __name__ == "__main__":
    main()
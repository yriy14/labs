class MatrixProcessor:
    def __init__(self, matrix):
        self.matrix = matrix

    def insertion_sort(func):
            def wrapper(self,*args,**kwargs):
                col = kwargs.get('col') 
                for i in range(1, len(self.matrix)):
                    key = self.matrix[i]
                    j = i - 1
                    while j >= 0 and (self.matrix[j][col] < key[col]):
                        self.matrix[j + 1] = self.matrix[j]
                        j -= 1
                    self.matrix[j + 1] = key
                return func(self, *args, **kwargs)  
            return wrapper
    
    def max_el_in_row(self, row):
        max_value = row[0]
        for value in row:
            if value > max_value:
                max_value = value
        return max_value
    
    def sum_list(self, lst):
        total = 0
        for number in lst:
            total += number
        return total

    def get_max_elements(self):
        max_elements = []
        for row in self.matrix:
            max_elements.append(self.max_el_in_row(row))
        return max_elements

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrix cant be added")
        
        result = []
        for i in range(len(self.matrix)):
            row = []  
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] - other.matrix[i][j])
            result.append(row)
        return MatrixProcessor(result)
    
    def __repr__(self):
        return '\n'.join([str(row) for row in self.matrix])
    
    @insertion_sort
    def print_sorted_matrix(self,col):
        for row in self.matrix:
            print(row)

def main():
    matrix = [
        [-12, 7, 23, 13, 4],
        [67, 15, 34, -5, 9],
        [2, 5, 17, -23, 45],
        [26, -6, 23, -5, -9],
        [18, 37, -8, 26, 12]
    ]
    
    processor = MatrixProcessor(matrix)

    max_elements = processor.get_max_elements()
    print("max element for each row:", max_elements)


    total_sum = processor.sum_list(max_elements)
    print("sum of max elements:", total_sum)

    matrix2 =[
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    
    processor2 = MatrixProcessor(matrix2)

    result_matrix = processor + processor2
    print("result of substraction two matrix:")
    print(result_matrix)

    print("sorted matrix")

    processor.print_sorted_matrix(col=0)

if __name__ == "__main__":
    main()
num = int(input("Ваша кількість слів: "))

words = [input() for _ in range(num)]

print(words)

# Функція для вибору стовпця 
def choose_column(words):
    max_spaces = -1
    chosen_col = 0
    
    for word in words:
        spaces = len(word) - len(word.lstrip())
        if spaces > max_spaces:
            max_spaces = spaces
            chosen_col = spaces  
        
    # Якщо знайдено колонки з пробілами, беремо їх
    if chosen_col < len(words[0]):
        return chosen_col
    else:
        return 

# Отримуємо стовпець
col = choose_column(words)


#if col <= 0:
#   answer = [''.join([words[row][col] for row in range(num)])]
#    print("Результат:", max(answer, key=len))
#else:
#    print("delete wrong row pls")

answer = [''.join([words[row][col] for row in range(num) if col < len(words[row])])]
print("Результат:", max(answer, key=len))
def insert(array, index, value):
    array.insert(index, value)
    return array

def remove(array, value):
    for i in range(len(array)):
        if array[i] == value:
            array.pop(i)
            break
    return array

def append(array, value):
    array.append(value)
    return array

def sort(array):
    array.sort()
    return array

def pop(array):
    array.pop()
    return array

def reverse(array):
    array.reverse()
    return array

array = []
n = int(input())

for i in range(n):
    command = input().split()
    if command[0] == 'insert':
        array = insert(array, int(command[1]), int(command[2]))
    elif command[0] == 'print':
        print(array)
    elif command[0] == 'remove':
        array = remove(array, int(command[1]))
    elif command[0] == 'append':
        array = append(array, int(command[1]))
    elif command[0] == 'sort':
        array = sort(array)
    elif command[0] == 'pop':
        array = pop(array)
    elif command[0] == 'reverse':
        array = reverse(array)
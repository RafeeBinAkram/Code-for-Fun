if __name__ == '__main__':
    N = int(input("Enter value of N: "))
    lst = []
    for _ in range(N):
        op, *value = input("Enter operation and values: ").split()
        value = list(map(int, value))
        if op == "append":
            lst.append(value[0])
        if op == "sort":
            lst.sort()
        if op == "print":
            print(lst)
        if op == "remove":
            lst.remove(value)
        if op == "insert":
            lst.insert(value[0], value[1])
        if op == "reverse":
            lst.sort(reverse=True)
        if op == "pop":
            length = len(lst)
            lst.pop(length-1)
            
        
        
    
        
        
    

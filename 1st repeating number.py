list_1 = [1,2,3,2,3,4,1,5,6,2,2,4,2]
n = len(list_1)
found = False
for i in range(n):
    for j in range(i+1, n):
        if list_1[i] ==list_1[j]:
            print(f"1st repeating number is {list_1[i]}")
            found= True
            break
    if found:
        break
            

     



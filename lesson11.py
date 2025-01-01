
if __name__ == "__main__":
    is_end = False
    arr1=[1,3,4,6,8,9,23,44,56,77,89,90]
    arr2=[0,1,2,4,6,7,8,9,11,12,23,33,45,66,78,99]
    arr_solution = []
    ind1 = ind2 = 0
    while True:
        if arr1[ind1] == arr2[ind2]:
            arr_solution.append(arr1[ind1])
            ind1 +=1
            ind2 +=1
            if ind1==len(arr1) or ind2==len(arr2): is_end=True
        elif arr1[ind1] < arr2[ind2]:
            ind1 +=1
            if ind1==len(arr1): is_end=True
        elif arr1[ind1] > arr2[ind2]:
            ind2 +=1
            if ind2==len(arr2): is_end=True
        if is_end:
            print (arr_solution)
            exit()

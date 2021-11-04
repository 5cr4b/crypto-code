

def  is_supper_increase(lst):
    sum =  0
    for i in range(len(lst)-1):
        sum += int(lst[i])
        print(sum)
        if sum > int(lst[i+1]) :
            return 'no'
    return 'yes'
lst = [x for x in input("input like 1 2 3 4 : ").split()]
print(is_supper_increase(lst))
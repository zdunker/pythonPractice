def subset_sum(numbers, target, partial=[]):
    s = sum(partial)
    
    if s > target:
        print "over limit ", partial
        return
    # check if the partial sum is equals to target
    if s == target: 
        print "sum(%s)=%s" % (partial, target)
        return

    for i in range(len(numbers)):
        subset_sum(numbers[i+1:], target, partial + [numbers[i]]) 


if __name__ == "__main__":
    subset_sum([12,3,9,8,4,5,7,10,1,1],20)
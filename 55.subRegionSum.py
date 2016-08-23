def sumRegion(matrix, x,y):
    sum = 0
    for i in range(x+1):
        for j in range(y+1):
            sum += matrix[i][j]
    print "x=%d y=%d sum=%d"%(x,y,sum)
    return sum

matrix = [[1,2,3,4,5,6,7,8,9,0],
          [0,9,8,7,6,5,4,3,2,1],
          [2,3,4,5,6,7,8,9,0,1],
          [8,7,6,5,4,3,2,1,0,9],
          [5,6,7,8,9,0,1,2,3,4],
          [4,3,2,1,0,9,8,7,6,5]]

#sum region(abcd) = sum(od) - sum(oc) - sum(ob) + sum(oa)
def subRegion(matrix,x1,y1,x2,y2):
    return sumRegion(matrix, x2, y2) - sumRegion(matrix, x1-1, y2) - sumRegion(matrix, x2, y1-1) + sumRegion(matrix, x1-1, y1-1)

if __name__ == '__main__':
    print subRegion(matrix, 2, 2, 3, 5)
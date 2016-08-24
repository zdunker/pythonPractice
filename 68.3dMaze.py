listLevel0 = [['A', 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 1]]
listlevel1 = [[1, 1, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 1, 0],
              [1, 0, 0, 0, 0, 1, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 1]]
listlevel2 = [[1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 1, 0],
              [1, 1, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0],
              [1, 1, 1, 1, 0, 0, 0, 1]]
listlevel3 = [[1, 1, 1, 1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0]]
listlevel4 = [[0, 0, 1, 0, 0, 0, 0, 1],
              [0, 0, 1, 0, 0, 0, 0, 1],
              [0, 0, 1, 0, 0, 0, 0, 1],
              [0, 0, 1, 0, 'B', 0, 0, 1],
              [0, 0, 1, 1, 0, 0, 0, 1],
              [0, 0, 0, 1, 0, 0, 0, 1],
              [0, 0, 0, 1, 0, 0, 0, 1],
              [0, 0, 0, 1, 1, 1, 0, 0]]
mazeList = [listLevel0,listlevel1,listlevel2,listlevel3,listlevel4]
print mazeList[0][0][0]

def search(x, y, z):
    if mazeList[x][y][z] == 'B':
        print 'found at %d,%d,%d' % (x, y, z)
        return True
    elif mazeList[x][y][z] == 1:
        #print 'wall at %d,%d' % (x, y)
        return False
    elif mazeList[x][y][z] == 2:
        #print 'visited at %d,%d' % (x, y)
        return False
    
    print 'visiting %d,%d,%d' % (x, y, z)

    # mark as visited
    mazeList[x][y][z] = 2

    # explore neighbors clockwise starting by the one on the right
    if ((x < len(mazeList)-1 and search(x+1, y, z))
        or (y > 0 and search(x, y-1, z))
        or (x > 0 and search(x-1, y, z))
        or (y < len(mazeList[x])-1 and search(x, y+1, z))
        or (z < len(mazeList[x][y])-1 and search(x, y, z+1))
        or (z > 0 and search(x, y, z-1))):
        return True

    return False

search(0, 0, 0)
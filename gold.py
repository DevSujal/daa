

def maxgoldReturn(grid):
    rows = len(grid)
    col = len(grid[0])
    maxgold = 0
    for i in range(rows):
        for j in range(col):
            if(grid[i][j] > 0):
                gold = maxgoldbypath(grid, i, j, rows, col,  [[i, j]], 0)
                if(gold > maxgold):
                    maxgold = gold
                
    return maxgold

def maxgoldbypath(grid, i, j, rows, cols, visited,maxgold):
    if(i >= rows or j >= cols or i < 0 or j < 0):
        return maxgold
    prei = i
    prej = j
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if((x == i and y == j) or (x == i+1 and y == j+1) or (x == i+1 and y == j-1) or (x == i-1 and y == j+1) or (x == i-1 and y == j-1) or x < 0 or y < 0 or x == rows or y == cols or grid[x][y] == 0):
                continue
            if([x,y] not in visited):
                prei = x
                prej = y

                visited.append([prei, prej])         
                maxgold = maxgoldbypath(grid, prei, prej, rows, cols,visited,maxgold)
                visited.pop()

    if(prei == i and prej == j or [prei, prej] in visited):
        gold = 0
        for k in visited:
            gold += grid[k[0]][k[1]]
        maxgold = max(maxgold, gold)
        return maxgold
    return maxgold
                
    
for i in [[1,0,7,0,0,0],[2,0,6,0,1,0],[3,5,6,7,4,2],[4,3,1,0,2,0],[3,0,5,0,20,0]]:
    print(i)
print(maxgoldReturn([[1,0,7,0,0,0],[2,0,6,0,1,0],[3,5,6,7,4,2],[4,3,1,0,2,0],[3,0,5,0,20,0]]))
    





def maxunits(storage_capacity, profit_weight2):
    profit_weight = [i for i in profit_weight2]
    n = len(profit_weight)
    for i in range(n-1):
        post = i
        for j in range(i+1, n):
            if(profit_weight[j][1] > profit_weight[post][1]):
                post = j

        if(post != i):
           temp = profit_weight[i]
           profit_weight[i] = profit_weight[post]
           profit_weight[post] = temp

    profit = 0
    # print(profit_weight)

    for i in range(n):
        if(profit_weight[i][0]  <= storage_capacity):
            profit += profit_weight[i][1] * profit_weight[i][0]
            storage_capacity -=  profit_weight[i][0]
        else:
            profit += profit_weight[i][1] * storage_capacity
            break

    return profit


print(maxunits(13, [[2,1],[4,4],[3,1],[4,1],[2,4],[3,4],[1,3],[4,3],[5,3],[5,3]]))
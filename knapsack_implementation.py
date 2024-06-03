import numpy as np, pandas as pd
def calc_profit_by_minweight(storage_capacity, p, w, n, x):

    ans = pd.DataFrame({
        "weight_obj" : [],
        "profit_obj" : [],
        "capacity_remain" : [],
        "weight_in_bag" : [],
        "Partial_Complete" : []
    })
    st = storage_capacity
    profit = [x for x in p]
    weight = [x for x in w]
    profit_sorted = []
    weight_sorted = []
    for _ in range(n):
        min_index = weight.index(min(weight))
        profit_sorted.append(profit[min_index])
        weight_sorted.append(weight[min_index])
        profit.pop(min_index)
        weight.pop(min_index)

    
    weight_obj = [0]
    profit_obj = [0]
    capacity_remain = [storage_capacity]
    weight_in_bag = [0]
    Partial_Complete = ["-"]
    for i in range(n):
        if(storage_capacity >= weight_sorted[i]):
            x[i] = 1
            weight_in_bag.append(15 - storage_capacity + weight_sorted[i])
            storage_capacity -= weight_sorted[i]
            weight_obj.append(weight_sorted[i])
            profit_obj.append(x[i] * profit_sorted[i])
            capacity_remain.append(storage_capacity)
            Partial_Complete.append("Complete")
        else:
            x[i] = storage_capacity/weight_sorted[i]
            weight_obj.append(storage_capacity)
            profit_obj.append(x[i] * profit_sorted[i])

            if(storage_capacity != 0):
                Partial_Complete.append("Partial")
            else:
                Partial_Complete.append("-")
            storage_capacity = 0
            capacity_remain.append(storage_capacity)
            weight_in_bag.append(st)

            ans["weight_obj"] = weight_obj
            ans["profit_obj"] = profit_obj
            ans["capacity_remain"] = capacity_remain
            ans["weight_in_bag"] = weight_in_bag
            ans["Partial_Complete"] = Partial_Complete
            break
    profit_bag = 0
    for i in range(n):
        profit_bag += x[i] * profit_sorted[i]  

    print(ans)
    return profit_bag

def calc_profit_by_maxprofit(storage_capacity, p, w, n, x):

    ans = pd.DataFrame({
        "weight_obj" : [],
        "profit_obj" : [],
        "capacity_remain" : [],
        "weight_in_bag" : [],
        "Partial_Complete" : []
    })
    st =storage_capacity
    profit = [x for x in p]
    weight = [x for x in w]
    profit_sorted = []
    weight_sorted = []
    for _ in range(n):
        max_index = profit.index(max(profit))
        profit_sorted.append(profit[max_index])
        weight_sorted.append(weight[max_index])
        profit.pop(max_index)
        weight.pop(max_index)

    weight_obj = [0]
    profit_obj = [0]
    capacity_remain = [storage_capacity]
    weight_in_bag = [0]
    Partial_Complete = ["-"]

    for i in range(n):
        if(storage_capacity >= weight_sorted[i]):
            x[i] = 1
            weight_in_bag.append(15 - storage_capacity + weight_sorted[i])
            storage_capacity -= weight_sorted[i]
            weight_obj.append(weight_sorted[i])
            profit_obj.append(x[i] * profit_sorted[i])
            capacity_remain.append(storage_capacity)
            Partial_Complete.append("Complete")
        else:
            x[i] = storage_capacity/weight_sorted[i]
            weight_obj.append(storage_capacity)
            profit_obj.append(x[i] * profit_sorted[i])
            if(storage_capacity != 0):
                Partial_Complete.append("Partial")
            else:
                Partial_Complete.append("-")
            storage_capacity = 0
            capacity_remain.append(storage_capacity)
            weight_in_bag.append(st)

            ans["weight_obj"] = weight_obj
            ans["profit_obj"] = profit_obj
            ans["capacity_remain"] = capacity_remain
            ans["weight_in_bag"] = weight_in_bag
            ans["Partial_Complete"] = Partial_Complete
            break

    profit_bag = 0
    for i in range(n):
        profit_bag += x[i] * profit_sorted[i]  

    print(ans)
    return profit_bag

    
def calc_profit_by_profit_by_weight_ratio(storage_capacity, p, w, n, x):

    ans = pd.DataFrame({
        "weight_obj" : [],
        "profit_obj" : [],
        "capacity_remain" : [],
        "weight_in_bag" : [],
        "Partial_Complete" : []
    })
    st = storage_capacity
    ratio = list(np.array(p) / np.array(w))
    profit = [x for x in p]
    weight = [x for x in w]
    profit_sorted = []
    weight_sorted = []
    ratio_sorted = []

    for _ in range(n):
        max_index = ratio.index(max(ratio))
        profit_sorted.append(profit[max_index])
        weight_sorted.append(weight[max_index])
        ratio_sorted.append(ratio[max_index])
        profit.pop(max_index)
        weight.pop(max_index)
        ratio.pop(max_index)

        
    weight_obj = [0]
    profit_obj = [0]
    capacity_remain = [storage_capacity]
    weight_in_bag = [0]
    Partial_Complete = ["-"]

    for i in range(n):
        if(storage_capacity >= weight_sorted[i]):
            x[i] = 1
            weight_in_bag.append(15 - storage_capacity + weight_sorted[i])
            storage_capacity -= weight_sorted[i]
            weight_obj.append(weight_sorted[i])
            profit_obj.append(x[i] * profit_sorted[i])
            capacity_remain.append(storage_capacity)
            Partial_Complete.append("Complete")
        else:
            x[i] = storage_capacity/weight_sorted[i]
            weight_obj.append(storage_capacity)
            profit_obj.append(x[i] * profit_sorted[i])
            if(storage_capacity != 0):
                Partial_Complete.append("Partial")
            else:
                Partial_Complete.append("-")
            storage_capacity = 0
            capacity_remain.append(storage_capacity)
            weight_in_bag.append(st)

            ans["weight_obj"] = weight_obj
            ans["profit_obj"] = profit_obj
            ans["capacity_remain"] = capacity_remain
            ans["weight_in_bag"] = weight_in_bag
            ans["Partial_Complete"] = Partial_Complete
            break

    profit_bag = 0
    for i in range(n):
        profit_bag += x[i] * profit_sorted[i]  
    print(ans)
    return profit_bag


storage_capacity = 15
n = 7
profit = [9, 15, 12, 4, 6, 16, 8]
weight = [2, 3, 5, 4, 3, 6, 3]
x = [0 for _ in range(n)]
    
choice = int(input("Enter the how you would like to calculate profit \n1 by minimum weight \n 2 by maximum profit \n  3 by ratio of profit and weight : "))

match(choice):
    case 1: print("The profit by min weight : ",calc_profit_by_minweight(storage_capacity, profit, weight, n, x))
    case 2: print("Profit obtained by max profit method : ",calc_profit_by_maxprofit(storage_capacity, profit, weight, n, x))
    case 3: print("Profit obtained by ratio is : ",calc_profit_by_profit_by_weight_ratio(storage_capacity, profit, weight, n, x))
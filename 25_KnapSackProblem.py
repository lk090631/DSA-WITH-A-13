def knapsack(weight,profit,capicity,index):
    if index==len(weight) or capicity ==0:
        return 0
    
    if weight[index]>capicity:
        return knapsack(weight,profit,capicity,index+1)
    
    include = profit[index] + knapsack(weight,profit,capicity-weight[index],index+1)
    exclude = knapsack(weight,profit,capicity,index+1)
    
    return max(include,exclude)


profit=[10,40,30,50]
weight=[5,4,6,3]
capicity=10
print(knapsack(weight,profit,capicity,0))
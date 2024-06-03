

def max_apples(apples, days, i, count, day):
    if(i >= len(apples)):
        return count
    if((i + days[i]) < day or apples[i] == 0 or days[i] == 0):
      if(i < day):
          return max_apples(apples, days, i+1, count, day)
      else:
          return max_apples(apples, days, i+1, count, day + 1)
    
    if(i + days[i] == day + 1):
        return max_apples(apples, days, i+1, count+1, day + 1)
    
    if((i + days[i] - day) < apples[i]):
            if(i + days[i] - day == 0):
              return max_apples(apples, days, i+1, count+1, day + 1)  
            return max_apples(apples, days, i+1, count + i + days[i] - day,  day + (i + days[i] - day))
    else:
       return max_apples(apples, days, i+1, count + apples[i], day + apples[i])

apples = [1,2,3,5,2]
days = [3,2,1,4,2]

# apples = [3,0,0,0,0,2]
# days = [3,0,0,0,0,2]

apples = [2, 1, 10]
days = [2, 10, 1]

print(max_apples(apples, days, 0, 0, 0))




    





apples = [1,2,3,5,2]
days = [3,2,1,4,2]
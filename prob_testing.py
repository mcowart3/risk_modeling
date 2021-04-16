from combat_simul import combat, roll
import random
import pandas as pd

myList = []
for i in range(1, 20):
    newList = []
    for j in range(1, 20):
        tertList = []
        for k in range(1, 1000):
            result = combat(i, j)
            if result < 0:
                result = 0
            
            tertList.append(result)
        newList.append(sum(tertList) / len(tertList))
        
    myList.append(newList)
df = pd.DataFrame(myList, columns = range(1, 20))
print(df)


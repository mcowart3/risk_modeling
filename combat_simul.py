
def combat(attacker, defender):
    a = attacker
    d = defender
    if a >= 3:
        a_dice = 3
    else:
        a_dice = a
    if d >= 2:
        d_dice = 2
    else:
        d_dice = 1
    results = roll(a_dice, d_dice)
    #print (results)
    a -= results[0]
    d -= results[1]
    #print(d)
    if a <= 0:
        
        outcome = d * -1
        return outcome
        
    else:
        if d <= 0:
            
            outcome = a
            return outcome
            
    return combat(a, d)
        
def roll(a, d):
    attacker = []
    defender = []
    result = [0, 0]
    for i in range(a):
        attacker.append(random.randint(1,6))
    for i in range(d):
        defender.append(random.randint(1,6))
    if max(attacker) > max(defender):
        result[1] += 1
    else:
        result[0] += 1
    attacker.remove(max(attacker))
    defender.remove(max(defender))
    if len(attacker) == 2 and len(defender) == 1:
        if max(attacker) > defender[0]:
            result[1] += 1
        else:
            result[0] += 1
    return result
import random



import random

def get_score(target, dice_map):
    score = 0
    if(target in dice_map):
        score += dice_map[target]

    i = target-1
    while i > 0:
        # print(f"i = {i}, dice_map[{i}] = {dice_map[i]} mod = {target % i}")
        if(i > 6):
            i-=1
            continue
        if(dice_map[i] == 0):
            i-=1
            continue
        elif(target % i == 0):
            # print(f"floor = {int(dice_map[i]*i/target)}")
            score += int(dice_map[i]*i/target)
        else:
            score += min(dice_map[i], dice_map[target-i])
            dice_map[target-i] = 0
        dice_map[i] = 0
        i -= 1
    return score

dice_map = {
    1: 1,
    2: 2,
    3: 1,
    4: 2,
    5: 0,
    6: 0
}

dice_map1 = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 6
}

dice_map2 = {
    1: 0,
    2: 1,
    3: 0,
    4: 5,
    5: 0,
    6: 0
}

dice_map3 = {
    1: 3,
    2: 1,
    3: 0,
    4: 2,
    5: 0,
    6: 0
}

dice_map4 = {
    1: 0,
    2: 0,
    3: 3,
    4: 0,
    5: 3,
    6: 0
}

dice_map5 = {
    1: 2,
    2: 0,
    3: 0,
    4: 4,
    5: 0,
    6: 0
}

# With target 5 this should be 3
dice_map6 = {
    1: 2,
    2: 1,
    3: 2,
    4: 0,
    5: 1,
    6: 0
}



res = get_score(5, dice_map6)
print(res)

def test():
    for _ in range(4):
        # dices = []
        dice_map = {i:0 for i in range(1,7)}
        for _ in range(6):
            throw = random.randint(1,6)
            # dices.append(throw)
            dice_map[throw] += 1
        target = 5
        non_0_dice = {key:val for key,val in dice_map.items() if val != 0 and key <= target} 
        print(non_0_dice)
        score = get_score(target, dice_map)
        print(f"Score = {score}")
        print('______________________')
    
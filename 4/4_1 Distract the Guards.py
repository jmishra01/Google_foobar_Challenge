# Distract the Guards
# ===================

# The time for the mass escape has come, and you need to distract the guards so that the bunny prisoners can make it out! Unfortunately for you, 
# they're watching the bunnies closely. Fortunately, this means they haven't realized yet that the space station is about to explode due to the 
# destruction of the LAMBCHOP doomsday device. Also fortunately, all that time you spent working as first a minion and then a henchman means that 
# you know the guards are fond of bananas. And gambling. And thumb wrestling.

# The guards, being bored, readily accept your suggestion to play the Banana Games.

# You will set up simultaneous thumb wrestling matches. In each match, two guards will pair off to thumb wrestle. The guard with fewer bananas will 
# bet all their bananas, and the other guard will match the bet. The winner will receive all of the bet bananas. You don't pair off guards with the 
# same number of bananas (you will see why, shortly). You know enough guard psychology to know that the one who has more bananas always gets over-confident 
# and loses. Once a match begins, the pair of guards will continue to thumb wrestle and exchange bananas, until both of them have the same number of bananas. 
# Once that happens, both of them will lose interest and go back to guarding the prisoners, and you don't want THAT to happen!

# For example, if the two guards that were paired started with 3 and 5 bananas, after the first round of thumb wrestling they will have 6 and 2 (the one with 
# 3 bananas wins and gets 3 bananas from the loser). After the second round, they will have 4 and 4 (the one with 6 bananas loses 2 bananas). 
# At that point they stop and get back to guarding.

# How is all this useful to distract the guards? Notice that if the guards had started with 1 and 4 bananas, then they keep thumb wrestling!
#  1, 4 -> 2, 3 -> 4, 1 -> 3, 2 -> 1, 4 and so on.

# Now your plan is clear. You must pair up the guards in such a way that the maximum number of guards go into an infinite thumb wrestling loop!

# Write a function answer(banana_list) which, given a list of positive integers depicting the amount of bananas the each guard starts with, returns the 
# fewest possible number of guards that will be left to watch the prisoners. Element i of the list will be the number of bananas that guard i 
# (counting from 0) starts with.

# The number of guards will be at least 1 and not more than 100, and the number of bananas each guard starts with will be a positive integer no more 
# than 1073741823 (i.e. 2^30 -1). Some of them stockpile a LOT of bananas.

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java

# Test cases
# ==========

# Inputs:
#     (int list) banana_list = [1, 1]
# Output:
#     (int) 2

# Inputs:
#     (int list) banana_list = [1, 7, 3, 21, 13, 19]
# Output:
#     (int) 0

# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. 
# If your solution passes the test cases, it will be removed from your home folder.

from itertools import combinations

def choose(l):
    check_list = [l[0][0], l[0][1]]
    for i in l[1:]:
        if i[0] in check_list:
            return False
        else:
            check_list.append(i[0])
        if i[1] in check_list:
            return False
        else:
            check_list.append(i[1])
    return True

def check(x, y):
    if (x+y)%2 == 1:
        return 1
    if x == y:
        return 0
    if (x+y)%4 != 0:
        return 1
    mem = [x]
    append = mem.append
    while True:
        if x < y:
            x, y = 2*x, y - x
        elif y < x:
            x, y = 2*y, x - y
        else:
            del mem
            return 0
        if x in mem:
            del mem
            return 1
        append(x)
        
def answer(banana_list):
    banana_list_len = len(banana_list)
    if banana_list_len == 1:
        return 1
    if banana_list_len == 2:
        return 2*(1-check(banana_list[0], banana_list[1]))
    guard_comp = filter(choose, combinations(combinations(banana_list, 2), banana_list_len//2))
    count = [sum([2*(1-check(j[0],j[1])) for j in i]) for i in guard_comp]
    return min(count)

banana_list = [1, 7, 3, 21, 13, 19, 31, 43]
print(answer(banana_list))

# guard_comp = (comb for comb in combinations(combinations(banana_list, 2), len(banana_list)//2) if choose(comb))
# for i in guard_comp:
#     print(i)

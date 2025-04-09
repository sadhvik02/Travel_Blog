# from itertools import combinations

# def getPossibleWay(M, S):
#     if S >= M:
#         print("Invalid input")
#         return "Invalid input"

#     all_combos = combinations(range(M), S)
#     valid_combos = [
#         combo for combo in all_combos
#         if all(combo[i+1] - combo[i] > 1 for i in range(len(combo)-1))
#     ]

#     print(f"Valid combos: {valid_combos}")
#     print(len(valid_combos))
#     return len(valid_combos)

# getPossibleWay(10, 6)



# getPossibleWay(7,3)
# getPossibleWay(10,6)
# getPossibleWay(10,5)
# getPossibleWay(8,3)
# getPossibleWay(12,5)
# getPossibleWay(15,3)


# def minDiff(arr):
#     arr.sort()
    
#     total_diff = sum(abs(arr[i] - arr[i-1]) for i in range(1, len(arr)))

#     print(total_diff)
#     return total_diff


# def min_absolute_difference(arr):
#     arr.sort()
#     total_difference = 0
#     for i in range(len(arr) - 1):
#         total_difference += abs(arr[i] - arr[i+1])
#     print(total_difference)
#     return total_difference
# min_absolute_difference([5,1,3,7,3])
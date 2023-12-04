# My version of zip()
def zap(list_one, list_two):
    new_list = []
    shortest_list_length = min(len(list_one), len(list_two))

    if shortest_list_length > 0:
        new_list = [(list_one[i], list_two[i]) for i in range(shortest_list_length)]
    return new_list

print(zap([0,1,2,3], [5,6,7]))
print(zap([2],[3,3]))
print(zap([3],[9]))
print(zap([], []))

# Output:
    # [(0, 5), (1, 6), (2, 7)]
    # [(2, 3)]
    # [(3, 9)]
    # []
#Refactor and optimize the below python script

''''def find_common(a, b):
    res = []
    for i in a:
        for j in b:
            if i == j:
                res.append(i)
    return res '''
def find_common(a, b):
    return list(set(a) & set(b))
# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = find_common(list1, list2)
print(common_elements)  # Output: [4, 5]

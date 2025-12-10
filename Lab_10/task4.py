#Give the structured and well formatted version of this below python script (modularize into smaller helper functions)

'''def process_scores(scores):
    total = 0
    for s in scores:
        total += s
    avg = total / len(scores)

    highest = scores[0]
    for s in scores:
        if s > highest:
            highest = s

    lowest = scores[0]
    for s in scores:
        if s < lowest:
            lowest = s

    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)'''


def calculate_total(scores):
    return sum(scores)  
def calculate_average(total, count):
    return total / count if count > 0 else 0
def find_highest(scores):
    return max(scores) if scores else None
def find_lowest(scores):
    return min(scores) if scores else None
def process_scores(scores):
    total = calculate_total(scores)
    average = calculate_average(total, len(scores))
    highest = find_highest(scores)
    lowest = find_lowest(scores)

    print("Average:", average)
    print("Highest:", highest)
    print("Lowest:", lowest)

# Example usage:
scores_list = [85, 90, 78, 92, 88]
process_scores(scores_list)
def calculate_stats(numders):
    total_sum = sum(numders)
    average = total_sum / len(numders)
    maximum = max(numders)
    minimum = min(numders)
    return total_sum, average, maximum, minimum


numders = [5, 10, 15, 20, 25]
total, average, max_num, min_num = calculate_stats(numders)

print(f"Total Sum: {total}")
print(f"Average: {average}")
print(f"Maximum: {max_num}")
print(f"minimum: {min_num}")
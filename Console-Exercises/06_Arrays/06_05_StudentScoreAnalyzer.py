scores = [78, 92, 85, 67, 90, 73, 88, 94, 60, 81]
total_score = 0
lowest_score = scores[0]
highest_score = scores[0]
sorted_scores = []

# get Total score
for i in range(len(scores)):
    total_score += scores[i]

# get average score from total score and amount of scores
average_score = total_score / len(scores)
print(f"Avg. Score: {average_score}")

# get lowest and highest score
for score in scores:
    if score < lowest_score:
        lowest_score = score
    if score > highest_score:
        highest_score = score

print(f"Low. Score: {lowest_score}")
print(f"Hig. Score: {highest_score}")

sorted_scores = scores.copy()

# bubble sort
for i in range(len(sorted_scores)):
    for j in range(len(sorted_scores) - 1 - i):
        if sorted_scores[j] > sorted_scores[j + 1]:
            # swap      
            sorted_scores[j], sorted_scores[j + 1] = sorted_scores[j + 1], sorted_scores[j]

print(f"Sorted Scores {sorted_scores}")  
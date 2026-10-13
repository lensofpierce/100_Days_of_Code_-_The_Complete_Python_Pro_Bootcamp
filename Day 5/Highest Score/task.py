student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# # Method 1
# total_exam_score = sum(student_scores)
# print(total_exam_score)
#
# # Method 2
# sum = 0
# for score in student_scores:
#     sum += score
#
# print(sum)

print(max(student_scores))

high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score
    elif score < high_score:    # Not needed
        continue                # Not needed
print(high_score)



exam_scores=[123,543,674,342,567,100,99,456,234,789,120,127,230,127,128,124]

# total_exam_score = sum(exam_scores)

sum=0
for score in exam_scores:
    sum += score

print(sum)

# max_score = max(exam_scores)

max_score=0

for score in exam_scores:
    if score>max_score:
        max_score=score

print(max_score)







#https://stepic.org/media/attachments/course67/week_2.html

quad_sum = 0
sum = 0

while True:
    b = int(input())
    sum += b
    quad_sum += b * b
    if sum == 0:
        break

print(quad_sum)

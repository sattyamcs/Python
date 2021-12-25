def percentage (marks):
    p = ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p

marks1 = [70,67,99,54]
percentage1 = percentage(marks1)
marks2 = [70,70,70,70]
percentage2 =percentage(marks2)

print(percentage1,percentage2)
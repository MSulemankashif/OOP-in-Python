# Write a function that returns a average marks if a list of marks is passed as a parameter

def average_func(marks):

    total = sum(marks)

    average = total / len(marks)
    return  average

student_marks = [80, 70, 90, 60]

result = average_func(student_marks)

print("Average Marks: ", int(result))

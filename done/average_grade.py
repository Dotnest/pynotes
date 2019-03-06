# Define a function that takes a list of lists and returns a new list of
# lists with a student's name and their average grade in each sublist.

def average_grade(lst):    
    """ Return students' names and their average grades.
    >>> average_grade([['Bob', 56, 80, 72, 90], ['Alice', 60, 88, 44, 70]])
    >>> [['Bob', 74.5], ['Alice', 65.5]]
    """
    # your code here
    for student in lst:
        total = 0
        count = 0
        for grade in student:
            if type(grade) != type("a"):
                total = total + grade
                count += 1
        student[1] = total/count
        for _ in range(len(student)-2):
            student.pop()
        print(student)
        #print(total)
        #print(count)


average_grade([['Bob', 56, 80, 72, 90], ['Alice', 60, 88, 44, 70]])
#>>> [['Bob', 74.5], ['Alice', 65.5]]
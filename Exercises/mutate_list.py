# Define a function that does this:
# Given a list of strings, with each string having a student’s name and
# their grades, mutate the input list so the original string positions are
# replaced with their average grades. The function doesn’t need an explicit
# return statement.


def get_averages(lst):
    # your code here
    for i in range(len(lst)):
        average = lst[i].split(', ')
        average = average[1:]
        for n in range(len(average)):
            average[n] = float(average[n])
        average = sum(average)/len(average)
        lst[i] = average
    

reports = ['Anna, 50, 92, 80', 'Bill, 60, 70', 'Cal, 98.5, 100, 95.5, 98']
get_averages(reports)
print(reports)
# [74.0, 65.0, 98.0]

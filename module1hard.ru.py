grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
set = sorted(students)
x = grades[0]
average_x = sum(x) / len(x)
y = grades[1]
average_y = sum(y) / len(y)
z = grades[2]
average_z = sum(z) / len(z)
a = grades[3]
average_a = sum(a) / len(a)
b = grades[4]
average_b = sum(b) / len(b)
av = [average_x, average_y, average_z, average_a, average_b]
s = set
k = {s: av for s, av in zip(s, av)}
print(k)





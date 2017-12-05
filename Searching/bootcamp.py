import collections
import bisect
Student = collections.namedtuple('Student', ('name','grade_point_average'))

def comp_gpa(student):
	return (-student.grade_point_average, student.name)

def search_student(students, target, comp_gpa):
	i= bisect.bisect_left([comp_gpa(student) for student in students], comp_gpa(target))
	return 0<=i<len(students) and students[i]==target


students=[Student("powei", 4.0), Student("kelly", 3.5), Student("young", 3.0)]

print search_student(students, Student("kelly", 3.2), comp_gpa)


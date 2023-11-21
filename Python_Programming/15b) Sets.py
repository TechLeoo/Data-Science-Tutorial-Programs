# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 19:34:40 2023

@author: lEO
"""

set = set({})

# Working with a set
# ADDING VALUES IN A SET
set.add("Leo")
set.add("Leo") # Sets do not take duplicates

# Creating a Subset for UNION, DIFFERENCE, INTERSECTION
People = {"Leo", "Adey", "Timi", "Franklin", "Fola", "Emma", "Daniel"}
Students = {"Edsam", "Basirat", "Olusola", "Dami", "Niyi", "Micheal", "Donald", "Henry", "Adey"}
FemaleStudents = {"Edsam", "Basirat", "Olusola",}
MaleStudents = {"Niyi", "Micheal", "Donald", "Henry", "Adey"}
Instructor = {"Leo", "Daniel"}
ThingsCanPop = {"Leo", "Adey", "Timi", "Franklin", "Fola", "Emma", "Daniel", "Edsam", "Basirat", "Olusola", "Dami", "Niyi", "Micheal", "Donald", "Henry", "Adey"}

# INTERSECTION
intersectPeopleMaleStudents = People.intersection(MaleStudents)
intersectStudentsFemaleStudents = Students.intersection(FemaleStudents)

# UNION
unionPeopleStudents = Students.union(People)
unionPeopleInstructor = Instructor.union(People)

# DIFFERENCE
differencePeopleInstructor = People.difference(Instructor)
differenceInstructorPeople = Instructor.difference(People)

# SUBSET
subsetPeopleInstructor = Instructor.issubset(People)
subsetStudentsFemaleStudents = FemaleStudents.issubset(Students)
subsetInstructorPeople = People.issubset(Instructor)

# SUPERSET
supersetPeopleInstructor = People.issuperset(Instructor) # True
supersetStudentsMaleStudents = MaleStudents.issuperset(Students) # False
supersetMaleStudents = Students.issuperset(MaleStudents) # True

# TAKING ELEMENTS OUT OF A SET
# 1) POP
WhatWePopped = ThingsCanPop.pop() # Will remove the FIRST ELEMENT after the SET has shuffled.
print(WhatWePopped)

# 2) REMOVE
WhatWeRemove = ThingsCanPop.remove("Franklin") # Will remove FRANKLIN entirely from our set.
print(WhatWeRemove)

# 3) DISCARD
WhatWeDiscard = ThingsCanPop.discard("Timi") # Will remove Timi entirely from our set.
print(WhatWeDiscard)

# 4a) CLEAR
WhatWeClear = ThingsCanPop.clear() # Clear all elements.
print(WhatWeClear)

# OR

# 4b) DELETE
# del ThingsCanPop
# print(ThingsCanPop)
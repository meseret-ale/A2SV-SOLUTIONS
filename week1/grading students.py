#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    
    grade = []
    for n in range(0, len(grades) ):
        if grades[n] < 40:
            grade.append(grades[n])
        else:
            for i in range(45, 105, 5):
                if i > grades[n]:
                    if i - grades[n] < 3:
                        grade.append(i)
                        break
                    else:
                        grade.append(grades[n])
                        break
                else:
                    continue
    return grade
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

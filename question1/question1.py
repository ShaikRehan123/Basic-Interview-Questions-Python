# a company which provides solutions to Tech Problems.
# Employees in this company have to test their final
# development code on both websites and an app.
# They hustle continuously to shift from Website to
# app and App to Website.. Company has provided the
# data of the employees with the timestamt and the work
# they are doing(()Website or App).You have to find
# out the minimum number of switches employees do from
# website to app and app to website.while doing this task.


# Initially you will be given an interger N an M denoting
# the number of websites and number of apps used respectively..
# Then an array of A of N integer denotes the time
# at which employees use Website in increasing order and an
# array B of M integer denotes the time at which employees
# use Apps in increasing order.

# You can assume that the employees cannot work on both
# websites and apps at the same time.


# Example:
# Input:
# N = 4 N -> NO. of websites
# A {23,27,30,33} -> time at which employees use websites
# M = 3 M -> NO. of apps
# B {9,10,21} -> time at which employees use apps

# Output:
# 1 -> minimum number of switches

# Explanation:
# Initially employees will start from Apps at 9 then
# do the word without switching till time 22 and then
# at time 23 they will switch to Website and do the
# task without switching till time 33.
# So the minimum number of switches is 1.


N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))


def min_switches(A, B):
    min_switches = 0
    i = 0
    j = 0

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            min_switches += 1
            i += 1
        else:
            j += 1

    return min_switches


print(min_switches(A, B))

# Unknown Problem

## Difficulty
Unknown

## Problem
[Unknown Problem](https://www.geeksforgeeks.org/problems/minimum-cost-to-connect-all-houses-in-a-city/1)

## Description
Courses
Big Savings Sale
Tutorials
Interview Prep
Switch to Dark Mode
Sign In
Menu
Back to Explore Page
Problem
Editorial
Submissions
Comments
Minimum cost to connect all houses in a city
Difficulty:
Medium
Accuracy:
64.58%
Submissions:
17K+
Points:
4
Given a 2D array
houses[][]
, consisting of
n
2D coordinates
{x, y}
where each coordinate represents the
location of each house
, the task is to find the
minimum cost to connect
all the houses of the city.
The
cost of connecting
two houses is the
Manhattan Distance
between the two points (x
i
, y
i
) and (x
j
, y
j
) i.e., |x
i
– x
j
| + |y
i
– y
j
|, where |p| denotes the absolute value of p.
Examples :
Input:
n = 5 houses[][] = [[0, 7], [0, 9], [20, 7], [30, 7], [40, 70]]
Output:
105
Explanation:
Connect house 1 (0, 7) and house 2 (0, 9) with cost = 2
Connect house 1 (0, 7) and house 3 (20, 7) with cost = 20
Connect house 3 (20, 7) with house 4 (30, 7) with cost = 10 
At last, connect house 4 (30, 7) with house 5 (40, 70) with cost 73.
All the houses are connected now.
The overall minimum cost is 2 + 10 + 20 + 73 = 105.
Input:
n = 4 houses[][] = [[0, 0], [1, 1], [1, 3], [3, 0]]
Output:
7
Explanation:
Connect house 1 (0, 0) with house 2 (1, 1) with cost = 2
Connect house 2 (1, 1) with house 3 (1, 3) with cost = 2 
Connect house 1 (0, 0) with house 4 (3, 0) with cost = 3 
The overall minimum cost is 3 + 2 + 2 = 7.
Constraint:
1 ≤ n ≤ 10
3
0 ≤ houses[i][j] ≤ 10
3
Expected Complexities
Time Complexity: O(n^2 log n)
Auxiliary Space: O(n^2)
Related Articles
Minimum Cost Required To Connect All Houses In A City
Please
login
to report an issue.
From Zero to Bharat-Wide. Build where your passion lies. Visit our website
Output Window
Compilation Results
Custom Input
Login

Courses
Big Savings Sale
Tutorials
Interview Prep
Switch to Dark Mode
Sign In
Menu
Back to Explore Page
Problem
Editorial
Submissions
Comments
Minimum cost to connect all houses in a city
Difficulty:
Medium
Accuracy:
64.58%
Submissions:
17K+
Points:
4
Given a 2D array
houses[][]
, consisting of
n
2D coordinates
{x, y}
where each coordinate represents the
location of each house
, the task is to find the
minimum cost to connect
all the houses of the city.
The
cost of connecting
two houses is the
Manhattan Distance
between the two points (x
i
, y
i
) and (x
j
, y
j
) i.e., |x
i
– x
j
| + |y
i
– y
j
|, where |p| denotes the absolute value of p.
Examples :
Input:
n = 5 houses[][] = [[0, 7], [0, 9], [20, 7], [30, 7], [40, 70]]
Output:
105
Explanation:
Connect house 1 (0, 7) and house 2 (0, 9) with cost = 2
Connect house 1 (0, 7) and house 3 (20, 7) with cost = 20
Connect house 3 (20, 7) with house 4 (30, 7) with cost = 10 
At last, connect house 4 (30, 7) with house 5 (40, 70) with cost 73.
All the houses are connected now.
The overall minimum cost is 2 + 10 + 20 + 73 = 105.
Input:
n = 4 houses[][] = [[0, 0], [1, 1], [1, 3], [3, 0]]
Output:
7
Explanation:
Connect house 1 (0, 0) with house 2 (1, 1) with cost = 2
Connect house 2 (1, 1) with house 3 (1, 3) with cost = 2 
Connect house 1 (0, 0) with house 4 (3, 0) with cost = 3 
The overall minimum cost is 3 + 2 + 2 = 7.
Constraint:
1 ≤ n ≤ 10
3
0 ≤ houses[i][j] ≤ 10
3
Expected Complexities
Time Complexity: O(n^2 log n)
Auxiliary Space: O(n^2)
Related Articles
Minimum Cost Required To Connect All Houses In A City
Please
login
to report an issue.
From Zero to Bharat-Wide. Build where your passion lies. Visit our website
Output Window
Compilation Results
Custom Input
Login

Menu
Back to Explore Page
Problem
Editorial
Submissions
Comments
Minimum cost to connect all houses in a city
Difficulty:
Medium
Accuracy:
64.58%
Submissions:
17K+
Points:
4
Given a 2D array
houses[][]
, consisting of
n
2D coordinates
{x, y}
where each coordinate represents the
location of each house
, the task is to find the
minimum cost to connect
all the houses of the city.
The
cost of connecting
two houses is the
Manhattan Distance
between the two points (x
i
, y
i
) and (x
j
, y
j
) i.e., |x
i
– x
j
| + |y
i
– y
j
|, where |p| denotes the absolute value of p.
Examples :
Input:
n = 5 houses[][] = [[0, 7], [0, 9], [20, 7], [30, 7], [40, 70]]
Output:
105
Explanation:
Connect house 1 (0, 7) and house 2 (0, 9) with cost = 2
Connect house 1 (0, 7) and house 3 (20, 7) with cost = 20
Connect house 3 (20, 7) with house 4 (30, 7) with cost = 10 
At last, connect house 4 (30, 7) with house 5 (40, 70) with cost 73.
All the houses are connected now.
The overall minimum cost is 2 + 10 + 20 + 73 = 105.
Input:
n = 4 houses[][] = [[0, 0], [1, 1], [1, 3], [3, 0]]
Output:
7
Explanation:
Connect house 1 (0, 0) with house 2 (1, 1) with cost = 2
Connect house 2 (1, 1) with house 3 (1, 3) with cost = 2 
Connect house 1 (0, 0) with house 4 (3, 0) with cost = 3 
The overall minimum cost is 3 + 2 + 2 = 7.
Constraint:
1 ≤ n ≤ 10
3
0 ≤ houses[i][j] ≤ 10
3
Expected Complexities
Time Complexity: O(n^2 log n)
Auxiliary Space: O(n^2)
Related Articles
Minimum Cost Required To Connect All Houses In A City
Please
login
to report an issue.
From Zero to Bharat-Wide. Build where your passion lies. Visit our website
Output Window
Compilation Results
Custom Input
Login

## Tags
Problem, Editorial, Submissions, Comments, Compilation Results, Custom Input

## Company Tags
CoursesBig Savings Sale, Tutorials, Interview Prep, Switch to Dark Mode, Difficulty:Medium, Accuracy:64.58%, Submissions:17K+, Points:4, Examples :


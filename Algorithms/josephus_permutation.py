def last_person(number_of_people, k):
    people = []
    [people.append(x) for x in range(1, number_of_people + 1)]
    i = 0
    while len(people) > 1:
        i = (i + k - 1) % len(people)
        people.remove(people[i])

    return people[0]


print(last_person(41, 3))

"""
Josephus problem
In computer science and mathematics, the Josephus problem is a theoretical problem related to a certain counting-out game. In this scenario, people are standing in a circle waiting to be eliminated every kth position until only one person remains, who is considered the survivor or the last person standing. The function last_person(number_people, k) calculates who that survivor is, given a total number of people (number_people) and a step rate (k) that determines which person is eliminated in each round.

HOW IT WORKS:

Initialization:

people is initialized as an empty list.
A list comprehension is used to fill people with integers from 1 to number_of_people inclusive, representing each person's position in the circle.

Elimination Process:

The variable i is initialized at 0 and represents the current index in people where the elimination will occur.
A while loop runs as long as more than one person remains in the list (len(people) > 1).
Inside the loop, i is updated to (i + k - 1) % len(people). This calculation finds the index of the next person to be eliminated. The -1 accounts for the zero-based indexing of the list and the fact that kth person from the current index i is to be removed.
The person at index i is then removed from people using people.remove(people[i]).

Survivor:

Once the loop ends (meaning only one person is left), people[0] is returned. This person is the survivor of the elimination process.

"""


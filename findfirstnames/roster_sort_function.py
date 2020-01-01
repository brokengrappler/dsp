

def find_first_names(students_input):
    """Function that returns the first names of students in the class
    ---
    students_input: list of student names ('firstname lastname')
    output: return list of only firstnames
    """
    firstnames = []

    for names in students_input:
        parsedname = names.split()
        firstnames.append(parsedname[0].capitalize())

    return sorted(firstnames)

testcase1 = [
        'Nicholas Jones', 'Ashley Rowland', 'Stephanie Jackson',
        'Donald Hicks', 'Evan Johnson'
    ]

testcase2 = [
        'Nicholas Jones', 'Ashley Rowland', 'Stephanie Jackson',
        'Donald Hicks', 'Evan Johnson', 'ashley Parker'
    ]

testcase3 = [
        'Brittany Johnson', 'Sarah Klein', 'Drew Thompson', 'Jimmy Parker',
        'Jill Kelly', 'Heidi Howard', 'Jonathan Watkins', 'Terri Allen',
        'Angela Reyes', 'Suzanne Roberts', 'daniel burgess MD',
        'Cristina Daniels', 'Sandra Vargas', 'Rachel Weeks', 'Nathaniel Mills',
        'Brittany Barnes', 'Brian Jennings', 'Alexandra Walker',
        'Robert Berry', 'John Mann', 'Erica Russell'
    ]

print(bool(find_first_names.__doc__))

print('students_input' in find_first_names.__doc__)

print(find_first_names(testcase2))
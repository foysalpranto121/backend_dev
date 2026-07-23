courses = [
    "Machine Learning",
    "Data Analytics",
    "Python",
    "Flutter",
    "AI Agent"
]

search = input("Enter Search: ")

## in this case i take linear search algorithm 

for course in courses:      
    if search.lower() in course.lower():
        print(course)
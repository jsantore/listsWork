import random


def main():
    example1 = "Computer Science 151, Computer Science 415, Computer Science 490"
    example2 = example1.replace("Computer Science", "Comp")
    course_list = ["Computer Science 151", "Computer Science 152",
                   "Computer Science 206", "Computer Science 415",
                   "Computer Science 490", "Computer Science 460",
                   "Computer Science 470"]

    for course in course_list:
        course = course.replace("Computer Science", "Comp")
        print(f"Let's teach {course}")
    first_course = random.choice(course_list)
    print(f"But the first one I'll prepare is {first_course}")
    #middle_courses = course_list[2:4]
    #print(middle_courses)
    # print(example1.upper())
    # print(example1)
    # print(example2)

main()
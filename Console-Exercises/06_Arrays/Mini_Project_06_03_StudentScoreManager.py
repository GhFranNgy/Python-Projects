# list of students
students = []
# dict for scores in each subject of each student
student_scores = {}
# ID
ID = 1

while True:
    try:
        # Menu
        selected_Option = int(input(
            "1. Add student\n"
            "2. Add score of a subject to student\n"
            "3. Show student average\n"
            "4. Show all students\n"
            "5. Exit\n"
        ))
        # ERROR selected option is out of range
        if not 1 <= selected_Option <= 5:
            print("Please enter a number between 1 and 5.")
            continue
    except ValueError:
        # ERROR selected option is not a number
        print("Please enter a valid number.")
        continue

    if selected_Option == 1:
        while True:
            # get student name
            student_Name = input("==========\nEnter name of student:\n").strip()

            # ERROR check for empty name nothing: == 0 == false
            if not student_Name:
                print("Name cannot be empty.")
                continue

            break

        # assign student ID
        student_ID = ID
        # save student Information ID | NAME
        student = (student_ID, student_Name)
        # add student information to list of all students
        students.append(student)
        # create new space for new student in scores
        student_scores[student_ID] = {}
        # add 1 to ID for next student
        ID += 1

        # confirm message
        print(f"==========\nStudent {student_Name} added with ID {student_ID}.")
        print(f"STUDENT INFORMATION: {student}\n==========")

    elif selected_Option == 2:

        # ERROR check if students list is empty: nothing == 0 == false
        if not students:
            print("No students exist yet.")
            continue

        # give user options
        print("==========\nAvailable students:")
        for s in students:
            print(f"ID: {s[0]} | Name: {s[1]}")

        while True:
            # loop until valid student ID is entered
            try:
                student_ID = int(input("Enter student ID:\n"))

                # ERROR if student ID is not found then ask again
                if student_ID not in student_scores:
                    print("Student not found.")
                    continue

                break
            except ValueError:
                # ERROR Invalid Input type
                print("Invalid ID.")

        while True:
            subject = input("Enter subject:\n").strip()

            # ERROR check if input is empty 
            if not subject:
                print("Subject cannot be empty.")
                continue

            break
        
        while True:
            try:
                # get score
                score = int(input("Enter your score (0–100):\n"))

                # if score is not between 0 and 100 then out of range
                if not 0 <= score <= 100:
                    print("Score must be between 0 and 100.")
                    continue

                break
            except ValueError:
                # ERROR score is not a number
                print("Score must be a number")

        # add subject to student if subject is not yet available
        if subject not in student_scores[student_ID]:
            student_scores[student_ID][subject] = []
        # add score to subject
        student_scores[student_ID][subject].append(score)

        # confirm message
        print(f"==========\nScore of {score} was added to subject {subject}.")
        print(f"STUDENT SCORES: {student_scores[student_ID]}\n==========")

    elif selected_Option == 3:
        # ERROR leave to menu if no student exist yet
        if not students:
            print("No students exist yet.")
            continue

        # ask for which students average and give options
        print("==========\nWhich student's average should be shown?")
        for s in students:
            print(f"ID: {s[0]} | Name: {s[1]}")

        while True:
            try:
                # select a student
                student_ID = int(input("Enter student ID to select:\n"))

                # if seached student is not found
                if student_ID not in student_scores:
                    print("Student not found.")
                    continue

                break
            except ValueError:
                # ERROR Invalid Input type
                print("Invalid ID.")
                continue

        # create list to get all scores regardless of subject
        all_scores = []
        # loop through scores and add trhem to all_scores
        for scores in student_scores[student_ID].values():
            all_scores.extend(scores)

        # look for student Name through student ID
        student_Name = next(student[1] for student in students if student[0] == student_ID)

        # if all_scores is something(filled) == 1 == true
        if all_scores:
            # get average
            average = sum(all_scores) / len(all_scores)
            print(f"==========\nThe average of {student_Name} is {average:.2f}\n==========")
        else:
            # ERROR if all_scores is empty
            print(f"==========\n{student_Name} has no scores yet.\n==========")

    elif selected_Option == 4:
        # ERROR leave to menu if no student exist yet
        if not students:
            print("No students exist yet.")
            continue

        # loop through every student and output information
        for student in students:
            student_ID, student_Name = student
            print(
                f"==========\n"
                f"STUDENT INFORMATION: {student} | "
                f"ID: {student_ID} | "
                f"NAME: {student_Name} | "
                f"SCORES: {student_scores[student_ID]}"
            )
        print("==========")

    else:
        # if 5 was selected the close programm
        print("Exiting program...")
        break
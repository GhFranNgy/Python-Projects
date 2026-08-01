import os
import csv
import time

start_time = time.perf_counter()

script_dir = os.path.dirname(__file__)
grades_dir = os.path.join(script_dir, "grades.csv")
report_dir = os.path.join(script_dir, "report.csv")

grades = []
valid_grades = []

def read_file():
    print("Reading csv...")
    try:
        with open (grades_dir, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row)
                grades.append(row)
        print("Done.\n")
    except FileNotFoundError:
        print(f"Error: File {grades_dir} was not found.")
        quit()


# TODO analyze get_average **Understand
def get_average(grades):
    
    print("Getting Average...")
    for row in grades:
        subjects = [key for key in row.keys() if key != "Name"]
        try: 
            values = [int(row[subject]) for subject in subjects]
        except ValueError:
            print(f"Invalid value in {row["Name"]}, line skipped")
            continue
        average = round(sum(values) / len(values), 2)
        row["Average"] = average
        valid_grades.append(row)
        print(row)
    print("Done.\n")

# TODO analyze get_average **Understand
def sort_after_average(grades):
    print("Sort after Average...")
    n = len(grades)
    for i in range(n):
        for j in range(0, n - i - 1):
            if grades[j]["Average"] < grades[j + 1]["Average"]:
                grades[j], grades[j+1] = grades[j+1], grades[j]
    for row in grades:
        print(row)
    print("Done.\n")

# TODO analyze get_average **Understand
def create_report(grades):
    print("Writing Report...")
    fieldnames = ["Name", "Math", "English", "Science", "Average"]
    with open (report_dir, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames= fieldnames)
        writer.writeheader()
        writer.writerows(grades)
    print(f"Done. ({report_dir})\n")

def best_and_last(grades):
    best = grades[0]["Name"]
    last = grades[len(grades) - 1]["Name"]
    print(f"Best Student: {best}")
    print(f"Last Student: {last}\n")

def class_average(grades):
    average = round(sum(row["Average"] for row in grades) / len(grades), 2)
    print(f"Class Average: {average}\n")

read_file()
get_average(grades)
sort_after_average(valid_grades)
create_report(valid_grades)
best_and_last(valid_grades)
class_average(valid_grades)

end_time = time.perf_counter()
runtime = end_time - start_time
print(f"Total Runtime: {runtime}")
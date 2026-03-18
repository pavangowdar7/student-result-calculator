def calculate_result(marks):
    total_marks = sum(marks)
    num_subjects = len(marks)
    percentage = (total_marks / (num_subjects * 100)) * 100
    
    # Assuming passing marks is 35 for each subject
    result = "Pass"
    for mark in marks:
        if mark < 35:
            result = "Fail"
            break
            
    return total_marks, percentage, result

def main():
    subjects = ["Math", "Science", "English", "History", "Geography"]
    marks = []

    print("Enter marks for the following subjects (out of 100):")
    for sub in subjects:
        while True:
            try:
                m = float(input(f"{sub}: "))
                if 0 <= m <= 100:
                    marks.append(m)
                    break
                else:
                    print("Please enter marks between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    total, percent, res = calculate_result(marks)

    print("\n" + "="*30)
    print("      STUDENT REPORT CARD")
    print("="*30)
    print(f"Total Marks: {total}/{len(subjects)*100}")
    print(f"Percentage:  {percent:.2f}%") 
    print(f"Status:      {res}")
    print("="*30)

if __name__ == "__main__":
    main()

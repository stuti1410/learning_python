if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    sorted_score = sorted({student[1] for student in students}) # Extract scores
    second_lowest = sorted_score[1]  # Find second lowest score
    result = [student[0] for student in students if student[1] == second_lowest]  # Find student names having second lowest score
    for i in sorted(result):  # Print names in sorted order.
        print(i)

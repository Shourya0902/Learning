if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    summ = 0
    avg = float(0)
    marks = list()
    for i in student_marks.keys():
        if i == query_name:    
            marks = student_marks[i]
            for j in marks:
                summ = summ +  j
            avg = summ / len(marks)
    print('%.2f'%avg)

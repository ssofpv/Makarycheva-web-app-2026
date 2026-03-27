def compute_average_scores(scores):
    # scores - список кортежей (один кортеж = один предмет)
    # Нужно транспонировать данные, чтобы сгруппировать оценки по студентам
    # zip(*scores) делает именно это
    
    students_scores = zip(*scores)
    averages = []
    
    for student in students_scores:
        avg = sum(student) / len(student)
        averages.append(avg)
        
    return tuple(averages)

if __name__ == '__main__':
    try:
        # Чтение N и X
        line1 = input().split()
        if not line1: exit()
        n, x = map(int, line1)
        
        scores_list = []
        for _ in range(x):
            # Чтение оценок по предмету
            subject_scores = tuple(map(float, input().split()))
            scores_list.append(subject_scores)
            
        averages = compute_average_scores(scores_list)
        
        for avg in averages:
            print(f"{avg:.1f}")
            
    except ValueError:
        pass
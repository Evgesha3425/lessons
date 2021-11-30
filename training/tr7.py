def result_exem(limit, *marks):
    count = 0
    for i in marks[1:]:
        if i > marks[0]:
            count += 1
    print(f"Экзамен сдали {count} учеников")


result_exem(3, 2, 4, 1, 3, 5, 2, 3, 4, 5, 1)
marks = [89,88,79,74,74,74,74,74,64,56,56,25,24]
current_rank = 0
global_rank = 0
current_mark = 0

for mark in marks:
    global_rank += 1
    if mark != current_mark:
        current_mark = mark
        current_rank = global_rank
    print(current_mark, current_rank)
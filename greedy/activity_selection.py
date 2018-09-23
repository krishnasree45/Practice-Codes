def find_number_of_meetings(start_list, finish_list, length):
    prev_fin_time = -1
    number_of_meetings = list()
    for i in range(length):
        finish_time = min(finish_list)
        index_value = finish_list.index(finish_time)
        import ipdb;ipdb.set_trace()
        # print(index_value)
        start_time = start_list[index_value]
        if prev_fin_time > start_time:
            finish_list[index_value] = pow(10, 6)
            continue
        number_of_meetings.append(index_value+1)
        prev_fin_time = finish_time
        finish_list[index_value] = pow(10, 6)
    print(*number_of_meetings, end=" ")


if __name__ == '__main__':
    number_of_test_cases = int(input())
    for i in range(number_of_test_cases):
        length = int(input())
        start_list = list(map(int, input().split()))
        finish_list = list(map(int, input().split()))
        if i == 0:
            print()
        find_number_of_meetings(start_list, finish_list, length)

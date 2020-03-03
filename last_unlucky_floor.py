max_floor_len = 999999
print(" Enter floor len : ")
floor_len_in = int(input())
unlucky = ['4','13']
current_floor = 1

while floor_len_in != 0:
    unlucky_present_ = False

    for num_ in unlucky:
        if str( current_floor ).find( num_ ) != -1:
            unlucky_present_ = True
            continue

    if not unlucky_present_:
        print("-------------")
        print( '\t', current_floor )
        print("-------------")
        floor_len_in = floor_len_in - 1
    current_floor = current_floor + 1
print("------------------------------------------------------")
print(" Last floor number : ", current_floor - 1 )

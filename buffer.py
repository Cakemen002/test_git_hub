def create_buffer():
    buffer = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return buffer

def show_buffer(buffer):
    for i in range(0, 3):
        print(f"{buffer[i][0]} {buffer[i][1]} {buffer[i][2]}")
    print("===============")
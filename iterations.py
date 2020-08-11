intern_counter = 0
extern_counter = 0

while extern_counter <= 10:
    while intern_counter <= 5:
        print(extern_counter, intern_counter)
        intern_counter += 1
    extern_counter += 1
    intern_counter = 0
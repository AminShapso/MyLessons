file_in = r'C:\Users\USER\Documents\Pycharm\Lessons23\Lesson 05.txt'
delimiter = ' '

with open(file_in, "r") as file:   # "r" = Read mode.
    for line_index, line in enumerate(file.readlines()):
        print(f"{line_index = }")
        print(f"{line = }")
        print(f"{line.strip() = }")
        print(f"{line.strip().split(delimiter) = }")

        success = False
        print(f"{success = }")
        for word in line.strip().split(delimiter):
            try:
                print(f"{float(word) = }")
                success = True
            except:
                pass
        print(f"{success = }")
        if not success:
            print("This line has failed to yield a number!")
        print()

with open('input.txt', 'r') as file:
    c = 0

    for line in file.readlines():
        line = line.replace('\n', '')

        if line:
            section_1, section_2 = line.split(',')
            section_1_start, section_1_end = section_1.split('-')
            section_2_start, section_2_end = section_2.split('-')
            # section_1_range = range(int(section_1_start), int(section_1_end) + 1)

            # if line == '9-99,51-77':
            #     print(section_1_start)
            #     print(section_1_end)
            #     print(section_2_start)
            #     print(section_2_end)

            # print(section_1_start <= section_2_start and section_1_end >= section_2_end)
            # print(section_2_start <= section_1_start and section_2_end >= section_1_end)

            # 2-8,3-9
            # 2-8,3-7

            # if the 1st assingment fully contains the 2st
            if int(section_1_start) <= int(section_2_start) and int(section_1_end) >= int(section_2_end):
                c += 1
                # print(line)
                continue

            # 6-6,4-6
            # 3-7,2-8

            # if the 2st assingment fully contains the 1st
            if int(section_2_start) <= int(section_1_start) and int(section_2_end) >= int(section_1_end):
                c += 1
                # print(line)
                continue

            # 6-6,6-6

    # print(c)
    print(c)

# 9-99,51-77

# 9-81,10-91

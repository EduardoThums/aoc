def check_overlap(section_1, section_2):
    section_1_start, section_1_end = section_1.split('-')
    section_2_start, section_2_end = section_2.split('-')

    return int(section_1_start) <= int(section_2_start) and int(section_1_end) >= int(section_2_start)


def main():
    with open('input.txt', 'r') as file:
        c = 0

        for line in file.readlines():
            line = line.replace('\n', '')

            if line:
                section_1, section_2 = line.split(',')

                if check_overlap(section_1, section_2) or check_overlap(section_2, section_1):
                    c += 1
                    continue

        print(c)


main()

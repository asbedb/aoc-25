def main():
    f_path = "../provided-files/day3.txt"
    rolling_joltage = 0
    try:
        with open(f_path, "r") as file:
            for line in file:
                cleaned_line = line.strip()
                line_length = len(cleaned_line)
                last_index = line_length - 1
                first_digit = 0
                first_pos = -1
                second_digit = 0
                for index, char in enumerate(cleaned_line):
                    if index == last_index:
                        continue
                    if char.isdigit():
                        num_char = int(char)
                        if num_char > first_digit:
                            first_digit = num_char
                            first_pos = index
                start_index_two = first_pos + 1
                remaining_line = cleaned_line[start_index_two:]
                for char in remaining_line:
                    if char.isdigit():
                        num_char = int(char)
                        if num_char > second_digit:
                            second_digit = num_char
                jolt_str = f"{first_digit}{second_digit}"
                rolling_joltage += int(jolt_str)
    except FileNotFoundError:
        print(f"Error: the file was not found")
    except Exception as e:
        print(f"An error occured: {e}")
    print(rolling_joltage)


if __name__ == "__main__":
    main()

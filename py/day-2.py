"""
-single line id input
-ranges are seperated by a comma `,`
- <first_id>-<last_id>
- invalid ID = repeated sequences (doesn't matter what length)
- ADD THE INVALID ID's TOGETHER
"""

# My first failed attempt lel
# def is_invalid_id(s):
#     L = len(s)
#     H = L/2
#     if L % 2 == 0:
#         return s[:int(H - 1)] == s[int(H + 1):]
#     else: 
#         return s[:int(H)] == s[int(H):]

def is_invalid_id(id_input):
    length = len(id_input)
    for size in range(1, length // 2 + 1):
        if length == 2 * size and id_input[:size] == id_input[size:]:
            return True
    return False

def main():
    f_path = "../provided-files/day2.txt"
    invalid_ids = 0
    try:
        with open(f_path, 'r') as file:
            instuction_set = file.readline().strip()
            all_options = instuction_set.split(",")
            for option in all_options:
                start, end = map(int, option.strip().split("-"))
                for number in range(start, end+ 1):
                    if is_invalid_id(str(number)):
                        invalid_ids += number
    except FileNotFoundError:
        print(f"Error: the file was not found")
    except Exception as e:
        print(f"An error occured: {e}")
    print(invalid_ids)

if __name__ == "__main__":
    main()
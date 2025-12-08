"""
- dial with one arrow on a circle
- around dial numbers 0 to 99 clockwise
- note with rotations (one per line)
- sequence order = <L for left or R for Right><number of turns>
- so if dial on zero and R1 then number = 99

The actual password is the number of times the dial is left 
pointing at 0 after any rotation in the sequence.
"""

def main():
    dial_pos = 50
    zero_count = 0
    f_path = "../provided-files/day1.txt"
    try:
        with open(f_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                stripped_line = line.strip() 
                first_char_stripped = stripped_line[0]
                rest_of_line = stripped_line[1:]
                dial_pos = (dial_pos + int(rest_of_line)) % 100 if first_char_stripped == "R" else (dial_pos - int(rest_of_line)) % 100
                if dial_pos == 0:
                    zero_count = zero_count + 1
    except FileNotFoundError:
        print(f"Error: the file was not found")
    except Exception as e:
        print(f"An error occured: {e}")
    print(zero_count)
if __name__ == "__main__":
    main()
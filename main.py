

def main():
    pass
    rec_file = open("sillyrec.txt", 'r')
    # read all the lines in
    all_lines = rec_file.readlines()
    # walk through entire file
    line_number =0
    for line in all_lines:
        line_number = line_number +1
        if line_number % 2 == 1:
            print(line)
#https://www.notboring.com/jokes/work/2.htm <-- website for letter of rec

main()
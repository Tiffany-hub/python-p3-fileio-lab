def write_file(file_name, file_content):
    with open(f'{file_name}.txt', 'w') as f :
        f.write(file_content)
        

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', 'a') as f:
        f.write(append_content)

def read_file(file_name):
    with open(f'{file_name}.txt', 'r') as f:
        return f.read()


if __name__ == "__main__":
    write_file(file_name = "logfile", file_content = "Log 1: 5 bananas added")
    append_file(file_name="logfile", append_content="\nLog 2: 3 bananas subtracted")
    content = read_file(file_name = "logfile")
    print(content)
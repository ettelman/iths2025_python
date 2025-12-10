from log_utils import parse_log_line

def main():
    line = "2025-02-22 AUTH failed login for user root"
    data = parse_log_line(line)

    print(data)

if __name__ == "__main__":
    main()
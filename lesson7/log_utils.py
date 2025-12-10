def parse_log_line(line):
    parts = line.split(" ")
    return {
        "timestamp":parts[0],
        "source": parts[1],
        "message":" ".join(parts[2:])
    }
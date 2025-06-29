import sys
from collections import Counter


def parse_log_line(line:str) ->dict:
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        return {}
    date, time, level, message = parts
    return {"date": date, "time": time, "level": level, "message": message}

def load_logs(file_path:str) -> list:
    logs = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                log = parse_log_line(line)
                if log:
                    logs.append(log)
    except FileNotFoundError:
        print(f" File '{file_path}' not found.")
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log["level"].lower()== level.lower()]

def count_logs_by_level(logs: list) -> dict:
    return dict(Counter(log["level"] for log in logs))

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17} | {count}")


def main():
    if len(sys.argv) < 2:
        print("Please specify the path to the log file as the first argument.")
        return
    file_path = sys.argv[1]
    logs = load_logs(file_path)

    if not logs:
        print("The log file is empty or does not contain valid entries.")
        return
    
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) == 3:
        level = sys.argv[2]
        filtered = filter_logs_by_level(logs, level)
        print(f"\nLog details for the level '{level.upper()}':")
        for log in filtered:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()
# A7 Task 5.py
# Electricity consumption analysis program


WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)
DELIMITER = ";"


def readFile(PFilename: str, PRows: list[str]) -> None:
    print(f'Reading file "{PFilename}".')
    PRows.clear()

    try:
        with open(PFilename, 'r', encoding="utf-8") as file:
            first_line = True
            for line in file:
                if first_line:
                    first_line = False
                    continue
                line = line.strip()
                if line == "":
                    continue
                PRows.append(line)
    except FileNotFoundError:
        print(f"Error! File {PFilename} not found")


def analyseData(PRows: list[str]) -> list[str]:
    # Gatherers
    daily_usage = {day: 0.0 for day in WEEKDAYS}
    daily_cost = {day: 0.0 for day in WEEKDAYS}
    for row in PRows:
     columns = row.split(DELIMITER)
     weekday = columns[2]
     consumption = float(columns[3])
     price = float(columns[4])
     if weekday not in daily_usage:
        continue
    daily_usage[weekday] += consumption
    daily_cost[weekday] += consumption * price

    results = []
    for day in WEEKDAYS:
        usage = daily_usage[day]
        cost = daily_cost[day]
        results.append( f" - {day} usage {usage:.2f} kWh, cost {cost:.2f} €")
    return results


def displayResults(PResults: list[str]) -> None:  # Print summary 
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for line in PResults:
        print(line)
    print("### Electricity consumption summary ###")


def main() -> None:
    print("Program starting.")
    PRows: list[str] = []
    PResults: list[str] = []
    filename = input("Insert filename: ")
    readFile(filename, PRows)
    print("Analysing timestamps.")
    PResults = analyseData(PRows)
    displayResults(PResults)
    PRows.clear()
    PResults.clear()
    return None


if __name__ == "__main__":
    main()  
    print("Program ending.") # A7 Task 5.py
# Electricity consumption analysis program


WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)
DELIMITER = ";"


def readFile(PFilename: str, PRows: list[str]) -> None:
    print(f'Reading file "{PFilename}".')
    PRows.clear()

    try:
        with open(PFilename, 'r', encoding="utf-8") as file:
            first_line = True
            for line in file:
                if first_line:
                    first_line = False
                    continue
                line = line.strip()
                if line == "":
                    continue
                PRows.append(line)
    except FileNotFoundError:
        print(f"Error! File {PFilename} not found")


def analyseData(PRows: list[str]) -> list[str]:
    # Gatherers
    daily_usage = {day: 0.0 for day in WEEKDAYS}
    daily_cost = {day: 0.0 for day in WEEKDAYS}
    for row in PRows:
     columns = row.split(DELIMITER)
     weekday = columns[2]
     consumption = float(columns[3])
     price = float(columns[4])
     if weekday not in daily_usage:
        continue
    daily_usage[weekday] += consumption
    daily_cost[weekday] += consumption * price

    results = []
    for day in WEEKDAYS:
        usage = daily_usage[day]
        cost = daily_cost[day]
        results.append( f" - {day} usage {usage:.2f} kWh, cost {cost:.2f} €")
    return results


def displayResults(PResults: list[str]) -> None:  # Print summary 
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for line in PResults:
        print(line)
    print("### Electricity consumption summary ###")


def main() -> None:
    print("Program starting.")
    PRows: list[str] = []
    PResults: list[str] = []
    filename = input("Insert filename: ")
    readFile(filename, PRows)
    print("Analysing timestamps.")
    PResults = analyseData(PRows)
    displayResults(PResults)
    PRows.clear()
    PResults.clear()
    return None


if __name__ == "__main__":
    main()  
    print("Program ending.") 

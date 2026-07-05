import json


INPUT_FILE = "raw_data.txt"
OUTPUT_FILE = "report.json"


def clean_text(text):
    """Remove extra spaces and convert to title case."""
    return " ".join(text.strip().split()).title()


records = []

with open(INPUT_FILE, "r", encoding="utf-8") as file:
    for line in file:

        line = line.strip()

        if not line:
            continue

        parts = [item.strip() for item in line.split(",")]

        # Skip invalid records
        if len(parts) != 4:
            continue

        name = clean_text(parts[0])

        try:
            age = int(parts[1])
        except ValueError:
            continue

        city = clean_text(parts[2])
        profession = clean_text(parts[3])

        record = {
            "name": name,
            "age": age,
            "city": city,
            "profession": profession
        }

        records.append(record)

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    json.dump(records, file, indent=4)

print("JSON report generated successfully!\n")
print(json.dumps(records, indent=4))

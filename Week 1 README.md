# Automated Multi-Format Report Generator

## Project Overview

This project reads an unorganized comma-separated text file, cleans and validates the data, and converts it into a structured JSON report using only Python's built-in libraries.

## Features

- Reads raw `.txt` files
- Removes extra whitespace
- Fixes inconsistent capitalization
- Skips invalid records
- Converts numeric fields
- Exports clean JSON

## Technologies Used

- Python
- json (built-in library)

## Files

- `generator.py` – Main Python program
- `raw_data.txt` – Sample raw input
- `report.json` – Generated JSON output

## Run

```bash
python generator.py

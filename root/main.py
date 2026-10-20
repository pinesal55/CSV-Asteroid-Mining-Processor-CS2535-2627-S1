
import csv

INPUT_FILE = "input_asteroid_data.csv"
OUTPUT_FILE = "output_asteroid_data.csv"

ORE_VALUE = 2
CRYSTAL_VALUE = 5
GAS_VALUE = 3

fieldnames = [
    "asteroid_id",
    "ore_units",
    "crystal_units",
    "gas_units",
    "total_units",
    "cargo_value"
]

# Read the input file and keep it open while processing
with open(INPUT_FILE, mode="r", newline="", encoding="utf-8") as input_file:
    reader = csv.DictReader(input_file)

    # Create a separate output file
    with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        # Process each asteroid while the input file is still open
        for row in reader:
            ore_units = int(row["ore_units"])
            crystal_units = int(row["crystal_units"])
            gas_units = int(row["gas_units"])

            total_units = ore_units + crystal_units + gas_units

            cargo_value = (
                ore_units * ORE_VALUE
                + crystal_units * CRYSTAL_VALUE
                + gas_units * GAS_VALUE
            )

            row["total_units"] = total_units
            row["cargo_value"] = cargo_value

            writer.writerow(row)

print(f"Processing complete! Results saved to {OUTPUT_FILE}")

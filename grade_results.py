"""
Utility script for taking a JSON output of grades for each student and
synthesizing them into a single CSV in the form:
<username>, <grade>
"""
import csv
import json
import os


def main():
    results_dir = "./results"
    result_files = [
        os.path.join(results_dir, f)
        for f in os.listdir(results_dir)
        if os.path.isfile(os.path.join(results_dir, f))
    ]

    with open('results.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for result_file in sorted(result_files):
            username = result_file.split("/")[-1].split(".")[0]
            file_path = result_file

            with open(file_path, "r") as json_handle:
                result_data = json.load(json_handle)
                csv_writer.writerow([username, result_data["grade"]])


if __name__ == "__main__":
    main()

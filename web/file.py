import csv

def save_to_file(jobs):
    with open("jobs.csv", "w", encoding="utf-8-sig", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["No", "제목", "회사", "지역", "Link"])

        for i, job in enumerate(jobs):
            csv_writer.writerow([i+1, job["title"], job["company"], job["location"], job["href"]])
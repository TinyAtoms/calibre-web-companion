import csv
from rich.console import Console
from rich.table import Column, Table
import subprocess
subprocess.run(["locust"])

def floatify(mystring):  # floatify probable floats
    return f"{float(mystring):3.3f}"


results = dict()
with open("calibre_stats.csv", "r") as cfile:
    reader = csv.reader(cfile, delimiter=",")
    for row in reader:
        if not len(row) or row[0] == "Type":
            continue
        results[row[0] + " " + row[1]] = {
            "median": floatify(row[4]),
            "avg": floatify(row[5]),
            "min": floatify(row[6]),
            "max": floatify(row[7]),
        }

console = Console()
table = Table(show_header=True, header_style="bold green")
table.add_column("Action/url")
table.add_column("min")
table.add_column("avg")
table.add_column("median")  # destination
table.add_column("max")  # source

for k, v in results.items():
    table.add_row(k, v["min"], v["avg"], v["median"], v["max"])
console.print(table)

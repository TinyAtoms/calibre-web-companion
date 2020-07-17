import csv


def floatify(mystring):  # floatify probable floats
    try:
        return f"{float(mystring):3.3f}"



results = dict() 
with open("calibre_stats.csv", "r") as cfile:
    reader = csv.reader(cfile, delimiter=",")
    for row in reader:
        if not len(row):
            continue
        results[action] = {
            "median" : floatify(row[4]),
            "avg" : floatify(row[5]),
            "min" : floatify(row[6]),
            "max" : floatify(row[7]),
        }


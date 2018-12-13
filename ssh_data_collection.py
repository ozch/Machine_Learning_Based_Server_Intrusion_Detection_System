import csv

csv_file = open('data/SSH.csv', 'w')
with csv_file:
    df=["is_private","is_failure","is_root","is_valid","no_failure","td","label"]
    writer = csv.DictWriter(csv_file, fieldnames=df)
    writer.writeheader()
    writer.writerow({"is_private":1 ,"is_failure":0 ,"is_root":0 ,"is_valid":1 ,"no_failure":0 ,"td":7789 ,"label":0 })
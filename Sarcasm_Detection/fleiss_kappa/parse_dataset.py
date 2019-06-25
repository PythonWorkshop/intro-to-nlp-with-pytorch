import csv
import json
import random

rating = ["yes","no"]
headlines = []
with open("dataset.json","r")  as f:
    lines = f.readlines()
    for line in lines:
        json_obj = json.loads(line)
        headlines.append(json_obj['headline'])

with open("rated.csv","w") as w:
    writer = csv.writer(w)
    for headline in headlines:
        row = []
        row.append([headline,random.choice(rating),random.choice(rating),random.choice(rating)])
        writer.writerows(row)
    

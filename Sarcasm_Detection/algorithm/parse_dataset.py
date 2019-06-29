import json
import csv
with open("train_set.json","r") as f:
    train_lines = f.readlines()

with open("test_set.json","r") as f:
    test_lines = f.readlines()

def write_dataset(filename,lines):
    with open(filename,"w") as w:
        writer = csv.writer(w)
        for line in lines:
            row = []
            line_json = json.loads(line)
            row.append([line_json["headline"],len(line_json["headline"]),line_json["is_sarcastic"]])
            writer.writerows(row)

write_dataset("train_set_v2.json",train_lines)
write_dataset("test_set_v2.json",test_lines)
import json

# Name der Dateien
input1_filename = "base.json"
input2_filename = "exotic.json"
output_filename = "config.json"

# Lese die Daten aus beiden Dateien ein
with open(input1_filename, "r") as f1, open(input2_filename, "r") as f2:
    data1 = json.load(f1)
    data2 = json.load(f2)

# Füge die flipRestrictions von data2 zu data1 hinzu
if "flipRestrictions" in data2:
    if "flipRestrictions" in data1:
        # merge
        restrictions1 = json.loads(data1["flipRestrictions"])
        restrictions2 = json.loads(data2["flipRestrictions"])
        merged_restrictions = restrictions1 + restrictions2
        data1["flipRestrictions"] = json.dumps(merged_restrictions)
    else:
        # ersetze
        data1["flipRestrictions"] = data2["flipRestrictions"]

# Speichere die kombinierten Daten in der Ausgabedatei
with open(output_filename, "w") as f_out:
    json.dump(data1, f_out, indent=4)

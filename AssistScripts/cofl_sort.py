import json

# Dateinamen definieren
input_filename = "Base.json"
output_filename = "config.json"

# JSON-Datei einlesen
with open(input_filename, "r") as input_file:
    data = json.load(input_file)

# Wert für den Schlüssel "flipRestrictions" als JSON-Objekt laden
flip_restrictions = json.loads(data["flipRestrictions"])

# Sortieren nach "tag"
flip_restrictions_sorted = sorted(flip_restrictions, key=lambda x: x.get("item", {}).get("tag", "").lower())

# Aktualisieren des ursprünglichen Datums mit den sortierten flipRestrictions
data["flipRestrictions"] = json.dumps(flip_restrictions_sorted)

# Speichern der sortierten Daten
with open(output_filename, "w") as output_file:
    json.dump(data, output_file)

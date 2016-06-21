import json

j_config = {}
j_config["exe"] = "Eradication.exe"
j_config["args"] = []
a1 = {"-C":"config.json"}
a2 = {"-I":"..\..\InputFiles"}
a3 = {"-O":"output2"}
j_config["args"].append(a1)
j_config["args"].append(a2)
j_config["args"].append(a3)
j_config["campaign"] = {}
j_config["campaign"]["base"] = "simple_outbreak.json"
j_interventions = []
j_interventions.append("bednet intervention")
j_interventions.append("spatial repellent")
j_config["campaign"]["interventions"] = j_interventions

with open ("emod_config.json", "w") as outfile:
    json.dump(j_config, outfile, indent=4, sort_keys=True)

p_config = None
with open("emod_config.json" , "r") as infile:
    p_config = json.loads(infile.read())

p_config["campaign"]["interventions"].append("chloroquine")

print p_config["campaign"]["interventions"] 
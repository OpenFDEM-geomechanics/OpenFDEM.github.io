name_list = [
    "of.history.pv.interval",
    "of.history.pv.dynamic.interval",
    "of.history.pv.field",
    "of.history.pv.fracture",
    "of.history.pv.cohesive",
    "of.history.pv.damage",
    "of.history.pv.ae",
]

for name in name_list:
    with open(f"{name}.rst", "w") as file:
        file.write(f"{name}\n")
        file.write("=" * len(name) + "\n\n")

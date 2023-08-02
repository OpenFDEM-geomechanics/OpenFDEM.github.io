name_list = [
    "of.DFN.connectivity",
    "of.DFN.group",
    "of.DFN.cohesive",
    "of.DFN.broken"
]

for name in name_list:
    with open(f"{name}.rst", "w") as file:
        file.write(f"{name}\n")
        file.write("=" * len(name) + "\n\n")


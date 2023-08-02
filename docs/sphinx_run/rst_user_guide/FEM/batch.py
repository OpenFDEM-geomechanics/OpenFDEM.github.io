name_list = [
    "of.import.FEM.nodal.coord",
    "of.import.FEM.nodal.coord0",
    "of.import.FEM.nodal.velocity",
    "of.import.FEM.nodal.groups",
    "of.import.FEM.edge.groups",
    "of.import.FEM.element.groups",
    "of.import.FEM.element.connectivity",
]

for name in name_list:
    with open(f"{name}.rst", "w") as file:
        file.write(f"{name}\n")
        file.write("=" * len(name) + "\n\n")


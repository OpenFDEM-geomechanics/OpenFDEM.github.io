name_list = [
    "of.mesh.insert",
    "of.mesh.insert.dfn",
    "of.mesh.voronoi",
    "of.mesh.split",
    "of.mesh.bary",
    "of.mesh.RG",
    "of.mesh.RGB",
    "of.mesh.NVB",
    "of.mesh.baryGB",

]

for name in name_list:
    with open(f"{name}.rst", "w") as file:
        file.write(f"{name}\n")
        file.write("=" * len(name) + "\n\n")

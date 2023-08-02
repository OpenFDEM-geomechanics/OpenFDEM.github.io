name_list = [
    "of.geometry.square",
    "of.geometry.cut.square",
    "of.geometry.remove.square",
    "of.geometry.circle",
    "of.geometry.cut.circle",
    "of.geometry.remove.circle",
    "of.geometry.ellipse",
    "of.geometry.cut.ellipse",
    "of.geometry.remove.ellipse",
    "of.geometry.polygon",
    "of.geometry.cut.polygon",
    "of.geometry.remove.polygon",
    "of.geometry.table",
    "of.geometry.cut.table",
    "of.geometry.remove.table",
    "of.geometry.domain",
    "of.geometry.cut.joint",
    "of.geometry.cut.jset",
    "of.geometry.cut.DFN",
    "of.geometry.cut.arc",
    "of.geometry.minsize",
    "of.geometry.minangle",
    "of.geometry.iteration",
    "of.geometry.group",
    "of.geometry.mesh.size",
    "of.geometry.recombine",
    "of.geometry.mesh",
    "of.geometry.mesh.write",

]

for name in name_list:
    with open(f"{name}.rst", "w") as file:
        file.write(f"{name}\n")
        file.write("=" * len(name) + "\n\n")

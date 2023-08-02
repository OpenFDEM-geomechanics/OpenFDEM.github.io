name_list = [
    "of.boundary.nodal",
    "of.boundary.nodal.force",
    "of.boundary.nodal.velocity",
    "of.boundary.nodal.inivelocity",
    "of.boundary.nodal.acceleration",
    "of.boundary.nodal.clear",
    "of.boundary.edge.force",
    "of.boundary.edge.velocity",
    "of.boundary.edge.inivelocity",
    "of.boundary.edge.acceleration",
    "of.boundary.edge.clear",
    "of.boundary.element.stress",
    "of.boundary.element.stress.xgrad",
    "of.boundary.element.stress.ygrad",
    "of.boundary.element.clear",
    "of.boundary.blast",

]

for name in name_list:
    with open(f"{name}.rst", "w") as file:
        file.write(f"{name}\n")
        file.write("=" * len(name) + "\n\n")



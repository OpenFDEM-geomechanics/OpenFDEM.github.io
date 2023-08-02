name_list = [
    "of.group.nodal",
    "of.group.edge",
    "of.group.element",
    "of.group.cohelement",
    "of.group.nodal.from.element",
    "of.group.edge.from.element",
    "of.group.edge.from.cohelement",
    "of.group.edge.from.dfn",
    "of.group.edge.cohelement.from.dfn",
    "of.group.cohelement.from.gbm",
    "of.group.nodal.bool.union",
    "of.group.nodal.bool.intersect",
    "of.group.nodal.bool.subtract",
    "of.group.edge.bool.union",
    "of.group.edge.bool.intersect",
    "of.group.edge.bool.subtract",
    "of.group.element.bool.union",
    "of.group.element.bool.intersect",
    "of.group.element.bool.subtract",
    "of.group.cohelement.bool.union",
    "of.group.cohelement.bool.intersect",
    "of.group.cohelement.bool.subtract",

]

for name in name_list:
    with open(f"{name}.rst", "w") as file:
        file.write(f"{name}\n")
        file.write("=" * len(name) + "\n\n")

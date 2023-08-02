name_list = [
    "of.mat.element",
    "of.mat.cohesive",
    "of.mat.contact",
    "of.mat.hydro.matrix",
    "of.mat.hydro.fracture",
    "of.mat.mpm.fluid",
    "of.mat.mpm.solid",
    "of.mat.hydro.fluid",
    "of.mat.hydro.gas",
    "of.mat.nonlocal",
    "of.mat.thermal",
]

for name in name_list:
    with open(f"{name}.rst", "w") as file:
        file.write(f"{name}\n")
        file.write("=" * len(name) + "\n\n")

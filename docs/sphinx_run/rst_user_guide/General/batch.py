name_list = [
    "of.console.interval",
    "of.damp.global",
    "of.finalize",
    "of.import",
    "of.import.table",
    "of.log.interval",
    "of.new",
    "of.restore",
    "of.save",
    "of.save.FEM",
    "of.set.config",
    "of.set.contact",
    "of.set.debug",
    "of.set.GBM",
    "of.set.gravity",
    "of.set.large",
    "of.set.massscale",
    "of.set.module",
    "of.set.omp",
    "of.set.result",
    "of.set.rgbm",
    "of.solve",
    "of.step",
    "of.timestep",

]

for name in name_list:
    with open(f"{name}.rst", "w") as file:
        file.write(f"{name}\n")
        file.write("=" * len(name) + "\n\n")


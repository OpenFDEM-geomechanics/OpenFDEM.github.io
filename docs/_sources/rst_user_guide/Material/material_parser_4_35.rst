Material parser overview (4.35)
===============================

The current parser accepts the following top-level material entries:

- ``of.mat.element``
- ``of.mat.rockbolt``
- ``of.mat.particle``
- ``of.mat.cohesive``
- ``of.mat.contact``
- ``of.mat.hydro.matrix``
- ``of.mat.hydro.fracture``
- ``of.mat.mpm.fluid``
- ``of.mat.mpm.solid``
- ``of.mat.hydro.fluid``
- ``of.mat.hydro.gas``
- ``of.mat.nonlocal`` and the source-compatible spelling ``of.mat.nonlcoal``
- ``of.mat.thermal``
- ``of.mat.moisture``
- ``of.mat.hysteretic``

Most entries first read a group tag and then delegate the material-model
parameters to the solid, cohesive, hydro, thermal or moisture material
module. The old pages should therefore be used together with the current
model-registration code; this overview does not claim that every old model
keyword or parameter range remains valid.

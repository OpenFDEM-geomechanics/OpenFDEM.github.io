Irregular Deformable Cluster DEM
=================================

An irregular deformable particle can be represented as a cluster of
interacting constituent particles. The cluster geometry captures a
non-circular or otherwise irregular outline, while relative motion among its
constituents allows the aggregate to deform. If internal bonds soften or fail,
the particle can also fragment. This differs from a rigid clump, whose
constituents retain fixed relative positions and whose overall shape cannot
change.

OpenFDEM's project description identifies realistic particles as rigid or
deformable, notes overlapping-particle and Fourier-Voronoi-based shape
generation, and states that particle breakage is possible. The bonded-cluster
equations below are a general theoretical description; the exact internal
representation, bond law, and breakage criterion depend on the selected model.

Cluster kinematics and force balance
-------------------------------------

For a cluster with constituent particles :math:`a=1,\ldots,N_c`, each
constituent obeys its own translational and rotational balances,

.. math::

   m_a\dot{\mathbf{v}}_a
   =\sum_{b}\mathbf{F}_{ab}^{\mathrm{int}}
   +\sum_{c}\mathbf{F}_{ac}^{\mathrm{ext}}
   +m_a\mathbf{g},

.. math::

   \mathbf{I}_a\dot{\boldsymbol{\omega}}_a
   +\boldsymbol{\omega}_a\times
   (\mathbf{I}_a\boldsymbol{\omega}_a)
   =\sum_b\mathbf{M}_{ab}^{\mathrm{int}}
   +\sum_c\mathbf{M}_{ac}^{\mathrm{ext}},

where :math:`\mathbf{F}^{\mathrm{int}}` and
:math:`\mathbf{M}^{\mathrm{int}}` are forces and moments transmitted by
internal contacts or bonds, while the external terms arise from other
particles, boundaries, and applied loads. If all internal bonds remain intact
and infinitely stiff, relative constituent motion is suppressed and the
cluster approaches rigid-clump behavior. Finite bond stiffness permits
deformation; bond damage or failure permits irreversible shape change and
fragmentation.

Internal bond response and breakage
-----------------------------------

A simple bonded-contact idealization relates the local normal and tangential
relative displacements :math:`\delta_n` and :math:`\boldsymbol{\delta}_t` to
trial bond forces through

.. math::

   F_n^{\mathrm{trial}}=k_n^b\delta_n,
   \qquad
   \mathbf{F}_t^{\mathrm{trial}}=k_t^b\boldsymbol{\delta}_t,

where :math:`k_n^b` and :math:`k_t^b` are bond stiffnesses. A chosen strength
criterion may trigger damage when the normal or shear traction reaches its
corresponding tensile or shear capacity. After damage, the transmitted force
is reduced according to the selected softening law; after complete failure,
the interface no longer carries cohesive tension or shear, although ordinary
compressive contact and friction may remain. These equations illustrate the
mechanism and are not a claim about one specific OpenFDEM bond implementation.

Macroscopic response and calibration
------------------------------------

The response of an irregular cluster assembly emerges from both external
particle contacts and internal deformation. Cluster geometry affects packing,
contact orientation, and interlocking; constituent size and bond properties
affect the effective stiffness, strength, and breakage pattern. Resolution
should be adequate to represent the target particle shape and expected
deformation modes. Calibration should consider bulk observables such as
packing density, stress-strain response, peak strength, dilation, and fragment
size distribution, rather than fitting only individual bond parameters.

This cluster approach provides a mesoscale compromise: it can represent
particle-scale deformation and breakage without resolving a continuum mesh
inside every grain. Predictions remain dependent on the chosen cluster
discretization, contact law, bond law, and numerical time step.

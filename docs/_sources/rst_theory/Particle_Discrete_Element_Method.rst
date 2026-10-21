Particle Discrete Element Method (pDEM)
========================================

===================================================================

Rigid Particle DEM
------------------


The rigid-particle discrete element method (DEM) models a particulate
assembly as individual bodies whose shapes do not deform, while their
translations, rotations, contacts, and possible bonds evolve in time. It is
well suited to granular packing, impact, flow, and compression problems in
which bulk behavior emerges from particle-scale interactions. OpenFDEM
describes its pDEM module as supporting particle packing, kinematics,
collision, and linear, Hertz, cohesive-bond, and rotation-resistance contact
models.

Particle motion
~~~~~~~~~~~~~~~~~~~~

For particle :math:`i` with mass :math:`m_i`, center position
:math:`\mathbf{x}_i`, and translational velocity :math:`\mathbf{v}_i`, the
translational equation of motion is

.. math::

   m_i\dot{\mathbf{v}}_i
   =\sum_{c\in i}\mathbf{F}_{ic}+m_i\mathbf{g}+\mathbf{F}_i^{\mathrm{ext}},

where :math:`\mathbf{F}_{ic}` are contact or bond forces,
:math:`\mathbf{g}` is gravity, and :math:`\mathbf{F}_i^{\mathrm{ext}}` is
other applied loading. Rotation follows the angular-momentum balance

.. math::

   \mathbf{I}_i\dot{\boldsymbol{\omega}}_i
   +\boldsymbol{\omega}_i\times
   (\mathbf{I}_i\boldsymbol{\omega}_i)
   =\sum_{c\in i}\mathbf{M}_{ic}+\mathbf{M}_i^{\mathrm{ext}},

where :math:`\mathbf{I}_i` is the particle inertia tensor,
:math:`\boldsymbol{\omega}_i` is angular velocity, and :math:`\mathbf{M}`
denotes contact, bond, or applied moments. In two-dimensional calculations,
the rotational equation reduces to the out-of-plane scalar form.

Contact and friction
~~~~~~~~~~~~~~~~~~~~

For a pair of touching particles, the contact force is commonly resolved into
normal and tangential components,
:math:`\mathbf{F}_c=F_n\mathbf{n}+\mathbf{F}_t`, where :math:`\mathbf{n}` is
the contact normal. A linear elastic-frictional model uses the overlap
:math:`\delta_n` to compute a trial normal force, for example

.. math::

   F_n^{\mathrm{trial}}=k_n\delta_n-c_n v_n,
   \qquad
   |\mathbf{F}_t|\leq\mu_f F_n,

where :math:`k_n` is normal stiffness, :math:`c_n` is a normal damping
coefficient, :math:`v_n` is the relative normal velocity, and :math:`\mu_f`
is the friction coefficient. A tangential spring tracks relative slip, with
the trial force projected back to the Coulomb limit when sliding occurs. In
Hertz-type contact, the normal force instead depends nonlinearly on overlap.
The exact force law, damping, and friction update are constitutive choices;
they should be selected for the particle material and the intended time scale.

Time integration and interpretation
~~~~~~~~~~~~~~~~~~~~

DEM commonly advances the particle equations explicitly. The stable time step
must resolve the shortest relevant contact oscillation, which is controlled
by particle mass or inertia and contact stiffness. Increasing stiffness
reduces overlap but also decreases the stable time step. Contact stiffness,
damping, and friction therefore affect both numerical cost and the effective
macroscopic response and should be calibrated rather than treated as arbitrary
numerical constants.

Because particle shapes are fixed in rigid DEM, particle-scale deformation
and fracture are not resolved within a body. They can be represented
approximately by bonded particle assemblies or by the deformable-cluster
approach described in the following section.

===================================================================

Irregular Deformable Cluster DEM
--------------------------------


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
~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~

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


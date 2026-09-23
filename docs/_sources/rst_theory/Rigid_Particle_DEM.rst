Rigid Particle DEM
==================

The rigid-particle discrete element method (DEM) models a particulate
assembly as individual bodies whose shapes do not deform, while their
translations, rotations, contacts, and possible bonds evolve in time. It is
well suited to granular packing, impact, flow, and compression problems in
which bulk behavior emerges from particle-scale interactions. OpenFDEM
describes its pDEM module as supporting particle packing, kinematics,
collision, and linear, Hertz, cohesive-bond, and rotation-resistance contact
models.

Particle motion
---------------

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
--------------------

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
------------------------------------

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
approach described in :doc:`Irregular_Deformable_Cluster_DEM`.

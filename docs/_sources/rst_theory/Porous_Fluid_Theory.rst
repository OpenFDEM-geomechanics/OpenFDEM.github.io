Porous Fluid
============

Porous-fluid theory describes fluid transport through the connected pore
space of a permeable solid. At the continuum scale, the pore geometry is
represented by porosity and permeability rather than by resolving each pore.
The formulation below is for a saturated, single-phase Newtonian fluid; it is
a general porous-media model and does not imply that every coupling term is
active in every OpenFDEM analysis.

Darcy flux
----------

For slow viscous flow through a porous medium, the volumetric Darcy flux is

.. math::

   \mathbf{q}=-\frac{\mathbf{k}}{\mu}
   \left(\nabla p-\rho\mathbf{g}\right),

where :math:`\mathbf{q}` is the volume of fluid crossing unit bulk area per
unit time, :math:`\mathbf{k}` is the intrinsic permeability tensor,
:math:`\mu` is dynamic viscosity, :math:`p` is pore pressure, :math:`\rho` is
fluid density, and :math:`\mathbf{g}` is gravitational acceleration. The
minus sign makes flow proceed down the hydraulic-potential gradient. For
isotropic material, :math:`\mathbf{k}=k\mathbf{I}`. Darcy's law assumes that
inertial effects are small; high-speed flow may require a non-Darcy relation.

Mass conservation and pressure diffusion
-----------------------------------------

The local fluid mass balance is

.. math::

   \frac{\partial (\phi\rho)}{\partial t}
   +\nabla\cdot(\rho\mathbf{q})=m_f,

where :math:`\phi` is porosity and :math:`m_f` is a mass source per unit bulk
volume. For slightly compressible fluid and solid constituents, a commonly
used pressure form is

.. math::

   S_p\frac{\partial p}{\partial t}
   +\alpha_B\frac{\partial\varepsilon_v}{\partial t}
   +\nabla\cdot\mathbf{q}=Q_f,

where :math:`S_p` is the pressure-storage coefficient,
:math:`\alpha_B` is the Biot coefficient, :math:`\varepsilon_v` is volumetric
strain, and :math:`Q_f` is a volumetric fluid source. The strain term accounts
for the change in pore volume caused by deformation; its sign follows the
tension-positive strain convention. If deformation is not coupled, this term
is omitted. Combining this balance with Darcy's law gives the pressure
diffusion equation

.. math::

   S_p\frac{\partial p}{\partial t}
   +\alpha_B\frac{\partial\varepsilon_v}{\partial t}
   -\nabla\cdot\left[
   \frac{\mathbf{k}}{\mu}(\nabla p-\rho\mathbf{g})\right]=Q_f.

For constant properties, no gravity, and no deformation coupling, this reduces
to a diffusion equation for pore pressure. The permeability tensor controls
the ease and direction of flow, while storage controls the rate at which
pressure responds to fluid injection, production, or boundary loading.

Pressure initial and boundary conditions
----------------------------------------

A transient problem requires an initial pressure field. Typical boundary
conditions prescribe pore pressure, normal fluid flux, a source or sink, or
no-flow on an impermeable boundary. Prescribed pressure represents connection
to a pressure-controlled reservoir; prescribed flux represents a specified
injection or discharge rate. These conditions should be applied consistently
with the sign convention used for :math:`\mathbf{q}` and :math:`Q_f`.

The equations above assume a continuum representative volume and single-phase
flow. When two immiscible fluids occupy the pore space, saturation-dependent
relative permeability and capillary pressure are needed; see
:doc:`Two_Phase_Fluid_Theory`.

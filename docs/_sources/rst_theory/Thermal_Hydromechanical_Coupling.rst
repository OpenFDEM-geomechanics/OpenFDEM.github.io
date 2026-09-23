Thermal-Hydromechanical Coupling
================================

Thermal-hydromechanical (THM) coupling describes the interaction between
temperature, fluid pressure and flow, and deformation. Heating or cooling
changes the temperature field and produces thermal strain; deformation can in
turn change fracture aperture and fluid storage, while fluid flow transports
heat. The relative importance of these feedbacks depends on the material,
loading, and time scale.

The high-temperature rock treatment described in the accompanying reference
uses a one-way thermo-mechanical approximation: temperature drives thermal
stress, while deformation has a negligible effect on heat transfer. The
equations below present a broader THM framework and should be read as governing
principles; particular constitutive laws, coupling terms, and sign conventions
depend on the model setup.

Heat transport
--------------

In a fluid-bearing porous medium, heat is conducted through the solid-fluid
mixture and may also be carried by moving fluid. A common local energy balance
is

.. math::

   C_{\mathrm{eff}}\frac{\partial T}{\partial t}
   + \rho_f c_f\,\mathbf{v}\cdot\nabla T
   = \nabla\cdot(\mathbf{K}_{\mathrm{eff}}\nabla T) + Q,

where :math:`T` is temperature, :math:`C_{\mathrm{eff}}` is the effective
volumetric heat capacity, :math:`\rho_f` and :math:`c_f` are the fluid density
and specific heat, :math:`\mathbf{v}` is the Darcy velocity,
:math:`\mathbf{K}_{\mathrm{eff}}` is the effective thermal-conductivity
tensor, and :math:`Q` is a volumetric heat source. The advection term may be
omitted when fluid transport is absent or negligible. In an impermeable solid,
this reduces to transient matrix heat conduction.

Fluid flow and pressure
-----------------------

For a single-phase fluid under Darcy flow, the Darcy velocity can be written
as

.. math::

   \mathbf{v}=-\frac{\mathbf{k}}{\mu_f}
   \left(\nabla p-\rho_f\mathbf{g}\right),

where :math:`\mathbf{k}` is intrinsic permeability,
:math:`\mu_f` is dynamic viscosity, :math:`p` is pore pressure, and
:math:`\mathbf{g}` is gravitational acceleration. A simplified fluid mass
balance is

.. math::

   S\frac{\partial p}{\partial t}
   + \alpha_B\frac{\partial \varepsilon_v}{\partial t}
   + \nabla\cdot\mathbf{v}=q_f,

where :math:`S` is fluid-storage capacity, :math:`\alpha_B` is the Biot
coefficient, :math:`\varepsilon_v` is volumetric strain, and :math:`q_f` is a
fluid source per unit bulk volume. This form illustrates pressure-deformation
coupling; compressibility, temperature-dependent properties, and fracture
storage can require additional terms.

Thermal and poroelastic deformation
-----------------------------------

For small strains, an isotropic thermal strain is

.. math::

   \boldsymbol{\varepsilon}_{\mathrm{th}}
   =\alpha_T(T-T_0)\mathbf{I},

where :math:`\alpha_T` is the linear thermal-expansion coefficient, :math:`T_0`
is a reference temperature, and :math:`\mathbf{I}` is the identity tensor. A
representative linear poroelastic stress relation, with tension-positive stress
and compression-positive pore pressure, is

.. math::

   \boldsymbol{\sigma}
   =\mathsf{C}:
   \left(\boldsymbol{\varepsilon}-\boldsymbol{\varepsilon}_{\mathrm{th}}\right)
   -\alpha_B p\mathbf{I},

where :math:`\mathsf{C}` is the elastic stiffness tensor and
:math:`\boldsymbol{\varepsilon}` is total strain. Under idealized complete
restraint of an isotropic solid, the thermal stress increment is hydrostatic
and has magnitude :math:`3K\alpha_T\Delta T`, where :math:`K` is the bulk
modulus. The actual stress state depends on constraints, geometry, and
constitutive assumptions; this limiting expression is not a general plane-
strain formula.

In fractured media, the coupling may also occur through deformation-dependent
fracture aperture and permeability. These feedbacks connect the thermal,
hydraulic, and mechanical fields and can be important even when the intact
matrix is treated as impermeable.

Thermal Transfer
================

===================================================================

Matrix Thermal
--------------


Matrix thermal transfer describes heat storage and conduction within the
intact solid material. Temperature gradients drive heat from warmer regions
toward cooler regions, while heat sources, boundary conditions, and material
properties determine the transient temperature field.

Fourier's law
~~~~~~~~~~~~~~~~~~~~

The conductive heat-flux density is given by Fourier's law:

.. math::

   \mathbf{q}=-\mathbf{K}\nabla T,

where :math:`\mathbf{q}` is heat flux per unit area, :math:`T` is temperature,
and :math:`\mathbf{K}` is the thermal-conductivity tensor. The negative sign
indicates that heat flows down the temperature gradient. For a two-dimensional
domain, :math:`\nabla T=(\partial T/\partial x,\,\partial T/\partial y)`.
For an isotropic material, :math:`\mathbf{K}=k\mathbf{I}`, where :math:`k` is
the scalar thermal conductivity.

Energy balance
~~~~~~~~~~~~~~~~~~~~

For a stationary solid with constant density and specific heat capacity, local
energy conservation is

.. math::

   \rho C_p\frac{\partial T}{\partial t}
   +\nabla\cdot\mathbf{q}=Q,

where :math:`\rho` is mass density, :math:`C_p` is specific heat capacity,
and :math:`Q` is the volumetric heat-generation rate. Combining this balance
with Fourier's law gives

.. math::

   \rho C_p\frac{\partial T}{\partial t}
   =\nabla\cdot(\mathbf{K}\nabla T)+Q.

For homogeneous isotropic material with constant :math:`k`, this becomes

.. math::

   \frac{\partial T}{\partial t}
   =\frac{k}{\rho C_p}\nabla^2T+\frac{Q}{\rho C_p}.

The thermal diffusivity :math:`a_T=k/(\rho C_p)` measures how quickly
temperature disturbances spread through the matrix. If properties vary with
temperature or position, the divergence form should be retained rather than
replacing it with :math:`k\nabla^2T`.

Initial and boundary conditions
~~~~~~~~~~~~~~~~~~~~

Transient conduction requires an initial temperature field
:math:`T(\mathbf{x},0)=T_0(\mathbf{x})`. Common boundary conditions include a
prescribed temperature, a prescribed normal heat flux
:math:`-\mathbf{n}\cdot\mathbf{K}\nabla T`, or an exchange condition with the
surrounding environment. These conditions define how the matrix receives or
loses heat and should be consistent with the physical heating or cooling
process being represented.

The equations above assume a continuum matrix and do not by themselves
represent heat exchange across a discontinuity. Heat transfer between
separated blocks or across a fracture is described by the contact and fracture
thermal-resistance models, respectively.

Fracture Heat Resistance
~~~~~~~~~~~~~~~~~~~~


A fracture interrupts direct heat conduction through the intact matrix. Heat
may still cross the discontinuity through gas, liquid, or solid material in the
fracture, as well as through microscopic asperity contacts between its faces.
These mechanisms can be represented by an effective thermal resistance.

Series-resistance model
~~~~~~~~~~~~~~~~~~~~

Consider a fracture of aperture :math:`b` filled with a material of thermal
conductivity :math:`k_f`. For one-dimensional steady conduction normal to the
fracture, the resistance per unit area of the filling layer is

.. math::

   R''_{f}=\frac{b}{k_f}.

If the two fracture faces also have interfacial resistances
:math:`R''_{c,1}` and :math:`R''_{c,2}`, the total resistance per unit area is

.. math::

   R''_{\mathrm{tot}}=R''_{c,1}+\frac{b}{k_f}+R''_{c,2}.

The corresponding effective conductance is
:math:`h_f=1/R''_{\mathrm{tot}}`, and the heat flux from side 1 to side 2 is

.. math::

   q''_{1\rightarrow2}
   =h_f(T_1-T_2)
   =\frac{T_1-T_2}{R''_{\mathrm{tot}}}.

Here :math:`T_1` and :math:`T_2` are the temperatures on the opposing sides of
the fracture. For a fracture with negligible filling-layer resistance,
:math:`b/k_f` may be omitted; for a dry, open fracture, the effective
conductance can instead be calibrated to account for gas conduction and
radiation if those mechanisms are included in the intended model.

Interpretation and assumptions
~~~~~~~~~~~~~~~~~~~~

The series model assumes heat flows approximately normal to a locally planar
fracture and that the layer and interface resistances act in series. The
resistance has units of :math:`\mathrm{m^2\,K/W}`, while conductance has units
of :math:`\mathrm{W/(m^2\,K)}`. For a contact area :math:`A`, the total heat
transfer rate is :math:`\dot Q=Aq''_{1\rightarrow2}`. A larger aperture or
lower filling conductivity increases the layer resistance and reduces heat
transfer, all else being equal.

This effective fracture resistance represents heat transmission across the
fracture itself. It is distinct from the contact-thermal exchange law used
when two discrete elements or blocks are in thermal contact. In a numerical
model, the effective conductance should reflect the chosen representation so
that fracture resistance and contact resistance are not inadvertently counted
twice.

===================================================================

Contact Thermal
---------------


Contact thermal transfer exchanges heat between the surfaces of two discrete
elements or blocks in contact. It provides a thermal connection across a
mechanical contact and is commonly modeled with a conductance proportional to
the temperature difference across the interface.

Interface law
~~~~~~~~~~~~~~~~~~~~

Let :math:`\Gamma_c` denote the active contact interface, and let :math:`T_t`
and :math:`T_c` be the temperatures on the target and contactor sides. The
normal heat flux from target to contactor is

.. math::

   q_{t\rightarrow c}=h_c(T_t-T_c),

where :math:`h_c` is the thermal contact conductance. The heat-transfer rate
over the interface is

.. math::

   \dot Q_{t\rightarrow c}
   =\int_{\Gamma_c}h_c(T_t-T_c)\,\mathrm{d}\Gamma.

For a uniform conductance and temperature difference over an interface of
area :math:`A_c`, this reduces to
:math:`\dot Q_{t\rightarrow c}=h_cA_c(T_t-T_c)`. In a two-dimensional model,
the measure :math:`\mathrm{d}\Gamma` is a boundary length and the out-of-plane
thickness must be included if a three-dimensional heat rate is required.

Energy conservation and interpretation
~~~~~~~~~~~~~~~~~~~~

The equal-and-opposite heat rate is applied to the other body:

.. math::

   \dot Q_{c\rightarrow t}=-\dot Q_{t\rightarrow c}.

Thus, contact exchange redistributes energy between the bodies but does not
create or remove energy from the pair. If :math:`T_t>T_c` and :math:`h_c>0`,
heat flows from the target to the contactor. A larger conductance approaches
the perfect-contact limit, while a small conductance represents a more
thermally resistive interface. The conductance may be prescribed or calibrated
as an effective parameter; its dependence on contact pressure, roughness,
aperture, and interface material is model-specific.

Contact thermal transfer applies only where a contact interface is defined.
Heat transfer across an open fracture or a gap requires a fracture-resistance
or other gap-transfer model. Care is needed to avoid applying both laws to the
same interface unless their resistances have been intentionally combined.

Thermal-Hydromechanical Coupling
--------------------------------


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
~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~

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


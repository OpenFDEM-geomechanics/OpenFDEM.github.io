Fluid Transport
===============

===================================================================

Fracture Fluid
--------------


When subjected to explosive loading, the rock mass experiences the rapid
propagation of stress waves radiating outward from the blast hole. As the
waves travel and dissipate, radial fractures form, and the blasting gas
infiltrates the newly formed cracks, driving their secondary extension and
ultimately giving rise to a well-connected fracture network. In OpenFDEM, the
fracture geometry provides the flow domain through which the fluid (gas or
liquid) travels.

Fracture aperture
~~~~~~~~~~~~~~~~~~~~

Before rock failure occurs, the fluid is assumed to be unable to penetrate the
intact medium. Once the cohesive elements connecting adjacent solid elements
exceed their strength limit, they separate and become failed cohesive
elements. The intact rock blocks remain impermeable, so the fluid can only
flow through these fracture paths. The fracture aperture of each element, which
acts as the hydraulic opening, directly controls the fluid volume within the
flow domain. The aperture is evaluated using

.. math::
    :nowrap:

    \[a=\begin{cases}
    a_{\min}, & o_n+a_0<a_{\min}\\
    o_n+a_0, & a_{\min}<o_n+a_0<a_{\max}\\
    a_{\max}, & o_n+a_0>a_{\max}\\
    \end{cases} \tag{1}\]

where :math:`a_0` denotes the initial fracture aperture, :math:`a_{\max}` and
:math:`a_{\min}` represent its upper and lower bounds, respectively, and
:math:`o_n\left( n=1,2,3 \right)` is the aperture obtained from the Gauss
points along the adjacent edges shared between the fracture and neighboring
solid elements.

Fracture volume
~~~~~~~~~~~~~~~~~~~~

The fluid volume within each channel is calculated as

.. math::
    V_{channel,j}=\int_{\varGamma _n}{N_ga}\,ds \tag{2}

where :math:`N_g` denotes the shape function of the Gauss point, and :math:`a`
represents the aperture at a specific Gauss point within a channel. The fluid
volume of each cavity is determined by the volumes of the channels connected
to it. The total fracture volume of a cavity is obtained by aggregating the
nodal fracture volumes of all cohesive elements contained within it

.. math::
    V_{cavity}=\frac{1}{M}\oint_n{\int_{\varGamma _n}{N_ga}}\,ds \tag{3}

where :math:`n` denotes the number of channels connected to the cavity, and
:math:`M` is half the number of nodes in a single channel.

.. figure:: ../_static/Theory/gas_flow_process.png
    :alt: Fracture flow process
    :width: 45%
    :align: center

    Figure 1. Fluid flow through the fracture network formed by failed
    cohesive elements.

.. figure:: ../_static/Theory/gas_fracture_aperture.png
    :alt: Fracture unit opening and channel volume
    :width: 41%
    :align: center

    Figure 2. Fracture unit opening and channel volume.

.. figure:: ../_static/Theory/gas_flow_cavity.png
    :alt: Schematic of the flow cavity
    :width: 41%
    :align: center

    Figure 3. Schematic of the flow cavity comprising Nodes 1-6.

===================================================================

Porous Fluid
------------


Porous-fluid theory describes fluid transport through the connected pore
space of a permeable solid. At the continuum scale, the pore geometry is
represented by porosity and permeability rather than by resolving each pore.
The formulation below is for a saturated, single-phase Newtonian fluid; it is
a general porous-media model and does not imply that every coupling term is
active in every OpenFDEM analysis.

Darcy flux
~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~

A transient problem requires an initial pressure field. Typical boundary
conditions prescribe pore pressure, normal fluid flux, a source or sink, or
no-flow on an impermeable boundary. Prescribed pressure represents connection
to a pressure-controlled reservoir; prescribed flux represents a specified
injection or discharge rate. These conditions should be applied consistently
with the sign convention used for :math:`\mathbf{q}` and :math:`Q_f`.

The equations above assume a continuum representative volume and single-phase
flow. The two-phase extension is presented in the next section.

===================================================================

Two-Phase Fluid
---------------


Two-phase porous flow describes two immiscible fluids, such as water and gas
or water and oil, sharing the same pore space. Because both phases compete for
the available pores, each phase's mobility depends on saturation. The
equations below give the standard continuum formulation; they do not prescribe
a particular relative-permeability curve or imply that this formulation is
used by every OpenFDEM fluid solver.

Saturation and capillary pressure
~~~~~~~~~~~~~~~~~~~~

For a two-phase system, the phase saturations satisfy

.. math::

   S_w+S_n=1,

where :math:`S_w` and :math:`S_n` are the wetting- and non-wetting-phase
saturations. Capillary pressure is the pressure difference between the phases,
conventionally defined as

.. math::

   p_c(S_w)=p_n-p_w,

where :math:`p_w` and :math:`p_n` are the wetting- and non-wetting-phase
pressures. A constitutive relation :math:`p_c(S_w)` closes the pressure-
saturation relation and reflects pore-scale interface and wettability effects.

Phase-specific Darcy law and mass balance
~~~~~~~~~~~~~~~~~~~~

The Darcy flux for phase :math:`\alpha\in\{w,n\}` is

.. math::

   \mathbf{q}_{\alpha}
   =-\frac{\mathbf{k}\,k_{r\alpha}(S_\alpha)}{\mu_\alpha}
   \left(\nabla p_\alpha-\rho_\alpha\mathbf{g}\right),

where :math:`\mathbf{k}` is the absolute permeability tensor,
:math:`k_{r\alpha}` is the dimensionless relative permeability,
:math:`\mu_\alpha` and :math:`\rho_\alpha` are phase viscosity and density,
and :math:`\mathbf{g}` is gravity. The phase mass balances are

.. math::

   \frac{\partial(\phi\rho_\alpha S_\alpha)}{\partial t}
   +\nabla\cdot(\rho_\alpha\mathbf{q}_\alpha)=m_\alpha,
   \qquad \alpha\in\{w,n\},

where :math:`\phi` is porosity and :math:`m_\alpha` is a mass source per unit
bulk volume for that phase. These balances are coupled through the saturation
constraint, the capillary-pressure relation, and the relative-permeability
functions.

Relative permeability and closure
~~~~~~~~~~~~~~~~~~~~

Relative permeability accounts macroscopically for the reduction in a phase's
conducting pore space due to the presence of the other phase. It usually
varies between zero and one and is specified as a function of saturation,
often together with residual saturations. One illustrative Corey-type closure
uses the effective wetting saturation

.. math::

   S_e=\frac{S_w-S_{wr}}{1-S_{wr}-S_{nr}},
   \qquad
   k_{rw}=S_e^{n_w},
   \qquad
   k_{rn}=(1-S_e)^{n_n},

where :math:`S_{wr}` and :math:`S_{nr}` are residual wetting- and
non-wetting-phase saturations, and :math:`n_w,n_n` are empirical exponents.
This is an example, not a universal law: measured or calibrated
capillary-pressure and relative-permeability curves should be used when
available. Hysteresis, compressibility, dissolution, and dynamic interfacial
effects require additional constitutive assumptions.

Model limits
~~~~~~~~~~~~~~~~~~~~

If capillary effects are negligible, the phase pressures may be approximated
as equal; if one phase is absent, the model reduces to single-phase flow.
Saturation fronts can be sharp, so the predicted solution may depend on
constitutive curves, mesh resolution, and time-step selection. The choice of
primary unknowns (for example, one phase pressure and one saturation) is a
numerical formulation decision and does not change the underlying conservation
laws.

===================================================================

Gas Flow
--------


To reproduce the coupled fracturing behavior driven by blasting gas with high
fidelity, OpenFDEM provides a compressible gas-solid coupling model based on
FDEM. The blasting gas is assumed to obey the ideal gas equation of state. At
each time step, the gas volume at different locations along the fractures is
computed, allowing the gas density and bulk modulus to be updated. The gas
pressure field is then transferred to the mechanical module to compute the
fracture propagation at the next time step, and the updated fracture geometry
is subsequently used for the next gas-flow calculation. The definition of the
fracture aperture and volume is described in the preceding fracture-fluid
section.

.. figure:: ../_static/Theory/gas_fracture_development.png
    :alt: Blast-induced fracture development
    :width: 80%
    :align: center

    Figure 1. Development of the blast-induced fracture network: from stress
    wave loading to gas-driven secondary fracture extension.

Compressible gas flow model
~~~~~~~~~~~~~~~~~~~~

The velocity of blasting gas can reach the order of hundreds of meters per
second, and the fracture aperture can be estimated to range from
:math:`10^{-6}` to :math:`10^{-4}` m. The Reynolds number can then be
calculated using

.. math::
    \mathrm{Re}=\frac{\rho va}{\mu} \tag{1}

where :math:`\rho` is the fluid density, :math:`v` is the gas velocity,
:math:`a` is the fracture aperture, and :math:`\mu` is the dynamic viscosity.
The Reynolds number of blasting gas flowing through blast-induced fractures
can be preliminarily estimated to range from approximately 10 to 1000. When
:math:`\mathrm{Re}` exceeds 1, inertial effects must be considered, meaning
that the Forchheimer model should be adopted and the conventional Darcy flow
model is no longer applicable.

The flow of blasting gas within rock fractures satisfies the principle of mass
conservation

.. math::
    \frac{\partial \rho _g}{\partial t}+\nabla \cdot \left( \rho _g\mathbf{q}_{\mathbf{g}} \right) =0 \tag{2}

where :math:`\mathbf{q}_g` is the gas velocity vector and :math:`\rho _g` is
the gas density. Integrating over any control volume :math:`V_i` and its
control boundary :math:`\varGamma _i` yields

.. math::
    \frac{\partial}{\partial t}\int_{V_i}{\rho _gdV}+\int_{\varGamma _i}{\rho _g\left( \mathbf{q}_{\mathbf{g}}\cdot \mathbf{n} \right)}\,d\varGamma =0 \tag{3}

where :math:`\mathbf{n}` is the unit vector normal to the boundary of the
control volume.

For an ideal adiabatic compressible gas, the variation of density with time is
pressure-dependent

.. math::
    \frac{\partial \rho _g}{\partial t}=\frac{\partial \rho _g}{\partial p_g}\frac{\partial p_g}{\partial t}=\frac{\rho _g}{K_g}\frac{\partial p_g}{\partial t} \tag{4}

where :math:`K_g` is the bulk modulus of the gas. Combining the volume and
boundary integral terms, the discrete pressure equation for the control volume
:math:`V_i` becomes

.. math::
    \frac{V_i}{K_g}\frac{\partial p_g}{\partial t}+Q_{i}^{total}=0 \tag{5}

where :math:`Q_{i}^{total}` is the total flow rate within the control volume,
from which the gas pressure can be determined.

Because the velocity of blasting gas is relatively high, the pressure gradient
term and the velocity term in Darcy's law exhibit a nonlinear dependence.
Forchheimer introduced an empirical constant :math:`\beta` to account for this
nonlinearity caused by inertial effects

.. math::
    \nabla p_g+\rho _gg=\frac{\rho _gg}{\mathrm{k}_i}q_g+\beta \rho _g{q_g}^2, \quad \mathrm{k}_i=k_g\frac{\rho _gg}{\mu} \tag{6}

where :math:`\mathrm{k}_i` is the gas permeability coefficient, :math:`k_g` is
the gas permeability, and :math:`\beta` characterizes the influence of the
inertial effects. The parameter :math:`\beta` is expressed as

.. math::
    \beta =\lambda \left( \frac{\xi}{D_{\mathrm{h}}} \right) ^{\eta} \tag{7}

where :math:`D_{\mathrm{h}}=2a` is the hydraulic diameter, :math:`\xi` is the
peak penetration height, and :math:`\lambda` and :math:`\eta` are two
empirical coefficients, taken as 0.022 and 2/3, respectively. Based on Eq. 6,
the gas velocity between any fracture element node :math:`i` in one cavity and
its corresponding node :math:`j` in an adjacent cavity can be expressed as

.. math::
    q_g=\frac{1}{2\rho _g\beta}\left( -\frac{\mu}{k_g}+\sqrt{\left( \frac{\mu}{k_g} \right) ^2+4\beta \rho _g\frac{\varDelta p_g}{L}} \right) \tag{8}

where :math:`\varDelta p_g` is the gas pressure difference between cavity
:math:`i` and cavity :math:`j`, calculated from the previous time step, and
:math:`L` is the length of the fracture element.

.. figure:: ../_static/Theory/gas_nondarcy_flow.png
    :alt: Non-Darcy gas flow
    :width: 60%
    :align: center

    Figure 2. Non-Darcy gas flow: comparison of the gas flow velocity between
    the Forchheimer (non-Darcy) and Darcy models.

Gas equation of state
~~~~~~~~~~~~~~~~~~~~

During the ideal adiabatic compressible gas flow, compressibility must be
taken into account. Unlike liquids, which are nearly incompressible, the
density of the gas changes significantly with pressure. Both density and bulk
modulus vary with pressure. According to the equation of state for an ideal
adiabatic gas, the gas density :math:`\rho _g` and bulk modulus :math:`K_g`
are given by

.. math::
    \rho _g=\rho _0p_{g}^{-\frac{1}{\gamma}} \tag{9}

.. math::
    K_g=p_g\gamma \tag{10}

where :math:`\rho _0` is the initial gas density, :math:`p_g` is the current
gas pressure in the cavity, and :math:`\gamma` is the adiabatic index of the
gas. In this study, the adiabatic index of the blasting gas is approximated by
that of air, :math:`\gamma=1.4`.

Gas-solid coupling
~~~~~~~~~~~~~~~~~~~~

Following the determination of gas pressures for all cavities within the
computational domain, the gas pressure :math:`\sigma _g` acting on each
adjacent solid element is calculated. Defining the mass flow rate as
:math:`m_t=q_g\left( x \right) \rho \left( x \right) A_e`, the flow equation
can be written as

.. math::
    \frac{d\sigma _g\left( x \right)}{dx}=\left( \frac{\mu m_t}{k_gA_e}+\frac{{\beta m_t}^2}{A_{e}^{2}} \right) \left( \rho _{c,in}\left( \frac{\sigma _g\left( x \right)}{p_{c,in}} \right) ^{\frac{1}{\gamma}} \right) ^{-1} \tag{11}

where :math:`p_{c,in}` and :math:`\rho _{c,in}` represent the gas pressure and
density at the inlet cavity, respectively. Integrating this equation yields
the gas pressure distribution along each fracture element

.. math::
    \sigma _g\left( x \right) =\left[ p_{c,in}^{\frac{\gamma +1}{\gamma}}+\frac{\gamma +1}{\gamma}\frac{p_{c,in}^{\frac{1}{\gamma}}}{\rho _{c,in}}\left( \frac{\mu m_t}{k_gA_e}+\frac{{\beta m_t}^2}{A_{e}^{2}} \right) x \right] ^{\frac{\gamma}{\gamma +1}} \tag{12}

Once the pressure distribution along the parallel plate is obtained, the
virtual work principle is applied to equivalently assign the pressure to the
nodes of the fracture element, yielding the nodal force

.. math::
    \mathbf{f}_{\mathbf{gas}}=\int_{S_e}{\mathbf{N}^{\mathrm{T}}\left( x \right) \sigma _g\left( x \right) \cdot \mathbf{n}}\,ds \tag{13}

where :math:`\mathbf{n}` is the normal vector of the element surface subjected
to the gas action, :math:`S_e` is the area of that surface, and
:math:`\mathbf{N}(x)` is the shape function matrix of the element.

The gas-mechanical coupling is achieved by alternately advancing the time
steps between the mechanical solver and the gas-pressure solver, realizing a
fully bidirectional coupling. The mechanical solver computes the deformation,
fracturing and interaction of the rock mass. The gas flow solver then captures
the change in cavity volume caused by fracture propagation, elastic
deformation and gas compressibility, recalculates the gas density and bulk
modulus, and determines the gas pressure, which is applied back to the
mechanical solver as an external load.

.. figure:: ../_static/Theory/gas_module_interaction.png
    :alt: Interaction between computational modules
    :width: 53%
    :align: center

    Figure 3. Interaction between the mechanical solver and the gas flow
    solver.

Critical time step of the coupling
~~~~~~~~~~~~~~~~~~~~

Both the mechanical and gas solvers employ an explicit time integration
scheme. The critical time step of the mechanical solver, required to ensure
numerical stability, can be estimated as

.. math::
    \varDelta t_{cr}^{s}=\frac{h_{\min}}{\sqrt{\left( \lambda +2\mu \right) /\rho}} \tag{14}

where :math:`h_{\min}` is the minimum width of the solid element,
:math:`\lambda` and :math:`\mu` are the Lamé constants, and :math:`\rho` is
the material density. The critical time step for the gas solver is given by

.. math::
    \varDelta t_{cr}^{g}=\min \left[ \frac{V_i}{K_g\sum_i{\frac{k_{g,i}}{\mu _g}}} \right] \tag{15}

where :math:`k_{g,i}` is the permeability, :math:`\mu _g` is the dynamic
viscosity of the fluid, and :math:`K_g` is the gas bulk modulus. Because the
critical time step for transient flow can be very restrictive, a sub-cycling
strategy is adopted, in which each mechanical time-step loop contains multiple
gas-calculation sub-cycles. After the gas flow solver completes the specified
number of sub-cycles, the gas pressure from the final sub-cycle is passed to
the mechanical solver, which then proceeds to the next mechanical time step.

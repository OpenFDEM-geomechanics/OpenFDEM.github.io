Gas Flow
====================================

To reproduce the coupled fracturing behavior driven by blasting gas with high
fidelity, OpenFDEM provides a compressible gas-solid coupling model based on
FDEM. The blasting gas is assumed to obey the ideal gas equation of state. At
each time step, the gas volume at different locations along the fractures is
computed, allowing the gas density and bulk modulus to be updated. The gas
pressure field is then transferred to the mechanical module to compute the
fracture propagation at the next time step, and the updated fracture geometry
is subsequently used for the next gas-flow calculation. The definition of the
fracture aperture and volume is described in the :doc:`Fracture_Fluid_Theory`
section.

.. figure:: ../../images/Theory/gas_fracture_development.png
    :alt: Blast-induced fracture development
    :width: 80%
    :align: center

    Figure 1. Development of the blast-induced fracture network: from stress
    wave loading to gas-driven secondary fracture extension.

Compressible gas flow model
------------------------------------------------

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

.. figure:: ../../images/Theory/gas_nondarcy_flow.png
    :alt: Non-Darcy gas flow
    :width: 60%
    :align: center

    Figure 2. Non-Darcy gas flow: comparison of the gas flow velocity between
    the Forchheimer (non-Darcy) and Darcy models.

Gas equation of state
------------------------------------------------

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
------------------------------------------------

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

.. figure:: ../../images/Theory/gas_module_interaction.png
    :alt: Interaction between computational modules
    :width: 53%
    :align: center

    Figure 3. Interaction between the mechanical solver and the gas flow
    solver.

Critical time step of the coupling
------------------------------------------------

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


.. raw:: html

   <script type="text/javascript" id="mapmyvisitors" src="//mapmyvisitors.com/map.js?d=FhQBKeKNkCLqgUfZdslz45dHXRuV_WDVgVzZVYmuX7s&cl=ffffff&w=a"></script>

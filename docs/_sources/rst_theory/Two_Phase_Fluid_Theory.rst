Two-Phase Fluid
===============

Two-phase porous flow describes two immiscible fluids, such as water and gas
or water and oil, sharing the same pore space. Because both phases compete for
the available pores, each phase's mobility depends on saturation. The
equations below give the standard continuum formulation; they do not prescribe
a particular relative-permeability curve or imply that this formulation is
used by every OpenFDEM fluid solver.

Saturation and capillary pressure
---------------------------------

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
-----------------------------------------

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
---------------------------------

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
------------

If capillary effects are negligible, the phase pressures may be approximated
as equal; if one phase is absent, the model reduces to single-phase flow.
Saturation fronts can be sharp, so the predicted solution may depend on
constitutive curves, mesh resolution, and time-step selection. The choice of
primary unknowns (for example, one phase pressure and one saturation) is a
numerical formulation decision and does not change the underlying conservation
laws.

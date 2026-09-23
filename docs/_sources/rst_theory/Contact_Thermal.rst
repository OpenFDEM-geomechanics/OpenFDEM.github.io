Contact Thermal
===============

Contact thermal transfer exchanges heat between the surfaces of two discrete
elements or blocks in contact. It provides a thermal connection across a
mechanical contact and is commonly modeled with a conductance proportional to
the temperature difference across the interface.

Interface law
-------------

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
---------------------------------------

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

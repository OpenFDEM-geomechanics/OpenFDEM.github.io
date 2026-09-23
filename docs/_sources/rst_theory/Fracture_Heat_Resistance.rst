Fracture Heat Resistance
========================

A fracture interrupts direct heat conduction through the intact matrix. Heat
may still cross the discontinuity through gas, liquid, or solid material in the
fracture, as well as through microscopic asperity contacts between its faces.
These mechanisms can be represented by an effective thermal resistance.

Series-resistance model
-----------------------

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
------------------------------

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

Phase Field
===========

The phase-field method represents a sharp crack by a smooth damage field over
a narrow band. This avoids explicitly tracking a moving crack surface and
allows complex crack paths, branching, and coalescence to emerge from the
solution. In this section, :math:`d=0` denotes intact material and :math:`d=1`
fully developed fracture. The formulation is a standard variational model for
quasi-brittle or brittle fracture; the precise degradation law and material
split used in a computation are model choices.

Regularized fracture energy
---------------------------

For linear elastic material, a representative total potential energy is

.. math::

   \Pi(\mathbf{u},d)
   =\int_{\Omega}
   \left[g(d)\psi_e^+(\boldsymbol{\varepsilon})
   +\psi_e^-(\boldsymbol{\varepsilon})\right]\,\mathrm{d}\Omega
   +\int_{\Omega}G_c\,\gamma_\ell(d,\nabla d)\,\mathrm{d}\Omega
   -W_{\mathrm{ext}},

where :math:`\mathbf{u}` is displacement,
:math:`\boldsymbol{\varepsilon}` is strain, :math:`\psi_e^+` and
:math:`\psi_e^-` are the tensile and compressive parts of the elastic energy,
:math:`G_c` is fracture energy per unit crack area, and
:math:`W_{\mathrm{ext}}` is external work. Separating tensile and compressive
energy prevents compressive states from spuriously driving crack growth.

For the common AT2 crack-density function and quadratic degradation law,

.. math::

   \gamma_\ell(d,\nabla d)
   =\frac{d^2}{2\ell}+\frac{\ell}{2}|\nabla d|^2,
   \qquad
   g(d)=(1-d)^2+\kappa,

where :math:`\ell` is the regularization length and :math:`\kappa` is a small
residual stiffness used to avoid a singular elastic operator. The length
:math:`\ell` controls the width of the diffused crack and must be resolved by
the mesh. Other crack-density functions, such as AT1, lead to different
evolution equations and nucleation behavior.

Mechanical equilibrium and damage evolution
--------------------------------------------

Quasi-static mechanical equilibrium is expressed as

.. math::

   \nabla\cdot\boldsymbol{\sigma}+\mathbf{b}=\mathbf{0},
   \qquad
   \boldsymbol{\sigma}
   =g(d)\frac{\partial\psi_e^+}{\partial\boldsymbol{\varepsilon}}
   +\frac{\partial\psi_e^-}{\partial\boldsymbol{\varepsilon}},

where :math:`\boldsymbol{\sigma}` is Cauchy stress and :math:`\mathbf{b}` is
body force per unit volume. For the AT2 choice, a common phase-field equation
is

.. math::

   \frac{G_c}{\ell}d-G_c\ell\nabla^2d
   -2(1-d)H=0,

where :math:`H` is a history field that stores the maximum tensile elastic
energy attained at a material point. Using a non-decreasing history field
enforces the irreversibility of fracture in a staggered solution; equivalently,
the damage is constrained not to decrease with loading. Boundary conditions
for :math:`d` and mechanical displacement must be selected consistently with
the physical crack and loading problem.

Numerical interpretation
------------------------

The regularization length is a material/model scale, not simply a mesh size.
The mesh should contain multiple elements across the diffused crack band, and
results should be checked for sensitivity to :math:`\ell`, mesh resolution,
and residual stiffness. Staggered solution alternates between mechanical
equilibrium and damage evolution; monolithic solution solves both fields
together. These are numerical strategies for the coupled equations, not
different fracture-energy definitions.

The equations shown are a reference AT2-type formulation. They provide
theoretical context for the Phase Field module and should not be interpreted as
a complete listing of every constitutive option or solver detail in OpenFDEM.

Further reading
---------------

* Bourdin, B., Francfort, G. A., and Marigo, J.-J. (2000). Numerical
  experiments in revisited brittle fracture. *Journal of the Mechanics and
  Physics of Solids*, 48(4), 797-826. DOI: 10.1016/S0022-5096(99)00028-9.
* Miehe, C., Welschinger, F., and Hofacker, M. (2010). Thermodynamically
  consistent phase-field models of fracture: Variational principles and
  multi-field FE implementations. *International Journal for Numerical
  Methods in Engineering*, 83(10), 1273-1311. DOI: 10.1002/nme.2861.

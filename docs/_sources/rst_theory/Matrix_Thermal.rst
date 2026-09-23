Matrix Thermal
==============

Matrix thermal transfer describes heat storage and conduction within the
intact solid material. Temperature gradients drive heat from warmer regions
toward cooler regions, while heat sources, boundary conditions, and material
properties determine the transient temperature field.

Fourier's law
-------------

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
--------------

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
-------------------------------

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

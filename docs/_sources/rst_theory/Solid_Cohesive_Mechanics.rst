Solid Cohesive Mechanics
====================================

In FDEM, cohesive elements are inserted between adjacent bulk elements to
bond the node pairs and to represent the initiation and propagation of
fractures. As separation of a node pair arises, the cohesive element undergoes
an elastic deformation stage, a damage softening stage and an ultimate
fracturing stage.

Constitutive law of the cohesive element
--------------------------------------------

The constitutive law of the cohesive element is characterized by the fracture
process zone (FPZ) model. By separating the normal and tangent components, the
constitutive law between the separation
:math:`\boldsymbol{\delta }=\left[ o, s \right]` and the cohesive stress
:math:`\boldsymbol{\sigma }=\left[ \sigma _n, \tau \right]` can be described as

.. math::
    :nowrap:

    \[\sigma _n=\begin{cases}
    \frac{o}{h}p_n, & o<0\\
    p_no, & 0<o\le o_p\\
    f\left( D \right) f_t, & o_p<o\le o_r\\
    0, & o>o_r\\
    \end{cases} \tag{1}\]

.. math::
    :nowrap:

    \[\tau =\begin{cases}
    p_ns, & |s|\le s_p\\
    f\left( D \right) f_s, & s_p<|s|\le s_r\\
    \sigma _n\tan \varphi , & |s|>s_r\\
    \end{cases} \tag{2}\]

where :math:`\sigma _n` and :math:`\tau` denote the normal and tangent
components of the bonding stress :math:`\boldsymbol{\sigma }`, respectively;
:math:`o` and :math:`s` denote the normal and tangent components of the
relative displacement :math:`\boldsymbol{\delta }` between a node pair;
:math:`p_n` is the penalty stiffness; :math:`o_p` and :math:`s_p` are the
elastic limit displacements in the normal and tangent directions, with
:math:`o_p=f_t/p_n` and :math:`s_p=f_s/p_n`; :math:`o_r` and :math:`s_r` are
the ultimate limit displacements; :math:`f_t` and :math:`f_s` are the tensile
strength and direct shear strength of the cohesive element; :math:`\varphi` is
the inner friction angle; and :math:`f\left( D \right)` is the characteristic
function describing the softening curves, where :math:`D` is the damage
variable defined as

.. math::
    D=\min \left[ 1,\sqrt{\left( \frac{o-o_p}{o_r-o_p} \right) ^2+\left( \frac{|s|-s_p}{s_r-s_p} \right) ^2} \right] \tag{3}

.. figure:: ../../images/Theory/qFDEM_joint_behaviour.png
    :alt: Mechanical behaviour of joint elements in FDEM
    :width: 85%
    :align: center

    Figure 1. Mechanical behaviour of joint elements in FDEM: (a) Mode I
    tensile behaviour and Mode II shear behaviour; (b) Mixed mode failure
    criterion.

Quadratic cohesive element
--------------------------------------------

In the two-dimensional linear FDEM framework, four-node cohesive elements are
used to bond the node pairs between linear triangle elements. To satisfy the
continuity condition in continuum mechanics, all node pairs among high-order
elements should be adhered to ensure the stress coordination on the edges.
Therefore, a novel quadratic cohesive element is proposed. The new cohesive
element ensures the compatibility of bulk elements of an arbitrary order
through uniform cohesion among node pairs.

Based on Eqs. 1-3, the stress at the positions of all node pairs can be
directly obtained. However, to compute the nodal cohesive force, the complete
stress distribution along the element edge and the integration strategy need
further assumptions. The traditional four-node cohesive element assumes a
linear cohesive stress distribution consistent with the displacement
distribution along the element edge. Extending this assumption to the
quadratic-order case, the integrated nodal cohesive force
:math:`\boldsymbol{f}_{\mathrm{int},\mathrm{coh}}^{ecoh}` can be given based on
the principle of virtual work

.. math::
    \boldsymbol{f}_{\mathrm{int},\mathrm{coh}}^{ecoh}=\int_{\Gamma _{ecoh}}{\left( \left. \boldsymbol{N}^{ecoh} \right|_{\varGamma} \right) ^{\mathrm{T}}\cdot \left. \boldsymbol{N}^{ecoh} \right|_{\varGamma}\boldsymbol{t}_{ecoh}}\mathrm{d}\Gamma _{ecoh}=\boldsymbol{W}\cdot \boldsymbol{t}_{ecoh} \tag{4}

where the local nodal cohesive traction vector is
:math:`\boldsymbol{t}_{ecoh}=\left[ \boldsymbol{t}_1, \boldsymbol{t}_2, \boldsymbol{t}_3 \right] ^{\mathrm{T}}`,
and :math:`\boldsymbol{W}` is the nodal cohesive force allocation matrix. At
the elastic state, the nodal cohesive force can be expressed as the product of
the cohesive stiffness matrix :math:`\boldsymbol{K}` and the relative
displacement of each node pair, i.e.
:math:`\boldsymbol{f}_{\mathrm{int},\mathrm{coh}}^{ecoh}=\boldsymbol{K}\cdot \boldsymbol{\delta}`
with :math:`\boldsymbol{K}=p_n\boldsymbol{W}`.

Giving the quadratic shape function vector in one dimension
:math:`\left. \boldsymbol{N}^{ecoh} \right|_{\varGamma}=\frac{h}{2}\left[ \frac{1}{2}\xi \left( \xi -1 \right) , 1-\xi ^2, \frac{1}{2}\xi \left( \xi +1 \right) \right]`,
the stiffness using continuously distributed stress
:math:`\boldsymbol{K}_{continuous}` is obtained as

.. math::
    :nowrap:

    \[\boldsymbol{K}_{continuous}=\frac{hp_n}{2}\left[ \begin{matrix}
    4/15 & 2/15 & -1/15\\
    2/15 & 16/15 & 2/15\\
    -1/15 & 2/15 & 4/15\\
    \end{matrix} \right] \tag{5}\]

where :math:`h` is the length of the element edge. It can be observed that the
cohesive stiffness is primarily concentrated on the mid-side node, while the
stiffness on the corner nodes remains very weak. This non-uniform assignment
of cohesive stiffness can induce deformation incompatibility at the interfaces
of the bonded continuum elements, leading to a non-physical degradation of the
apparent cohesive strength, and causing premature damage of the cohesive
element at the edges even when the overall stress level is far below the
nominal strength.

.. figure:: ../../images/Theory/qFDEM_cohesive_strategies.png
    :alt: High order cohesive elements and two computation strategies
    :width: 70%
    :align: center

    Figure 2. High order cohesive elements and two computation strategies:
    (a) Quadratic order cohesive element; (b) Continuously distributed stress
    method; (c) Discrete nodal spring method.

Therefore, a new quadratic cohesive element is proposed to solve this problem.
As shown in Figure 2 (c), the newly developed cohesive element can be treated
as a series of independent springs, which compute the cohesive force solely
based on each node pair's cohesive stress. Consequently, the nodal force at
each node can be directly determined as

.. math::
    \boldsymbol{f}_{\mathrm{int},\mathrm{coh}}^{ecoh,i}=\frac{h}{3}\boldsymbol{t}_{ecoh,i} \tag{6}

and the nodal force vector can also be represented as
:math:`\boldsymbol{f}_{\mathrm{int},\mathrm{coh}}^{ecoh}=\boldsymbol{W}_d\cdot \boldsymbol{t}_{ecoh}`,
where the weight matrix :math:`\boldsymbol{W}_d=\frac{h}{3}\boldsymbol{I}_n`.
At the elastic state, the cohesive stiffness :math:`\boldsymbol{K}_{discrete}` is

.. math::
    :nowrap:

    \[\boldsymbol{K}_{discrete}=\frac{hp_n}{3}\left[ \begin{matrix}
    1 & 0 & 0\\
    0 & 1 & 0\\
    0 & 0 & 1\\
    \end{matrix} \right] \tag{7}\]

In this way, each node pair is bonded without bias. As shown in Figure 3, the
opening of the three node pairs using the proposed nodal spring element is very
uniform. This not only ensures the interface compatibility but also prevents
the artificial reduction of the material strength in the quadratic-order
circumstance of FDEM.

.. figure:: ../../images/Theory/qFDEM_interface_compat.png
    :alt: Comparison of interface compatibility
    :width: 85%
    :align: center

    Figure 3. The comparison of interface compatibility under (a) Uniform
    nodal force between (b) Continuously distributed stress method, and (c)
    Discrete nodal spring method.


.. raw:: html

   <script type="text/javascript" id="mapmyvisitors" src="//mapmyvisitors.com/map.js?d=FhQBKeKNkCLqgUfZdslz45dHXRuV_WDVgVzZVYmuX7s&cl=ffffff&w=a"></script>

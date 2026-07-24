Fracture Fluid
====================================

When subjected to explosive loading, the rock mass experiences the rapid
propagation of stress waves radiating outward from the blast hole. As the
waves travel and dissipate, radial fractures form, and the blasting gas
infiltrates the newly formed cracks, driving their secondary extension and
ultimately giving rise to a well-connected fracture network. In OpenFDEM, the
fracture geometry provides the flow domain through which the fluid (gas or
liquid) travels.

Fracture aperture
------------------------------------------------

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
------------------------------------------------

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

.. figure:: ../../images/Theory/gas_flow_process.png
    :alt: Fracture flow process
    :width: 45%
    :align: center

    Figure 1. Fluid flow through the fracture network formed by failed
    cohesive elements.

.. figure:: ../../images/Theory/gas_fracture_aperture.png
    :alt: Fracture unit opening and channel volume
    :width: 41%
    :align: center

    Figure 2. Fracture unit opening and channel volume.

.. figure:: ../../images/Theory/gas_flow_cavity.png
    :alt: Schematic of the flow cavity
    :width: 41%
    :align: center

    Figure 3. Schematic of the flow cavity comprising Nodes 1-6.


.. raw:: html

   <script type="text/javascript" id="mapmyvisitors" src="//mapmyvisitors.com/map.js?d=FhQBKeKNkCLqgUfZdslz45dHXRuV_WDVgVzZVYmuX7s&cl=ffffff&w=a"></script>

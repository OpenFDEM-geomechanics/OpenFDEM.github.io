of.boundary.edge.velocity
=========================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`boundary.edge.velocity` :blue:`*edge_tag*` <string> :blue:`normal` <double> :blue:`shear` <double> :blue:`ntable` <string_tag> :blue:`stable` <string_tag>
    |
    Create the edge velocity boundary on the edge groups. The velocity can be time dependent if you use the table. The normal shear values will be the factor if you use the table. That is
    :math:`v[i] = x \times table[i]`

    The edge will be automatically applied on the two nodes of the edge and consider the edge direction. Normal direction is the local normal direction, and towards to inside. Shear is along the edge, and counterclockwise


    **Parameters:** 
        **nodal_tag:** tag of the group
        
        **normal:** (default 0.0) Edge velocity in the local normal direction or the amplitude of n table.
        
        **shear:** (default 0.0) Edge velocity in the local shear direction or the amplitude of s table.

        **ntable:** (default -1) time dependent velocity in the local normal direction.
        
        **stable:** (default -1) time dependent velocity in the local shear direction.

|

Example:
--------------------------------------------------------------------

.. code-block:: 

    # pin the up
    of.boundary.edge.velocity ‘up’ normal 0.0 shear 0.0
    # assign the table which is named as pwave
    of.boundary.edge.velocity ‘up’ normal 1.0 ntable ‘pwave’



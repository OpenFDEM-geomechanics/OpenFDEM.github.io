of.boundary.edge.acceleration
=============================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`boundary.edge.acceleration` :blue:`*edge_tag*` <string> :blue:`normal` <double> :blue:`shear` <double> :blue:`ntable` <string_tag> :blue:`stable` <string_tag>
    |
    Create the edge acceleration boundary on the edge groups. The acceleration can be time dependent if you use the table. The normal shear values will be the factor if you use the table. That is 
    :math:`a[i] = x \times table[i]`
    
    **Parameters:** 
        **nodal_tag:** tag of the group
        
        **normal:** (default 0.0) Acceleration in the normal direction or the amplitude of n table.
        
        **shear:** (default 0.0) Acceleration in the shear direction or the amplitude of s table.

        **ntable:** (default -1) time dependent acceleration in the normal direction.
        
        **stable:** (default -1) time dependent acceleration in the shear direction.

|

Example:
--------------------------------------------------------------------

.. code-block:: 

    # ball will be given an acceleration of 100m/s^2
    of.boundary.edge.acceleration ‘ball’ shear -100
of.boundary.edge.inivelocity
============================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`boundary.edge.inivelocity` :blue:`*edge_tag*` <string> :blue:`normal` <double> :blue:`shear` <double>
    |
    Create the edge initial velocity boundaries on the edge groups. The velocity will be applied only at the initial.


    **Parameters:** 
        **nodal_tag:** tag of the group
        
        **normal:** (default free) Edge velocity in the local normal direction or the amplitude of n table.
        
        **shear:** (default free) Edge velocity in the local shear direction or the amplitude of s table.

|

Example:
--------------------------------------------------------------------

.. code-block:: 

    # ball will be given an initial impact velocity of 100m/s
    of.boundary.edge.inivelocity ‘ball’ shear -100


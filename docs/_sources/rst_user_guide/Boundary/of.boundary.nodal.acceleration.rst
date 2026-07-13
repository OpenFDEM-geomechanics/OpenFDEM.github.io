of.boundary.nodal.acceleration
==============================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`boundary.nodal.acceleration` :blue:`*nodal_tag*` <string> :blue:`x` <double> :blue:`y` <double> :blue:`r` <double> :blue:`xtable` <string_tag> :blue:`ytable` <string_tag> :blue:`rtable` <string_tag>
    |
    Create the nodal acceleration boundary on the nodal groups. r is for the angular acceleration, in :math:`rad/s^2`. The acceleration can be time dependent if you use the table. The x, y, r values will be the factor if you use the table. That is 
    :math:`a[i] = x \times table[i]`
    
    **Parameters:** 
        **nodal_tag:** tag of the group
        
        **x:** (default 0.0) Acceleration in the x direction or the amplitude of x table.
        
        **y:** (default 0.0) Acceleration in the y direction or the amplitude of y table.
        
        **r:** (default 0.0) Angular acceleration.

        **xtable:** (default -1) time dependent acceleration in x direction.
        
        **ytable:** (default -1) time dependent acceleration in y direction.
        
        **rtable:** (default -1) time dependent angular acceleration.
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    # ball will be give an acceleration of 100m/s^2
    of.boundary.nodal.acceleration ‘ball’ y -100
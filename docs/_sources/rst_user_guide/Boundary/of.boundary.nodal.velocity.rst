of.boundary.nodal.velocity
==========================
.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`boundary.nodal.velocity` :blue:`*nodal_tag*` <string> :blue:`x` <double> :blue:`y` <double> :blue:`r` <double> :blue:`xtable` <string_tag> :blue:`ytable` <string_tag> :blue:`rtable` <string_tag>
    |
    Create the nodal velocity boundary on the nodal groups. r is for the angular velocity, in rad/s. The velocity can be time dependent if you use the table. The x, y, r values will be the factor if you use the table. That is 

    :math:`v[i] = x \times table[i]`
    
    **Parameters:** 
        **nodal_tag:** tag of the group
        
        **x:** (default 0.0) Velocity in the x direction or the amplitude of x table.
        
        **y:** (default 0.0) Velocity in the y direction or the amplitude of y table.
        
        **r:** (default 0.0) Angular velocity

        **xtable:** (default -1) time dependent velocity in x direction.
        
        **ytable:** (default -1) time dependent velocity in y direction.
        
        **rtable:** (default -1) time dependent angular velocity.
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    # fix in x direction, y direction and rotation
    of.boundary.nodal.velocity ‘up’ x 0.0 y 0.0 r 0.0
    # assign the table which is named as pwave 
    of.boundary.nodal.velocity ‘up’ x 1.0 xtable ‘pwave’



of.boundary.nodal.force
=======================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`boundary.nodal.force` :blue:`*nodal_tag*` <string> :blue:`x` <double> :blue:`y` <double> :blue:`r` <double> :blue:`xtable` <string_tag> :blue:`ytable` <string_tag> :blue:`rtable` <string_tag>
    |
    Create nodal force boundaries on nodal groups. r is for the moment. The force can be time dependent if you use the table. The x, y, r values will be the factor if you use the table. That is 

    :math:`f[i] = x \times table[i]`
    
    **Parameters:** 
        **nodal_tag:** tag of the group
        
        **x:** (default 0.0) Nodal forces in the x direction or the amplitude of x table.
        
        **y:** (default 0.0) Nodal forces in the y direction or the amplitude of y table.
        
        **r:** (default 0.0) Nodal moments or the amplitude of r table.

        **xtable:** (default -1) time dependent nodal force in x direction.
        
        **ytable:** (default -1) time dependent nodal force in y direction.
        
        **rtable:** (default -1) time dependent moment.
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.boundary.nodal.force ‘bottom’ x -1 xtable ‘pwave’


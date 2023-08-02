of.boundary.nodal.inivelocity
=============================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`boundary.nodal.inivelocity` :blue:`*nodal_tag*` <string> :blue:`x` <double> :blue:`y` <double> :blue:`r` <double> :blue:`xtable` <string_tag> :blue:`ytable` <string_tag> :blue:`rtable` <string_tag>
    |
    Create the nodal initial velocity boundaries on the nodal groups. r is for the angular velocity, in rad/s. The velocity will be applied only at the initial.

    **Parameters:** 
        **nodal_tag:** tag of the group
        
        **x:** (default free) Initial velocity in the x direction.
        
        **y:** (default free) Initial elocity in the y direction.
        
        **r:** (default free) Initial angular velocity

|

Example:
--------------------------------------------------------------------

.. code-block:: 

    # an initial impact velocity of the ball is 100m/s
    of.boundary.nodal.inivelocity ‘ball’ y -100 



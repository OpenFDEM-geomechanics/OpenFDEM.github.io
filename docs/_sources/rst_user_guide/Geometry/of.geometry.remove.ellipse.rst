of.geometry.remove.ellipse
==========================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`geometry.remove.ellipse` :blue:`*new_geometry_tag*` <string> :blue:`*object_geometry_tag*` <string> :blue:`*region*` <double, double, double, double, double, int>
    |
    Remove the geometry in the object by assigning the x, y, maxradius, minradius, theta and segments of the ellipse.

    **Parameters:** 
        **new_geometry_tag:** tag of the geometry group cut from the original geometry.

        **object_geometry_tag:** tag of the original geometry group
        
        **region:** (default nseg 20) There are three methods to define a ellipse:
        
        1. [x y minradius maxradius theta nseg]
        2. center [x, y] radius [min max] theta nseg 
        3. x value, y value, rad value. minradius value, maxradius value, theta value, nseg value
        
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.geometry.remove.ellipse [tunnel] [rock] center [0,0] rad [1.0, 2.0] theta 0 segments 10

.. figure:: ../../../images/User_Guide/Ellipse_Remove.png
    :alt: Ellipse_Remove
    :align: center
    :scale: 60%

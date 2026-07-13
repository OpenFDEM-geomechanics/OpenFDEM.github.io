of.geometry.cut.arc
===================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`geometry.cut.arc` :blue:`*new_geometry_tag*` <string> :blue:`*object_geometry_tag*` <string> :blue:`*region*` <double, double, double, double, int>
    Create an arc geometry in object geometry by assign the center, start angle, end angle, radius and number of segments.
    
    **Parameters:** 
        **new_geometry_tag:** tag of the geometry group cut from the original geometry.

        **object_geometry_tag:** tag of the original geometry group
        
        **region:** (default nseg 20) There are three methods to create a circle:
        
        1. [x, y, rad, nseg]
        2. center [x, y] radius nseg 
        3. x value y value rad value nseg value
        
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.geometry.cut.arc [tunnel_edge] [rock] center [0,0] radius 1.0 theta [45, 90] segments 20
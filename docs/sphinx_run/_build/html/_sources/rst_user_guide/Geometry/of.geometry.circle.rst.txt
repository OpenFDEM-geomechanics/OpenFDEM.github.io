of.geometry.circle
==================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`geometry.circle` :blue:`*geometry_tag*` <string> :blue:`*region*` <double, double, double, int>
    Create a geometry by assigning the x, y, radius and segments of the circle.


    **Parameters:** 
        **geometry_tag:** tag of the geometry group
        
        **region:** (default nseg 20) There are three methods to create a circle:
        1. [x, y, rad, nseg]
        2. center [x, y] radius nseg 
        3. x value y value rad value nseg value
        
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    # The circle will not be a perfect circle. Instead, it will be approximated by a decagon.
    of.geometry.circle [rock] center [0,0] rad 1.0 segments 10

.. figure:: ../../../images/User_Guide/Circle.png
    :alt: Circle
    :align: center
    :scale: 60%
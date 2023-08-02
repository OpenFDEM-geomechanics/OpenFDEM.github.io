of.geometry.remove.circle
=========================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`geometry.remove.circle` :blue:`*new_geometry_tag*` <string> :blue:`*object_geometry_tag*` <string> :blue:`*region*` <double, double, double, int>
    Remove the geometry in the object by assigning x, y, radius and segments of the circle.
    
    .. note::
        There are three rules to follow:

        - rule 1, the object should already exist.
        
        - rule 2, the region is for the new geometry.
        
        - rule 3, the new object will be removed but the curves will be reserved to refine the mesh size.



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

    of.geometry.remove.circle [tunnel] [rock] center [0,0] rad 1.0 segments 10

.. figure:: ../../../images/User_Guide/Circle_Remove.png
    :alt: Circle_Removes
    :align: center
    :scale: 60%
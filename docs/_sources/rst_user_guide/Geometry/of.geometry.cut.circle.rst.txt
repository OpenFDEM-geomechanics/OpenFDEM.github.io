of.geometry.cut.circle
======================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`geometry.cut.circle` :blue:`*new_geometry_tag*` <string> :blue:`*object_geometry_tag*` <string> :blue:`*region*` <double, double, double, int>
    Remove a geometry in existing geometry using the square method.
    
    .. note::
        
        There are three rules to follow:

        - rule 1, the object should already exist.
        
        - rule 2, the region is for the new geometry.
        
        - rule 3, it only cuts the object into several parts, but the fragments still have the object tag nseg, which is 20 by default.



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

    of.geometry.cut.circle [tunnel] [rock] center [0,0] rad 1.0 segments 10

.. figure:: ../../../images/User_Guide/Circle_Cut.png
    :alt: Circle_Cut
    :align: center
    :scale: 60%
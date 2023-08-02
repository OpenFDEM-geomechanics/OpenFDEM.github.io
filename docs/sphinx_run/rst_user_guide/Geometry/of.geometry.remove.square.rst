of.geometry.remove.square
=========================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`geometry.remove.square` :blue:`*new_geometry_tag*` <string> :blue:`*object_geometry_tag*` <string> :blue:`*region*` <double, double, double, double>
    Remove a geometry in existing geometry using the square method.
    
    .. note::
        There are three rules to follow:

        - rule 1, the object should already exist.
        
        - rule 2, the region is for the new geometry.
        
        - rule 3, the new geometry will be removed. The tag is still reserved to mark the intersected edges between two objects.



    **Parameters:** 
        **new_geometry_tag:** tag of the geometry group cut from the original geometry.

        **object_geometry_tag:** tag of the original geometry group
        
        **region:** There are three methods to define a sqaure:
        
        1. [xmin. xmax. ymin, ymax]
        2. x [xmin, xmax] y [ymin, ymax]
        3. xmin value xmax value ymin value ymax value
        
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.geometry.remove.square [tunnel] [rock] x [0 1] y [0 1]

.. figure:: ../../../images/User_Guide/Square_Remove.png
    :alt: Square
    :align: center
    :scale: 60%
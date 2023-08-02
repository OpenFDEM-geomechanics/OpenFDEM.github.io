of.geometry.square
==================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`geometry.square` :blue:`*geometry_tag*` <string> :blue:`*region*` <double, double, double, double>
    Create a geometry by assigning xmin, xmax, ymin and ymax of the box.


    **Parameters:** 
        **geometry_tag:** tag of the geometry group
        
        **region:** There are three methods to create a square:
        
        1. [xmin. xmax. ymin, ymax]
        2. x [xmin, xmax] y [ymin, ymax]
        3. xmin value xmax value ymin value ymax value
        
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    # Method 1
    of.geometry.square [0 1 0 1]
    # Method 2
    of.geometry.square [rock] x [0 1] y [0 1]
    # Method 3
    of.geometry.square [rock] xmin 0 xmax 1 ymin 0 ymax 1

.. figure:: ../../../images/User_Guide/Square.png
    :alt: Square
    :align: center
    :scale: 60%



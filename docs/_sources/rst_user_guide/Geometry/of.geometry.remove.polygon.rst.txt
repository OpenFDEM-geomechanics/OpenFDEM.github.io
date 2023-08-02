of.geometry.remove.polygon
==========================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.** :red:`geometry.remove.polygon` :blue:`*new_geometry_tag*` <string> :blue:`*object_geometry_tag*` <string> :blue:`*region*` <int, double, double, double, double...>
    |
    Remove a geometry in the object by assigning the N <x> <y> <x> <y>… of the polygon.

    **Parameters:** 
        **new_geometry_tag:** tag of the geometry group cut from the original geometry.

        **object_geometry_tag:** tag of the original geometry group
        
        **region:** Define the points on the polygon: N, [x0,y0] [x1,y1], [x2,y2], [x3, y3]…
        
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.geometry.remove.polygon [tunnel] [rock] 4 [-1 -1] [1,-1] [1,1] [-1,1]



of.geometry.polygon
===================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`geometry.polygon` :blue:`*geometry_tag*` <string> :blue:`*region*` <int, double, double, double, double, ...>
    Create a geometry by assign the N <x> <y> <x> <y>… of the polygon. The polygon will be closed.



    **Parameters:** 
        **geometry_tag:** tag of the geometry group
        
        **region:** Define the points on the polygon: N, [x0,y0] [x1,y1], [x2,y2], [x3, y3]…
        
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.geometry.polygon [rock] 4 [-1 -1] [1,-1] [1,1] [-1,1]


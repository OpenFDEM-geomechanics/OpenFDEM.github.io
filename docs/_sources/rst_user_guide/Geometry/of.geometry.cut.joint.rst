of.geometry.cut.joint
=====================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.** :red:`geometry.cut.joint` :blue:`*new_geometry_tag*` <string> :blue:`*object_geometry_tag*` <string> :blue:`*region*` <double, double, double, double...>
    |
    Cut a joint in an object by assign the <x> <y> <x> <y>…

    **Parameters:** 
        **new_geometry_tag:** tag of the geometry group cut from the original geometry.

        **object_geometry_tag:** tag of the original geometry group
        
        **region:** Define the points on the joints: [x0,y0] [x1,y1], [x2,y2], [x3, y3]…
        
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.geometry.cut.joint 'joint' 'tock' [0,1] [2,3]



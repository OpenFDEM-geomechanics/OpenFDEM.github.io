of.geometry.remove.table
========================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.** :red:`geometry.remove.table` :blue:`*new_geometry_tag*` <string> :blue:`*object_geometry_tag*` <string> :blue:`*table_tage*` <string>
    |
    remove a geometry by assign the N <x> <y> <x> <y>… of the polygon from a table, all the nodes in the table will be closed.

    **Parameters:** 
        **new_geometry_tag:** tag of the geometry group cut from the original geometry.

        **object_geometry_tag:** tag of the original geometry group
        
        **region:** Define the points on the polygon: N, [x0,y0] [x1,y1], [x2,y2], [x3, y3]… The polygon will be closed.
        
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.geometry.remove.table [tunnel] [rock] 'moutain'
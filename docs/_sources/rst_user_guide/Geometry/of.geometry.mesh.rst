of.geometry.mesh
================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`geometry.mesh` :blue:`*mesh_algorithm*` <string> :blue:`*order*` <int>
    Set the method to create mesh. 

    **Parameters:** 
        **mesh_algorithm:** (default delaunay) delaunay. meshadapt, frontal-delaunay
        
        **order:** (default 1) The order can be set to 2 or 3 to generate higher order elements.
        
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    # Default
    of.geometry.mesh delaunay
    # Alternative choice
    of.gemetry.mesh meshadapt order 2



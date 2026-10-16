of.mesh.voronoi
===============

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`mesh.voronoi`
    Change the Delaunay mesh to a Voronoi mesh. All group information is
    cleared after this mesh processing, so entities should be regrouped.
    The current parser does not read an element-group argument; the command
    applies to the entire mesh.

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.mesh.voronoi



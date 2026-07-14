of.mesh.voronoi
===============

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`blast.position` :blue:`*element_tag*` <string> 
    Change the delaunay element to Voronoi element. All the group information will be cleared after this mesh processing. You should regroup all the entities. This command only supports entire mesh processing.
    
    **Parameters:** 
        **element:** tag of the elements.
        
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.mesh.voronoi [rock]



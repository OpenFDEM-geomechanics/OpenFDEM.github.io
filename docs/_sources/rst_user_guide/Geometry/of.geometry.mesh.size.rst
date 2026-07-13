of.geometry.mesh.size
=====================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`geometry.mesh.size` :blue:`*group_tag*` <string> :blue:`*mesh_size*` <Real>
    Set the mesh size to the tags. If use default means the global mesh size, you can also set a different value for the zone you want to refine.


    **Parameters:** 
        **geometry_tag:** tag of the geometry group
        
        **mesh_size:** the mesh size for global or local area.
        
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    # Global Mesh Size
    of.geometry.mesh.size [default] 0.03
    # Mesh Size at the User Defined Area
    of.geometry.mesh.size [refineLine] 0.001



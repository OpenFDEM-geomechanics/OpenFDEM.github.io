of.mesh.implicit
================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`mesh.implicit` :blue:`*mesh_group_tag1*` <string> [*mesh_group_tag2* <string> ...]
    Enable implicit cohesive insertion/remeshing for the selected mesh groups.

    **Parameters:**
        **mesh_group_tag:** one or more existing mesh-group tags.

Example:
--------------------------------------------------------------------

.. code-block::

    of.mesh.implicit 'all'

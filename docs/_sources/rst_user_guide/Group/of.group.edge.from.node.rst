of.group.edge.from.node
=======================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`group.edge.from.node` :blue:`*edge_group_tag*` <string> :blue:`*nodal_group_tag*` <string>
    Create an edge group from the edges attached to a nodal group.

    **Parameters:**
        **edge_group_tag:** (default none) new edge group tag.

        **nodal_group_tag:** source nodal group tag.

Example:
--------------------------------------------------------------------

.. code-block::

    of.group.edge.from.node 'boundary_edges' 'boundary_nodes'

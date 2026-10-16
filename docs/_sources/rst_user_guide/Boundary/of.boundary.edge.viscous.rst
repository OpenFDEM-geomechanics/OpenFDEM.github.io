of.boundary.edge.viscous
========================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`boundary.edge.viscous` :blue:`*edge_tag*` <string> :blue:`normal` :blue:`shear`
    Apply a viscous/absorbing boundary to an edge group. The command
    automatically enables the dynamic module.

    **Parameters:**
        **edge_tag:** (default none) tag of the edge group.

        **normal:** select the local normal direction for absorbing action.

        **shear:** select the local shear direction for absorbing action.

Example:
--------------------------------------------------------------------

.. code-block::

    of.boundary.edge.viscous 'bottom' normal shear

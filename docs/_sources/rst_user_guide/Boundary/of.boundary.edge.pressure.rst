of.boundary.edge.pressure
=========================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`boundary.edge.pressure` :blue:`*edge_tag*` <string> :blue:`normal` <double> :blue:`shear` <double> :blue:`ntable` <string_tag> :blue:`stable` <string_tag> :blue:`nfunction` <quoted string> :blue:`sfunction` <quoted string>
    Apply normal and/or shear pressure to an edge group. The values can be
    time-dependent when tables or functions are used.

    **Parameters:**
        **edge_tag:** (default none) tag of the edge group.

        **normal:** (default 0.0) normal pressure component or amplitude.

        **shear:** (default 0.0) shear pressure component or amplitude.

        **ntable:** (default -1) time-dependent normal pressure table.

        **stable:** (default -1) time-dependent shear pressure table.

        **nfunction:** (default none) time-dependent normal pressure function.

        **sfunction:** (default none) time-dependent shear pressure function.

Example:
--------------------------------------------------------------------

.. code-block::

    of.boundary.edge.pressure 'top_edge' normal 1.0e6

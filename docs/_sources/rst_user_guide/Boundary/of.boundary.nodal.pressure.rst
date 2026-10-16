of.boundary.nodal.pressure
==========================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`boundary.nodal.pressure` :blue:`*nodal_tag*` <string> :blue:`normal` <double> :blue:`shear` <double> :blue:`ntable` <string_tag> :blue:`stable` <string_tag> :blue:`nfunction` <quoted string> :blue:`sfunction` <quoted string>
    Apply normal and/or shear pressure to the boundary edges associated with
    a nodal group. Tables and functions are accepted in the same way as the
    edge pressure boundary.

    **Parameters:**
        **nodal_tag:** (default none) tag of the nodal group.

        **normal:** (default 0.0) normal pressure component or amplitude.

        **shear:** (default 0.0) shear pressure component or amplitude.

        **ntable:** (default -1) time-dependent normal pressure table.

        **stable:** (default -1) time-dependent shear pressure table.

        **nfunction:** (default none) time-dependent normal pressure function.

        **sfunction:** (default none) time-dependent shear pressure function.

Example:
--------------------------------------------------------------------

.. code-block::

    of.boundary.nodal.pressure 'top_nodes' normal 1.0e6

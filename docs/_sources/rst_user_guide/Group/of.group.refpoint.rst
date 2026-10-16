of.group.refpoint
=================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`group.refpoint` :blue:`*group_tag*` <string>
    Group reference points using the supported geometric ranges.

    ``circle.in``, ``circle.on``, ``circle.out``, ``box.in``,
    ``plane.on``, ``plane.above``, ``plane.below``, polygon ranges and
    ``bycoord`` are dispatched by the current parser. The reference points
    must already exist.

Example:
--------------------------------------------------------------------

.. code-block::

    of.group.refpoint [ring_points] range circle.on center [0.0 0.0] radius 1.0

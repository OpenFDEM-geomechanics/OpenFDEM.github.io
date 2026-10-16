of.mesh.insert.internal
=======================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`mesh.insert.internal` :blue:`*element_tag*` <string>
    Insert cohesive elements only between adjacent elements belonging to the
    selected mesh region. This mode is intended for a selected internal
    material/element region and avoids inserting cohesive elements merely
    because an interface touches an unselected region.

    **element_tag:** one or more existing element-group tags.

Example:
--------------------------------------------------------------------

.. code-block::

    of.mesh.insert.internal [rock]

.. Run after mesh and element groups exist. The parser sets the cohesive
.. model flag, performs internal insertion, then transfers common-node and
.. boundary information. Precise interface-selection behavior lives in the
.. mesh module and still needs a small-model runtime check.

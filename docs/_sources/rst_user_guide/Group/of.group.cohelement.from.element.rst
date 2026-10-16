of.group.cohelement.from.element
================================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`group.cohelement.from.element` :blue:`*group_tag*` <string> :blue:`*element_group_a*` <string> :blue:`*element_group_b*` <string>
    Group cohesive elements located between two element groups.

    **Parameters:**
        **group_tag:** (default none) new cohesive-element group tag.
        **element_group_a:** first element group tag.
        **element_group_b:** second element group tag.

Example:
--------------------------------------------------------------------

.. code-block::

    of.group.cohelement.from.element 'quartz_mica' 'quartz' 'mica'

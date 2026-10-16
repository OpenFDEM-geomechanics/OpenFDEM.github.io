of.group.refpoint.bool
======================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`group.refpoint.bool.union` :blue:`*result_tag*` <string> :blue:`*group_a*` <string> :blue:`*group_b*` <string>
    Perform boolean operations on reference-point groups.


**of.**\ :red:`group.refpoint.bool.intersect` :blue:`*result_tag*` <string> :blue:`*group_a*` <string> :blue:`*group_b*` <string>
    Perform boolean operations on reference-point groups.


**of.**\ :red:`group.refpoint.bool.subtract` :blue:`*result_tag*` <string> :blue:`*group_a*` <string> :blue:`*group_b*` <string>
    Perform boolean operations on reference-point groups.

    **Parameters:**
        **result_tag:** (default none) new reference-point group tag.

        **group_a:** first input group tag.

        **group_b:** second input group tag.

Example:
--------------------------------------------------------------------

.. code-block::

    of.group.refpoint.bool.union 'combined' 'left' 'right'
    of.group.refpoint.bool.intersect 'common' 'left' 'right'
    of.group.refpoint.bool.subtract 'difference' 'left' 'right'

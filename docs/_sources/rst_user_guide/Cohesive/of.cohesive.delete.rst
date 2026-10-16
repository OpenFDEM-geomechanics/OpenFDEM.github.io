of.cohesive.delete
==================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`cohesive.delete` :blue:`*cohesive_group_tag*` <string>
    Mark all cohesive elements in the specified cohesive-element group as
    broken.

    **Parameters:**
        **cohesive_group_tag:** (default none) tag of an existing cohesive
        element group.

Example:
--------------------------------------------------------------------

.. code-block::

    of.cohesive.delete 'precrack'

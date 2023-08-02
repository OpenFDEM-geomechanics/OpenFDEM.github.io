of.group.nodal.from.element
===========================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`group.nodal.from.element` :blue:`*group_tag*` <string> :blue:`*element_group_tag*` <string>
    |
    Inherit the nodal group from their parent elements. All the nodals of the targeted elements will be group as the new nodal groups.

    **Parameters:** 
        **group_tag:** tag of the group.
        
        **element_group_tag:** element group tag.        
        
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.group.nodal.from.element [rocknodal] [rockelement]


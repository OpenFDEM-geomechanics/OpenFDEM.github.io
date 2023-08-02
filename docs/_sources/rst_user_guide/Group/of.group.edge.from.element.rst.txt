of.group.edge.from.element
==========================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`group.edge.from.element` :blue:`*group_tag*` <string> :blue:`*element_group_tag*` <string>
    |
    Inherit the edge group from their parent elements. All the edges of the targeted elements will be group as the new edge groups.

    **Parameters:** 
        **group_tag:** tag of the group.
        
        **element_group_tag:** element group tag.        
        
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.group.edge.from.element [rockedge] [rockelement]


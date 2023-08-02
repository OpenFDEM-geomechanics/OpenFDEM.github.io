of.group.edge.from.dfn
======================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`group.edge.from.dfn` :blue:`*group_tag*` <string> :blue:`*dfn_group_tag*` <string>
    |
    Inherit the edge group from their parent dfns. All the edges of the targeted dfns will be group as the new edge groups.

    **Parameters:** 
        **group_tag:** tag of the group.
        
        **dfn_group_tag:** dfn group tag.        
        
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.group.edge.from.dfn [rockedge] [dfn2]


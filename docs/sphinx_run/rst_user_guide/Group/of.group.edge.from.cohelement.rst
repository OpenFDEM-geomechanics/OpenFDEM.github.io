of.group.edge.from.cohcohelement
=============================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`group.edge.from.cohelement` :blue:`*group_tag*` <string> :blue:`*cohelement_group_tag*` <string>
    |
    Inherit the edge group from their parent cohelements. All the edges of the targeted cohelements will be group as the new edge groups.

    **Parameters:** 
        **group_tag:** tag of the group.
        
        **cohelement_group_tag:** cohelement group tag.        
        
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.group.edge.from.cohelement [rockedge] [rockcohelement]


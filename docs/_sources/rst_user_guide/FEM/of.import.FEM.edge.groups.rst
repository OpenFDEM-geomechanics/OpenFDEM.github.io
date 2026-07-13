of.import.FEM.edge.groups
=========================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`import.FEM.edge.groups` :blue:`*group_tag*` <string> :blue:`*N*` <int> :blue:`*node_id1*` <int> :blue:`*node_id2*` <int> :blue:`*node_id3*` <int> ...
    |
    Import the edge groups.
    
    **Parameters:** 
        **N:** size of the group

        **node_id:** node ids
    

|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.import.FEM.edge.groups 'rock' 5 1 3 9 15 32




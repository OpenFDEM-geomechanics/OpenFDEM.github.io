of.boundary.edge.clear
======================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`boundary.edge.clear` :blue:`*edge1_tag*` <string> :blue:`*edge2_tag*` <string> :blue:`*edge3_tag*` <string> ...
    |
    Delete the edge boundaries defined previously. Directly set the edge groups.
    
    **Parameters:** 
        **edge_tag:** tag of the edge group

|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.boundary.edge.clear ‘leftedge’ ‘rightedge’ ‘up’ ‘down’


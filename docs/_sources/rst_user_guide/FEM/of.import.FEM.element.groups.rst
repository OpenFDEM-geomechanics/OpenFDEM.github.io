of.import.FEM.element.group
===========================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`import.FEM.element.group` :blue:`*element_tag*` <string> :blue:`*size*` <int> :blue:`*edge_id1*` <int> :blue:`*edge_id2*` <int> :blue:`*edge_id3*` <int> ...
    Import the element groups.
    
    **Parameters:** 
        **element_tag:** tag of elements.

        **size:** size of the groups.

        **edge_id:** edge ids.   


Example:
--------------------------------------------------------------------

.. code-block:: 

    of.import.FEM.element.group 'rock' 5 1 3 9 15 32


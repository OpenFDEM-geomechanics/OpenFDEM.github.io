of.import.FEM.element.connectivity
==================================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`import.FEM.element.connectivity` :blue:`*N*` <int> :blue:`*type*` <int> :blue:`*node_count*` <int> :blue:`*edge_id1*` <int> :blue:`*edge_id2*` <int> :blue:`*edge_id3*` <int> ...
    |
    Import the element connectivity.
    
    **Parameters:** 
        **N:** size of the group.
        
        **type:** type of the element connectivity
        
        +-----------------+-----------------+-----------------+-----------------+
        | Type Number     | Element Type    | Number of Edges | Dimensions      |
        +=================+=================+=================+=================+
        | 1               | LINE2           | 2               | 1               |
        +-----------------+-----------------+-----------------+-----------------+
        | 2               | TRIANGLE3       | 3               | 2               |
        +-----------------+-----------------+-----------------+-----------------+
        | 3               | QUADRANGLE4     | 4               | 2               |
        +-----------------+-----------------+-----------------+-----------------+
        | 4               | TRIANGLE6       | 3               | 2               |
        +-----------------+-----------------+-----------------+-----------------+
        | 5               | QUADRANGLE8     | 4               | 2               |
        +-----------------+-----------------+-----------------+-----------------+
        | 6               | QUADRANGLE9     | 4               | 2               |
        +-----------------+-----------------+-----------------+-----------------+
        | 7               | POLYGON         | node_num        | 2               |
        +-----------------+-----------------+-----------------+-----------------+

        **node_count:** number of nodes.   
        
        **node_id:** node ids.  

|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.import.FEM.element.connectivity 1 2 3 0 10 6


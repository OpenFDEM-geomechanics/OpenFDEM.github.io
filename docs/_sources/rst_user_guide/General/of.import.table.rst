of.import.table
================================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`gravity` :blue:`table_tag` <string> :blue:`file_path` <string>
    Import the table, the file type can be arbitrary.
    
    1. Y-only table
        <Table Type> time [start time, end time] <N data>
        
        <data.0>
        
        <data.1>
        
        ...
    
    2. X-Y table
        <Table Type> <N data>

        <data.x0> <data.y0>
        
        <data.x1><data.y1> 
        
        ...

    
    |
    **Parameters:** 
        **table_tag:** the tag to this table of data.
        
        **file_path:** file path of the table.

**Example:**

.. code-block:: 

    # Example
    of.import.table ‘pwave’ “inputPwave.dat”



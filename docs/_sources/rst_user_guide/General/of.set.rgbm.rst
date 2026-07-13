of.set.rgbm
================================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`set.rGBM` :blue:`*group_count*` <int> :blue:`*group1_name*` <string> :blue:`*greyvalue1*` <int> :blue:`*group2_name*` <string> :blue:`*greyvalue2*` <double>...
    Assign the number of groups for minerals to create the realistic GBM model, and assign the group tags, grey levels for different minerals. The groups are issued to elements. The grey levels ranging from 0 -255 are used for separating different minerals.
    
    |
    **Parameters:** 
        **group_count:** Number of groups will be assigned.
        
        **group_name:** The name of mineral groups.
        
        **greyvalue:** They grey level of mineral ranges from 0-255.

**Example:**

.. code-block:: 

    # Example
    of.set.rGBM 3 ‘Quartz’ 76 ‘Feldspar’ 153 ‘Mica’ 255




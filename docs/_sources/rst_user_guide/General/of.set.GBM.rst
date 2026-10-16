of.set.gbm
================================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`set.gbm` :blue:`*group_count*` <int> :blue:`*group1_name*` <string> :blue:`*ratio1*` <double> :blue:`*group2_name*` <string> :blue:`*ratio2*` <double>...
    Assign the number of groups for minerals in GBM module and assign the group tags and area ratio for different minerals. The groups are issued to elements. The accumulation of all ratios should equal to 1.0.
    
    **Parameters:** 
        **group_count:** Number of groups will be assigned.
        
        **group_name:** The name of mineral groups.
        
        **ratio:** The ratio of mineral in the model. The sum of mineral ratio should be 1.0.

Example:
--------------------------------------------------------------------

.. code-block:: 

    # Example
    of.set.gbm 3 ‘Quartz’ 0.4 ‘Feldspar’ 0.3 ‘Mica’ 0.3

.. note::

    ``of.config.GBM`` is a separate parser command that only enables the GBM
    flag and does not read the group-count arguments shown above.

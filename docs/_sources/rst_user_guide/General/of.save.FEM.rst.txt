of.save.FEM
================================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`save.FEM` :blue:`*file_name*` <string>
    **(Mandetory for in-situ stress problems)** Save the FEM results after in-situ stress equilibrium is reached. This file will write out the mesh information after deformed for the next step excavation. This file avoids rebalancing your model.
    
    |
    **Parameters:** 
        **file_name:** Save the FEM results under this file name.

**Example:**

.. code-block:: 

    # Example
    of.save.FEM ‘insitu.fem’



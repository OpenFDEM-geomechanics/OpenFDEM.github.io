of.set.config
================================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`config` :blue:`*type*` <string> 
    Choose the plane stress or plane strain for the 2D problems. Plane stress is set by default.

    **Parameters:** 
        **type:** (default planestress) 2D problem can be solved based on plane stress or plane strain.


**Example:**

.. code-block:: 

    # Default
    of.set.config planestress
    # Alternative
    of.set.config planestrain




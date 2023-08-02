of.set.module
================================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`set.module` :blue:`*type*` <string> :blue:`*switch*` <bool>
    Turn on or off for special modules.
    
    |
    **Parameters:** 
        **type:** Modules currently available are 'hydro', 'thermal', 'blast' and 'dynamic'. 
        For some special modules which are not listed here, please contact the developer for 
        the access.


**Example:**

.. code-block:: 

    # Hydro modules
    of.set.config hydro on
    of.set.config hydro off

    # Thermal modules
    of.set.config thermal on
    of.set.config thermal off

    # Blast modules
    of.set.config blast on
    of.set.config blast off

    # Dynamic modules
    of.set.config dynamic on
    of.set.config dynamic off




of.damp.global
================================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`damp.global` :blue:`*ratio*` <Real> 
    Set the global damping value to slow down the loading velocity, which is helpful for balance. **The damping value should not be over than 1.0.**
    
    |
    **Parameters:** 
        **ratio:** (default 0.7) Global damping value for slow down the loading velocity.

**Example:**

.. code-block:: 

    # Default
    of.damp.global 0.7



of.timestep
================================
.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`timestep` :blue:`*type*` <string> :blue:`*timestep*` <Real>
    Set the user defined timestep. The type can be “fix” or “auto”. OpenFDEM will compute the default timestep which can result in stable results. Be careful to set the timestep yourself only when you are rather enough understand what’s explicit dynamic modelling.
    
    OpenFDEM will print out the default timestep and give a warning to you if your defined timestep is larger than the default value.
    
    |
    **Parameters:** 
        **type:** (default 'auto') 'auto' provides a timestep size evaluated by OpenFDEM, but users can use 'fix' to set the user defined timestep.
        
        **timestep:** (optional) fixed time step

**Example:**

.. code-block:: 

    # Default
    of.timestep auto
    # Fixed time step
    of.timestep fix 1.0e-9





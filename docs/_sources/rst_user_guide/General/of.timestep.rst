of.timestep
================================
.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`timestep` :blue:`*type*` <string> :blue:`*timestep*` <Real>
    Set the user defined timestep. The type can be ``fix``, ``auto`` or
    ``creep``. OpenFDEM will compute the default timestep which can result in
    stable results. Be careful to set the timestep yourself only when you
    understand explicit dynamic modelling.
    
    OpenFDEM will print out the default timestep and give a warning to you if your defined timestep is larger than the default value.
    
    **Parameters:** 
        **type:** (default ``auto``) ``auto`` updates the mechanical timestep,
        ``fix`` sets a user-defined mechanical timestep, and ``creep`` reads a
        creep timestep value.
        
        **timestep:** (optional) fixed time step

Example:
--------------------------------------------------------------------

.. code-block:: 

    # Default
    of.timestep auto
    # Fixed time step
    of.timestep fix 1.0e-9
    # Creep time step
    of.timestep creep 1.0e-6

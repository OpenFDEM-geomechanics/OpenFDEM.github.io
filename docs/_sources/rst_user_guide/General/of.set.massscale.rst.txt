of.set.massscale
================================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`.set.massscale` :blue:`*mass_scale*` <Real>
    Set the mass scale value to lump the nodal mass and give a larger timestep. That will be useful to balance your model when kinetics is not important. Be careful to use if you are beginner.
    
    |
    **Parameters:** 
        **mass_scale:** (default 1.0) 

**Example:**

.. code-block:: 

    # Default
    of.set.massscale 1.0



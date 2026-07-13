of.set.gravity
================================
.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`gravity` :blue:`x` <double> :blue:`y` <double>
    Add gravity to the model. Gravity is a body force, which is issued by x and y components. Negative is down forward by default.
    
    |
    **Parameters:** 
        **x:** gravitational acceleration in the x directions.
        
        **y:** gravitational acceleration in the y directions.

**Example:**

.. code-block:: 

    # Default
    of.set.gravity x 0.0 y 0.0
    # Method 1
    of.set.gravity x 0.0 y -9.8
    # Method 2
    of.set.gravity y -9.8


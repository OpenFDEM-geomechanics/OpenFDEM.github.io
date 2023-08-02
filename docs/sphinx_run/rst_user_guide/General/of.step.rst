of.step
================================
.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`step` :blue:`*number_of_steps*` <int>
    **(Mandatory Option)** Assign the number of steps for the current run.
    The run will be terminated after the steps reach the assigned count, 
    but the console will not be terminated until it meets *of.finalize*.

    .. note:: 
        Also see the alternative of the mandatory option **of.solve**
    |
    **parameter:**
        **number_of_steps:** the number of steps program will run before termination.
|

**Example:**

.. code-block:: 

    of.step 30000
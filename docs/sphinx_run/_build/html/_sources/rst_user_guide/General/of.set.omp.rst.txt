of.set.omp
================================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`omp` :blue:`*number_of_cores*` <int>
    Assign the count of cores you want to use for CPU parallelization. 
    The parallelization will be turned on only when the computer has 
    more than 2 cores.

    .. note::
        Go Task Manager > Performance > CPU > Cores to check the number of cores your 
        computer has. If nothing is set here, serial computing with 1 core will be used.
    |
    **Parameter**: 
        **number_of_cores:** (default 1) The number of cores will be used for computation.
|

**Example:**

.. code-block:: 

    # Default
    of.set.omp 1
    # Example
    of.set.omp 16

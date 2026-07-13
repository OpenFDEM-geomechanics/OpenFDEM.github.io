of.solve
================================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`solve` :blue:`*mechanical_ratio*` <double>
    **(Mandatory)** Assign the mechanical ratio as the iteration threshold to exit the running. 
    The double value :math:`\zeta` is the ratio of the total maximum unbalance force to the total 
    force. Generally, the ratio less than 1.0e-5 can be considered as the equilibrium state.
    This command is important to determine the equilibrium state in in-situ stress equilibrium 
    or static problems.

    :math:`\zeta = \frac{\sum^n_{i=1}\sqrt{\bar{f_i}}}{\sum^n_{i=1}\sum^n_{j=1}\sqrt{f_{i,j}}}`, :math:`\bar{f_i}` is the unbalanced force on 
    node :math:`i`. :math:`j` are types of the nodal forces. :math:`f_{i,j}` is the :math:`j` th type force on node :math:`i`.  

    |    
    .. note:: 
        Also see the alternative of the mandatory option **of.step**
    |
    **Parameter**: 
        **mechanical ratio**: (default 0.0001) the maximum ratio between the total maximum unbalance force to 
        the total force before termination. 

|

**Example:**

.. code-block::

    # Default 
    of.solve 0.0001

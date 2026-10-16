of.solve.step / of.solve.ratio / of.solve.time
===============================================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

The current parser provides three solve modes.

**of.**\ :red:`solve.step` :blue:`*steps*` <int>
    Run for the specified number of steps. ``of.step`` is retained as a
    compatibility alias.


**of.**\ :red:`solve.ratio` :blue:`*mechanical_ratio*` <double>
    Stop when the mechanical unbalance ratio reaches the specified value.
    The ratio is the total maximum unbalanced force divided by the total
    force. This is useful for in-situ stress equilibrium and static problems.


**of.**\ :red:`solve.time` :blue:`*time*` <double>
    Run until the specified physical time has been reached.

Example:
--------------------------------------------------------------------

.. code-block::

    # Run 2000 steps
    of.solve.step 2000

    # Solve to a mechanical ratio
    of.solve.ratio 1.0e-5

    # Run for a physical time
    of.solve.time 0.002

.. The old page documented of.solve <ratio>. Direct of.solve needs runtime
.. verification before documenting it as fully supported.

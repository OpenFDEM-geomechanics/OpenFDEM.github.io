of.import.function
==================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`import.function` :blue:`*function_tag*` <string> :blue:`*expression*` <quoted string>
    Register a time-dependent function for later boundary/history use.

    **Parameters:**
        **function_tag:** (default none) function name used later by commands.

        **expression:** time-dependent expression, quoted.

Example:
--------------------------------------------------------------------

.. code-block::

    of.import.function 'pulse' 'sin(2.0*pi*time)'

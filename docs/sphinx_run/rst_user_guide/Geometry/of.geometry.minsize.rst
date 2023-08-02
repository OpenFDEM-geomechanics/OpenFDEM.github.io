of.geometry.minsize
===================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`geometry.minsize` :blue:`*minsize*` <Real> 
    Set the minsize to delete the bad segments for jsets and dfns.

    **Parameters:** 
        **minsize:** Bad segments under this threshold will be deleted.

|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.geometry.minsize 1e-3
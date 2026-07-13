of.history.pv.dynamic.interval
==============================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`history.pv.dynamic.interval` :blue:`global` <int> :blue:`threshold` <int> :blue:`reduce` <int>
    Set the dynamic result writing intervals by the increasing broken CZM.

    **Parameters:** 
        **global:** (default 1000) output intervals.
        
        **threshold:** threshold for the minimum interval.

        **reduce:** step of reducing.

    
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.history.pv.dynamic.interval global 20000 threshold 100 reduce 200
    of.history.pv.dynamic.interval [20000 100 200]



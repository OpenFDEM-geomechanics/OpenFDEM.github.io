of.history.pv.ae
================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`history.pv.ae` :blue:`*tag1*` <string> :blue:`*tag2*` <string> :blue:`*tag3*` <string> ...
    Set the items you want to write in ParaView results (See the list below). It can be used when AE mode is turned on.
    
    Field keywords:
    
    - default (Output all)
    
    - mode

    - time

    - win_time

    - win_kinetic

    - kinetic

    - magnitude

    - energy

    
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.history.pv.ae default
    of.history.pv.ae 'mode' 'time' 'magnitude'



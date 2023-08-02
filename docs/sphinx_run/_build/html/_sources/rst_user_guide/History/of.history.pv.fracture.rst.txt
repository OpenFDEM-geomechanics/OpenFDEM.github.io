of.history.pv.fracture
======================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`history.pv.fracture` :blue:`*tag1*` <string> :blue:`*tag2*` <string> :blue:`*tag3*` <string> ...
    Set the items you want to write in ParaView results (See the list below).
    
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

    of.history.pv.fracture default
    of.history.pv.fracture 'mode' 'time' 'magnitude'



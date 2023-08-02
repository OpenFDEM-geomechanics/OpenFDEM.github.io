of.history.pv.damage
====================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`history.pv.damage` :blue:`*tag1*` <string> :blue:`*tag2*` <string> :blue:`*tag3*` <string> ...
    Set the items you want to write in ParaView results (See the list below).
    
    Field keywords:
    
    - default (Output all)
    
    - mode

    - sliding

    - opening

    - area

    - time

    - length
    
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.history.pv.damage default
    of.history.pv.damage 'mode' 'time' 'length'



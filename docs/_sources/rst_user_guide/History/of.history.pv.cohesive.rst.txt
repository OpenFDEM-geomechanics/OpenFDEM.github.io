of.history.pv.cohesive
======================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`history.pv.cohesive` :blue:`*tag1*` <string> :blue:`*tag2*` <string> :blue:`*tag3*` <string> ...
    Set the items you want to write in ParaView results (See the list below).
    
    Field keywords:
    
    - default (Output all)
    
    - velocity

    - force

    - displacement

    - shear_strength

    - dfn

    - mat_id

    - group


|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.history.pv.cohesive 'default'
    of.history.pv.cohesive 'velocity' 'force' 'displacement'




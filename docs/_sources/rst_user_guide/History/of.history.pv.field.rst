of.history.pv.field
===================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`history.pv.field` :blue:`*tag1*` <string> :blue:`*tag2*` <string> :blue:`*tag3*` <string> ...
    Set the items you want to write in ParaView results (See the list below).
    
    Field keywords:
    
    - default (Output all)
    
    - velocity

    - force
    
    - displacement
    
    - fluid_pressure – only for hydro
    
    - nodal_group
    
    - element_group
    
    - gbm_group
    
    - mass
    
    - stress
    
    - strain
    
    - strain_rate
    
    - principal_stress
    
    - mat_id
    
    - fragment
    
    - temperature – only for thermal
    
    - thermal-flux – only for thermal
    
    - t0 – only for thermal


    
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.history.pv.field 'default'
    of.history.pv.field 'velocity' 'force' 'displacement'




of.boundary.nodal.clear
=======================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`boundary.nodal.clear` :blue:`*nodal1_tag*` <string> :blue:`*nodal2_tag*` <string> :blue:`*nodal3_tag*` <string> ...
    |
    Delete the nodal boundaries defined previously. Directly set the nodal groups.
    
    **Parameters:** 
        **nodal_tag:** tag of the nodal group

|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.boundary.nodal.clear ‘leftedge’ ‘rightedge’ ‘up’ ‘down’
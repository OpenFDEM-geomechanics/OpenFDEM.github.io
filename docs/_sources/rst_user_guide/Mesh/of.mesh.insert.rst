of.mesh.insert
==============

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`mesh.insert` :blue:`*element_tag*` <string> 
    Insert cohesive in the target element groups. OpenFDEM support partially insert CZMs.
    
    **Parameters:** 
        **element_tag:** tag of the elements.
        
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.mesh.insert [default]
    of.mesh.insert [rock]



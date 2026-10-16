of.mesh.insert
==============

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`mesh.insert` :blue:`*element_tag*` <string>
    Insert cohesive elements using the selected mesh groups. The selected
    groups are passed to the standard cohesive insertion mode.
    
    **Parameters:** 
        **element_tag:** tag of the elements.
        

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.mesh.insert [default]
    of.mesh.insert [rock]

.. note::

    For insertion restricted to internal interfaces of the selected region,
    use :doc:`of.mesh.insert.internal<of.mesh.insert.internal>`.



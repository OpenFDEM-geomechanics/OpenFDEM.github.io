of.boundary.element.clear
=========================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`boundary.element.clear` :blue:`*element_tag1*` <string> :blue:`*element_tag2*` <string> :blue:`*element_tag3*` <string> ...
    |
    Delete the element boundaries defined before. Directly set the element groups
    
    **Parameters:** 
        **element_tag:** tag of the group to be cleared.
    
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.element.clear 'rock' 'soil' 


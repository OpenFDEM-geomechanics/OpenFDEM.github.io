of.mesh.split
=============

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`mesh.split` :blue:`*element_tag*` <string> 
    Insert contacts within the element tags and no cohesive elements will be created. The target element group will be changed to discrete bodies.
    
    **Parameters:** 
        **element_tag:** tag of the elements.
        
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.mesh.split [rock]



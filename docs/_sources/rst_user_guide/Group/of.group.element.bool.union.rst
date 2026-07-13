of.group.element.bool.union
===========================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`group.element.bool.union` :blue:`*group_tag*` <string> :blue:`tag1` <string> :blue:`tag2` <string> ...
    |
    Get the bool union of the second - last element groups and store them into the first tags.
    
    **Parameters:** 
        **group_tag:** tag of the group.
        
        **tag:** element groups to be operated.
        
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.group.element.bool.union [rock] [rock_up] [rock_down] [rock_left] [rock_right]


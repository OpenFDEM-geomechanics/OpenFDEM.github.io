of.blast.position
=================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`blast.position` :blue:`*borehole_tag*` <string> :blue:`x` <double> :blue:`y` <double> :blue:`radius` <double>
    Create a blast borehole by its center and radius.
    
    **Parameters:** 
        **borehole_tag:** tag of the group
        
        **x:** x coordinate of the center of the borehole
        
        **y:** y coordinate of the center of the borehole
        
        **radius:** the radius of the borehole.
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.blast.position ‘borehole1’ x 0.0 y 0.0 radius 1.0


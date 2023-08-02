of.boundary.blast
=================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`blast.position` :blue:`*borehole_tag*` <string> :blue:`p0` <double> :blue:`table` <string>
    Create the blast borehole boundaries from table.
    
    **Parameters:** 
        **borehole_tag:** tag of the group
        
        **p0:** initial position.
        
        **table:** time dependent position.
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.boundary.blast 'borehole1' p0 1.0 table 'pwave'


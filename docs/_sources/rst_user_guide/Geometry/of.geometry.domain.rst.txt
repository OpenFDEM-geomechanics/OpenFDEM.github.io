of.geometry.domain
==================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`geometry.domain` :blue:`region` <double, double, double, double>
    Create a geometry domain by assigning xmin, xmax, ymin and ymax of the box.


    **Parameters:**      
        **region:** geometry domain for creating the joints. There are three methods to define the domain:
        1. [xmin. xmax. ymin, ymax]
        2. x [xmin, xmax] y [ymin, ymax]
        3. xmin value xmax value ymin value ymax value
        
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.geometry.domain x [0 1] y [0 1]



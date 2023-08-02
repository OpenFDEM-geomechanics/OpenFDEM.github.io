of.import.FEM.nodal.coord
=========================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`import.FEM.nodal.coord` :blue:`*N*` <int> :blue:`*x0*` <double> :blue:`*y0*` <double> :blue:`*x1*` <double> :blue:`*y1*` <double> ...
    |
    Import the nodal results after deformation by knowing node count and initial coordinates.
    
    **Parameters:** 
        **N:** size of the group

        **x:** x coordinates

        **y:** x coordinates     

|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.import.FEM.nodal.coord 2 0.322 0.544 0.233 0.543


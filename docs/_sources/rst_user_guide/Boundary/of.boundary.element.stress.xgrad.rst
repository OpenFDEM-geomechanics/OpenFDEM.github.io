of.boundary.element.stress.xgrad
================================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`boundary.element.stress.xgrad` :blue:`*element_tag*` <string> :blue:`xx` <double> :blue:`xy` <double> :blue:`yy` <double>
    |
    Create the in-situ stress gradient in x direction on the assigned element groups.
    
    **Parameters:** 
        **element_tag:** tag of the group
        
        **xx:** (default 0.0) In-situ stress in the xx direction
        
        **xy:** (default 0.0) In-situ stress in the xy direction
        
        **yy:** (default 0.0) In-situ stress in the yy direction
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    # the rock is under 10 MPa in x direction and 30 MPa is y direction. Negative is compression.
    of.boundary.element.stress.xgrad ‘rock’ xx -10e6 yy -30e6   


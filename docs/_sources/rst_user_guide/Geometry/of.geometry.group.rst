of.geometry.group
=================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`geometry.group` :blue:`*geometry_tag*` <string> :blue:`*method*` <string> :blue:`*region*` <double, double, ...> ...
    Set group of the points in gmsh to set the new mesh size, the method includes.

    **Parameters:** 
        **geometry_tag:** tag of the geometry group
        
        **method:** 
        
        -box.in/box.on/box.out
    
        -circle.in/circle.on/circle.out
        
        -plane.on/plane.above/plane.below

        **region:**

        The region for box can be set as 
        
        - x [xmin xmax] y [ymin ymax] or
        
        - [xmin xmax ymin ymax]

        The region for circle can be set as 
        
        - center [x,y] radius or 

        - [x,y,radius]
        
        The region for plane can be set as 
        
        - p1 [x0,y0] p2 [x1,y1] or 
        
        - [x0,y0,x1,y1]

    .. note::
        
        - rule 1, the group of geometry is used for point only,

        - rule 2, the previous lines or surfaces also are inherited to groups

        - rule 3, the group information is updated after the entity fragmentation

|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.geometry.group [refine] range box.in x [0,1] y [0,1]


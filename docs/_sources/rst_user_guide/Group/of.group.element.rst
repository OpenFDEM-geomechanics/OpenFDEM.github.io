of.group.element
================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`group.element` :blue:`*group_tag*` <string> :blue:`*method*` <string> :blue:`*region*` <double, double, ...> ...
    **Parameters:** 
        **group_tag:** tag of the group.
        
        **method:** 
        
        -box.in
    
        -circle.in/circle.out
        
        -plane.above/plane.below

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
        
        - rule 1: it is illegal to use the same tags for one type of entity.
        
        - rule 2: the node group also be inherited from your input mesh file.
        
        - rule 3: the node groups can be done before the mesh processing. The group information will be transferred to the new inserted nodes automatically.

        

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.group.element [rock] range box.in x [0,1] y [0,1]

.. note::

    The current parser rejects ``box.on``, ``box.out``, ``circle.on`` and
    ``plane.on`` for ordinary element groups. ``circle.on`` is available for
    nodal, edge and cohesive-element groups, but not for
    ``of.group.element``.


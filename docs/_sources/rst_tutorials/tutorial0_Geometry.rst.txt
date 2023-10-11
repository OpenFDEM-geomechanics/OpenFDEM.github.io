How to create a geometry
########################################

OpenFDEM supports users to create all types of 2D geometries by using basic geometry types such as squares 
and circles or even polygons with Boolean operation to cut or remove one geometry from another. All syntaxes 
of creating geometries are explained in the command reference. A simple geometry as shown below will be created 
in this tutorial.

.. figure:: ../../images/Desmos/Geometry.png
    :alt: Create Geometry
    :align: center


    Figure 1: Create Geometry

==================================
1 Code
==================================

.. warning::

    Please note that, all the setting in the example is based on the developer's computer. You may need to change 
    these details based on your own environment.

To start with programming, create a new empty input file or copy it from the existing examples (later add the ``.of`` extension). Begin writing the following commands:

-------------------------------------------------------------------
2.1 Initialize the model
-------------------------------------------------------------------
1 Create a new run and clean up the old memories.

.. literalinclude:: examples/CreateGeometry/runme.of
    :lines: 39

2. Set up the folder name to save your results. Here the folder name is set to be “result”.

.. literalinclude:: examples/CreateGeometry/runme.of
    :lines: 43

3. Set the number of cores to be used for running this model in parallelization.

.. literalinclude:: examples/CreateGeometry/runme.of
    :lines: 48

4. Set the geometry domain.

.. literalinclude:: examples/CreateGeometry/runme.of
    :lines: 51

-------------------------------------------------------------------
2.2 Create the geometry
-------------------------------------------------------------------

1. Create a sqaure block and call it "rock".

.. literalinclude:: examples/CreateGeometry/runme.of
    :lines: 57

|
.. figure:: ../../images/Gmsh/Geo_Rect.png
    :alt: Create a square
    :align: center


    Figure 2: Create a square


2. Remove a circular tunnel at the top right corner.

.. literalinclude:: examples/CreateGeometry/runme.of
    :lines: 60

|
.. figure:: ../../images/Gmsh/Geo_Circle.png
    :alt: Remove a circle
    :align: center


    Figure 3: Remove a circle

3. Remove a rectangular tunnel at the top left corner.

.. literalinclude:: examples/CreateGeometry/runme.of
    :lines: 63

|
.. figure:: ../../images/Gmsh/Geo_Rect2.png
    :alt: Remove a rectangle
    :align: center


    Figure 4: Remove a rectangle

4. Cut an arc at the center.

.. literalinclude:: examples/CreateGeometry/runme.of
    :lines: 66

|
.. figure:: ../../images/Gmsh/Geo_Arc.png
    :alt: Cut an arc
    :align: center


    Figure 5: Cut an arc

5. Cut a rectangle underneath the arc.

.. literalinclude:: examples/CreateGeometry/runme.of
    :lines: 67

|
.. figure:: ../../images/Gmsh/Geo_Tunnel.png
    :alt: Cut a rectangle
    :align: center


    Figure 6: Cut a rectangle

-------------------------------------------------------------------
2.3 Create the mesh
-------------------------------------------------------------------

1. Assign the mesh size and create the mesh

.. literalinclude:: examples/CreateGeometry/runme.of
    :lines: 70-71

2. Finalize the model and clear memory

.. literalinclude:: examples/CreateGeometry/runme.of
    :lines: 74

==================================
2 Full Script
==================================

- `Create_Geometry.of`_ (click to download from GitHub)

.. _Create_Geometry.of: https://github.com/OpenFDEM-geomechanics/Examples/blob/main/CreateGeometry/runme.of

.. literalinclude:: examples/CreateGeometry/runme.of
    :lines: 37-73

|

.. raw:: html

   <script src="//clustrmaps.com/globe.js?d=IJDdJTOZeBy5TaHUiVkIm7GLGSulnk0C2NzaC4-34QA">
   </script>
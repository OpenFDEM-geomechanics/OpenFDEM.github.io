Tutorial 4: Brazilian Disc Test
########################################
Brazilian disc test is an indirect test method for assessing the tensile strength. 

.. figure:: ../../images/Desmos/BD_Test.png
    :alt: Geometry of the Brazilian disc test
    :align: center
    :scale: 40%

    Figure 1: Geometry of the Brazilian disc test

|

==================================
1.0 Tutorial Prerequistes
==================================
The following files are needed to follow along the tutorial:

- `example_br.geo`_ (click to download from GitHub)

.. _example_br.geo: https://github.com/OpenFDEM-geomechanics/Examples/blob/main/CreateBrazilianDiscTest/example_br.geo


==================================
2.0 Main Steps
==================================

#. Initialize the model.
#. Import the geometry and the mesh
#. Assign material properties.
#. Create the group
#. Assign boundary conditions.
#. Set the outputs.

==================================
3.0 Codes
==================================
Please note that, all the setting in the example is based on the developer's computer. You may need to change 
these setting based on your own conditions.

To start with programming, create a new empty text file (later add the `.of` extension). Begin writing the following commands:

-------------------------------------------------------------------
3.1 Initialize the model
-------------------------------------------------------------------
#. Create a new run and clean up the old memories.
    .. literalinclude:: ../../../src/examples/CreateBrazilianDiscTest/runme.of
        :lines: 39

#. Set up the folder name to save your results. Here the folder name is set to be “result”.
    .. literalinclude:: ../../../src/examples/CreateBrazilianDiscTest/runme.of
        :lines: 43


#. Set the number of cores to be used for running this model.
    .. warning::
        In this example, 15 cores will be used for running. To prevent the crushing of your computer, please 
        check your computer to fill in the number of cores you want to use from your computer. To check the number 
        of cores your computer has, you can go Task Manager > Performance > CPU > Cores. If nothing is set here, 
        serial computing will be used.
    .. literalinclude:: ../../../src/examples/CreateBrazilianDiscTest/runme.of
        :lines: 47

-------------------------------------------------------------------
3.2 Import the geometry and the mesh
-------------------------------------------------------------------
#. Import the geometry and mesh of the model from the "example_br.geo" file. The final geometry will be the same as Figure 1 shown.
    .. literalinclude:: ../../../src/examples/CreateBrazilianDiscTest/runme.of
        :lines: 51
#. Group the elements to rock, top platen and bottom platen.
    .. literalinclude:: ../../../src/examples/CreateBrazilianDiscTest/runme.of
        :lines: 54-56
#. Insert the cohesive elements to the mesh.
    .. literalinclude:: ../../../src/examples/CreateBrazilianDiscTest/runme.of
        :lines: 59

-------------------------------------------------------------------
3.3 Assign Material Properties
-------------------------------------------------------------------
The material properties of this model is shown as the table below:

+---------------------------------------------+------------------------+
| Parameter                                   | Value                  |
+=============================================+========================+
| **Continuum Triangular Elements - Rock**    |                        |
+---------------------------------------------+------------------------+
| model                                       | elastic                |
+---------------------------------------------+------------------------+
| density (:math:`kg/m^3`)                    | 2700                   |
+---------------------------------------------+------------------------+
| E (Pa)                                      | 30e9                   |
+---------------------------------------------+------------------------+
| :math:`\nu`                                 | 0.3                    |
+---------------------------------------------+------------------------+
| damp                                        | 0.6                    |
+---------------------------------------------+------------------------+
|                                             |                        |
+---------------------------------------------+------------------------+
| **Continuum Triangular Elements - Platens** |                        |
+---------------------------------------------+------------------------+
| model                                       | rigid                  |
+---------------------------------------------+------------------------+
| density (:math:`kg/m^3`)                    | 7000                   |
+---------------------------------------------+------------------------+
|                                             |                        |
+---------------------------------------------+------------------------+
| **Cohesive Material Properties**            |                        |
+---------------------------------------------+------------------------+
| model                                       | EM                     |
+---------------------------------------------+------------------------+
| tension (Pa)                                | 1e6                    |
+---------------------------------------------+------------------------+
| cohesion (Pa)                               | 3e6                    |
+---------------------------------------------+------------------------+
| friction                                    | 0.3                    |
+---------------------------------------------+------------------------+
| GI (:math:`J/m^2`)                          | 10                     |
+---------------------------------------------+------------------------+
| GII (:math:`J/m^2`)                         | 50                     |
+---------------------------------------------+------------------------+
|                                             |                        |
+---------------------------------------------+------------------------+
| **Contact Material Properties**             |                        |
+---------------------------------------------+------------------------+
| model                                       | MC                     |
+---------------------------------------------+------------------------+
| friction                                    | 0.3                    |
+---------------------------------------------+------------------------+



.. note::
    Check :doc:`element materal<../rst_user_guide/Material/of.mat.element>`, :doc:`cohesive materal<../rst_user_guide/Material/of.mat.cohesive>`, :doc:`contact materal<../rst_user_guide/Material/of.mat.contact>` to see more materials.


#. Set the material properties. For this test, the example uses the elastic constitutive model and assigned material for CZM and contact.
    .. literalinclude:: ../../../src/examples/CreateBrazilianDiscTest/runme.of
        :lines: 63-65, 67, 69

-------------------------------------------------------------------
3.4 Create Groups and Assign Boundary Conditions
-------------------------------------------------------------------
#. Group the nodes to prepare for the next step.
    .. note::
        There are three methods to group nodals in the mesh.
            #. box.in/box.on/box.out x [x_min x_max] y [y_min y_max] or [x_min x_max y_min y_max]
            #. circle.in/circle.on/circle.out center [x y] radius rad or [x y radius]
            #. plane.on/plane.above/plane.below p0 [x0 y0] p1 [x1 y1] or [x0 y0 x1 y1]

    .. literalinclude:: ../../../src/examples/CreateBrazilianDiscTest/runme.of
        :lines: 74-75

#. Assign the nodal boundaries. For uniaxial test, top and bottom platens are moving toward the sample the compress the sample, so platens are not moving in the x direction and moving with 0.05 m/s in the y direction.
    .. literalinclude:: ../../../src/examples/CreateBrazilianDiscTest/runme.of
        :lines: 79-80

-------------------------------------------------------------------
3.5 Set the Outputs
-------------------------------------------------------------------
#. Set the output interval to be every 50000 steps and output all fields variables and fracture variables. Control the output interval to a reasonable size could shorten the computation time but get a good understanding of the model.
    .. literalinclude:: ../../../src/examples/CreateBrazilianDiscTest/runme.of
        :lines: 84, 86-87
#. The program will run 500000 steps in total. In other words, it will output 10 files for reference.
    .. literalinclude:: ../../../src/examples/CreateBrazilianDiscTest/runme.of
        :lines: 91
#. Finalize the model and clear all the temporary memories.
    .. literalinclude:: ../../../src/examples/CreateBrazilianDiscTest/runme.of
        :lines: 93
#. Save the notepad and double click the .of file to run the program.

==================================
4.0 Run the Program
==================================
When you run the program, you can first check the mesh that was created by Gmsh as shown in Figure 2. If the mesh has a good quality, you can close the window to continue run the program.

.. figure:: ../../images/Gmsh/BD_Test.png
    :alt: Mesh of the sample
    :align: center
    :scale: 60%

    Figure 2: Mesh created by Gmsh

|

==================================
5.0 Results
==================================
Wait for updates.



==================================
6.0 Full Script
==================================

- `BD_test.of`_ (click to download from GitHub gist)

.. _BD_test.of: https://github.com/OpenFDEM-geomechanics/Examples/blob/main/CreateBrazilianDiscTest/runme.of

    .. literalinclude:: ../../../src/examples/CreateBrazilianDiscTest/runme.of
        :lines: 37-93









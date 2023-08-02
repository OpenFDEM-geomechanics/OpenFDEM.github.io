Tutorial 10: Phase Field
########################################
Uniaxial compression test is one of the most fundamental tests that will be used to get the material properties 
from the experimental stress-strain curve.

.. figure:: ../../images/Desmos/Phase_Field.png
    :alt: Geometry of the phase field model
    :align: center
    :scale: 60%

    Figure 1: Geometry of the uniaxial compression strength test

|

==================================
1.0 Main Steps
==================================

#. Initialize the model.
#. Create the geometry and the mesh
#. Assign material properties.
#. Create the group and assign boundary conditions.
#. Set the outputs.

==================================
2.0 Codes
==================================
Please note that, all the setting in the example is based on the developer's computer. You may need to change 
these setting based on your own conditions.

To start with programming, create a new empty text file (later add the `.of` extension). Begin writing the following commands:

-------------------------------------------------------------------
2.1 Initialize the model
-------------------------------------------------------------------
#. Create a new run and clean up the old memories.
    .. literalinclude:: ../../../src/examples/PhaseFieldModelforModeIcrack/runme.of
        :lines: 39

#. Set up the folder name to save your results. Here the folder name is set to be “result”.
    .. literalinclude:: ../../../src/examples/PhaseFieldModelforModeIcrack/runme.of
        :lines: 43

#. Turn off the contact
    .. literalinclude:: ../../../src/examples/PhaseFieldModelforModeIcrack/runme.of
        :lines: 46

#. Set the minangle to delete the bad segments for joints and DFNs.
    .. literalinclude:: ../../../src/examples/PhaseFieldModelforModeIcrack/runme.of
        :lines: 49

#. Set the number of cores to be used for running this model.
    .. warning::
        In this example, 15 cores will be used for running. To prevent the crushing of your computer, please 
        check your computer to fill in the number of cores you want to use from your computer. To check the number 
        of cores your computer has, you can go Task Manager > Performance > CPU > Cores. If nothing is set here, 
        serial computing will be used.
    .. literalinclude:: ../../../src/examples/PhaseFieldModelforModeIcrack/runme.of
        :lines: 53

-------------------------------------------------------------------
2.2 Create the geometry and the mesh
-------------------------------------------------------------------
#. See Figur 1 to create a polygon with 9 points.
    .. literalinclude:: ../../../src/examples/PhaseFieldModelforModeIcrack/runme.of
        :lines: 56-65
#. Cut the joints in the plate.
    .. literalinclude:: ../../../src/examples/PhaseFieldModelforModeIcrack/runme.of
        :lines: 68
#. Group the geometries.
    .. literalinclude:: ../../../src/examples/PhaseFieldModelforModeIcrack/runme.of
        :lines: 70-71
#. Set different mesh size for different group of geometries.
    .. literalinclude:: ../../../src/examples/PhaseFieldModelforModeIcrack/runme.of
        :lines: 73-76
#. Create the mesh.
    .. literalinclude:: ../../../src/examples/PhaseFieldModelforModeIcrack/runme.of
        :lines: 78
#. Group the elements in a mesh.
    .. literalinclude:: ../../../src/examples/PhaseFieldModelforModeIcrack/runme.of
        :lines: 80

-------------------------------------------------------------------
2.3 Assign Material and Thermal Properties
-------------------------------------------------------------------
#. Set the material properties.
    .. literalinclude:: ../../../src/examples/PhaseFieldModelforModeIcrack/runme.of
        :lines: 84-85
#. Assign materials contacts.
    .. literalinclude:: ../../../src/examples/PhaseFieldModelforModeIcrack/runme.of
        :lines: 87

-------------------------------------------------------------------
2.4 Create Groups and Assign Boundary Conditions
-------------------------------------------------------------------
#. Group the nodes to prepare for the next step.
    .. literalinclude:: ../../../src/examples/PhaseFieldModelforModeIcrack/runme.of
        :lines: 90-91
#. Assign the pressure boundary conditions.
    .. literalinclude:: ../../../src/examples/PhaseFieldModelforModeIcrack/runme.of
        :lines: 98-99

-------------------------------------------------------------------
2.5 Set the Outputs
-------------------------------------------------------------------
#. Set the output interval to be every 2000 steps and output all fields variables and fracture variables. Control the output interval to a reasonable size could shorten the computation time but get a good understanding of the model.
    .. literalinclude:: ../../../src/examples/PhaseFieldModelforModeIcrack/runme.of
        :lines: 103-104
#. The program will run 100000 steps in total. In other words, it will output 10 files for reference.
    .. literalinclude:: ../../../src/examples/PhaseFieldModelforModeIcrack/runme.of
        :lines: 108
#. Finalize the model and clear all the temporary memories.
    .. literalinclude:: ../../../src/examples/PhaseFieldModelforModeIcrack/runme.of
        :lines: 110
#. Save the notepad and double click the .of file to run the program.

==================================
3.0 Run the Program
==================================
When you run the program, you can first check the mesh that was created by Gmsh as shown in Figure 2. If the mesh has a good quality, you can close the window to continue run the program.

.. figure:: ../../images/Gmsh/Phase_Field.png
    :alt: Mesh of the sample
    :align: center
    :scale: 60%

    Figure 2: Mesh created by Gmsh

|

The phase field module is ON in this model.

.. figure:: ../../images/Command/Phase_Field_module.png
    :alt: Phase field module is ON
    :align: center
    :scale: 80%

    Figure 3: Global modules

|

Material properties you set on step 2.3 will be shown on the screen. You can confirm it while the program just starts to run.

.. figure:: ../../images/Command/Phase_Field_Material.png
    :alt: Material assignment
    :align: center
    :scale: 55%

    Figure 4: Check the material assignment from command window

|


==================================
4.0 Results
==================================
Wait for updates.



==================================
5.0 Full Script
==================================

- `Phase_Field.of`_ (click to download from GitHub)

.. _Phase_Field.of: https://github.com/OpenFDEM-geomechanics/Examples/blob/main/PhaseFieldModelforModeIcrack/runme.of

    .. literalinclude:: ../../../src/examples/PhaseFieldModelforModeIcrack/runme.of
        :lines: 37-110









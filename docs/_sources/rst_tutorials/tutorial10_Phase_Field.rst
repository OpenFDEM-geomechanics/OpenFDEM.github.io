Phase Field
########################################


.. figure:: ../../images/Desmos/Phase_Field.png
    :alt: Geometry of the phase field model
    :align: center
    :scale: 60%

    Figure 1: Geometry of the uniaxial compression strength test


==================================
1 Main Steps
==================================

#. Initialize the model.
#. Create the geometry and the mesh
#. Assign material properties.
#. Create the group and assign boundary conditions.
#. Set the outputs.

==================================
2 Codes
==================================
Please note that, all the setting in the example is based on the developer's computer. You may need to change 
these setting based on your own conditions.

To start with programming, create a new empty text file (later add the `.of` extension). Begin writing the following commands:

-------------------------------------------------------------------
2.1 Initialize the model
-------------------------------------------------------------------
1. Create a new run and clean up the old memories.

.. literalinclude:: examples/PhaseFieldModelforModeIcrack/runme.of
    :lines: 39

2. Set up the folder name to save your results. Here the folder name is set to be “result”.

.. literalinclude:: examples/PhaseFieldModelforModeIcrack/runme.of
    :lines: 43

3. Turn off the contact module, no contacts will be considered in this simulation.

.. literalinclude:: examples/PhaseFieldModelforModeIcrack/runme.of
    :lines: 46

4. Set the minangle to delete the bad segments for joints and DFNs.

.. literalinclude:: examples/PhaseFieldModelforModeIcrack/runme.of
    :lines: 49

5. Set the number of cores to be used for running this model.

.. literalinclude:: examples/PhaseFieldModelforModeIcrack/runme.of
    :lines: 54

-------------------------------------------------------------------
2.2 Create the geometry and the mesh
-------------------------------------------------------------------
1. See Figur 1 to create a polygon with 9 points.

.. literalinclude:: examples/PhaseFieldModelforModeIcrack/runme.of
    :lines: 57-66

2. Cut the joints in the plate.

.. literalinclude:: examples/PhaseFieldModelforModeIcrack/runme.of
    :lines: 69

3. Group the geometries.

.. literalinclude:: examples/PhaseFieldModelforModeIcrack/runme.of
    :lines: 71-72

4. Set different mesh size for different group of geometries.

.. literalinclude:: examples/PhaseFieldModelforModeIcrack/runme.of
    :lines: 74-77

5. Create the mesh.

.. literalinclude:: examples/PhaseFieldModelforModeIcrack/runme.of
    :lines: 79

6. Group the elements in a mesh.

.. literalinclude:: examples/PhaseFieldModelforModeIcrack/runme.of
    :lines: 81

-------------------------------------------------------------------
2.3 Assign Material and Thermal Properties
-------------------------------------------------------------------
1. Set the material properties.

.. literalinclude:: examples/PhaseFieldModelforModeIcrack/runme.of
    :lines: 85-86

2. Assign materials contacts.

.. literalinclude:: examples/PhaseFieldModelforModeIcrack/runme.of
    :lines: 88

-------------------------------------------------------------------
2.4 Create Groups and Assign Boundary Conditions
-------------------------------------------------------------------
1. Group the nodes to prepare for the next step.

.. literalinclude:: examples/PhaseFieldModelforModeIcrack/runme.of
    :lines: 91-92

2. Assign the pressure boundary conditions.

.. literalinclude:: examples/PhaseFieldModelforModeIcrack/runme.of
    :lines: 99-100

-------------------------------------------------------------------
2.5 Set the Outputs
-------------------------------------------------------------------
1. Set the output interval to be every 2000 steps and output all fields variables and fracture variables. Control the output interval to a reasonable size could shorten the computation time but get a good understanding of the model.

.. literalinclude:: examples/PhaseFieldModelforModeIcrack/runme.of
    :lines: 104-105

2. The program will run 100000 steps in total. In other words, it will output 10 files for reference.

.. literalinclude:: examples/PhaseFieldModelforModeIcrack/runme.of
    :lines: 109

3. Finalize the model and clear all the temporary memories.

.. literalinclude:: examples/PhaseFieldModelforModeIcrack/runme.of
    :lines: 111

4. Save the notepad and double click the .of file to run the program.

==================================
3 Run the Program
==================================
When you run the program, you can first check the mesh that was created by Gmsh as shown in Figure 2. If the mesh has a good quality, you can close the window to continue run the program.

.. figure:: ../../images/Gmsh/Phase_Field.png
    :alt: Mesh of the sample
    :align: center

    Figure 2: Mesh created by Gmsh


The phase field module is ON in this model.

.. figure:: ../../images/Command/Phase_Field_module.png
    :alt: Phase field module is ON
    :align: center

    Figure 3: Global modules


Material properties you set on step 2.3 will be shown on the screen. You can confirm it while the program just starts to run.

.. figure:: ../../images/Command/Phase_Field_Material.png
    :alt: Material assignment
    :align: center

    Figure 4: Check the material assignment from command window



==================================
4 Results
==================================
Wait for updates.



==================================
5 Full Script
==================================

- `Phase_Field.of`_ (click to download from GitHub)

.. _Phase_Field.of: https://github.com/OpenFDEM-geomechanics/Examples/blob/main/PhaseFieldModelforModeIcrack/runme.of

.. literalinclude:: examples/PhaseFieldModelforModeIcrack/runme.of
    :lines: 37-111



.. raw:: html

   <script src="//clustrmaps.com/globe.js?d=IJDdJTOZeBy5TaHUiVkIm7GLGSulnk0C2NzaC4-34QA">
   </script>



Tunnel excavation under `in-situ` stress
########################################
In-situ stress is an important issue that significantly influence the damage distribution and surrounding rock stability in underground excavation.
In this example, we will show how to create the excavation model, how to get stress equlibrium before excavation and how to use step-by-step excavation in OpenFDEM.

.. figure:: ../../images/Desmos/Apply_Insitu_Stress.png
    :alt: Geometry of the Rock and Excavation
    :align: center

    Figure 1: Geometry of the Rock and Excavation

==================================
1 Main Steps
==================================

#. Initialize the model
#. Import mesh
#. Create groups
#. Assign material properties
#. Assign boundaries
#. Setup output
#. Run model

==================================
2 Codes
==================================
.. warning::

    Please note that, all the setting in the example is based on the developer's computer. You may need to change 
    these details based on your own environment.

To start with programming, create a new empty input file or copy it from the existing examples (later add the ``.of`` extension). Begin writing the following commands:

-------------------------------------------------------------------
2.1 Initialize the model
-------------------------------------------------------------------
1 Create a new run and clean up the old memories.

.. literalinclude:: examples/ApplyInsituStress/runme.of
    :lines: 39

2. Set up the folder name to save your results. Here the folder name is set to be “result”.

.. literalinclude:: examples/ApplyInsituStress/runme.of
    :lines: 43

3. Set the number of cores to be used for running this model in parallelization.

.. literalinclude:: examples/ApplyInsituStress/runme.of
    :lines: 48

-------------------------------------------------------------------
2.2 Create the geometry and the mesh
-------------------------------------------------------------------
1. See Figure 1, we will create a square rock model with a 0.05 m radius hole at the center of the rock.  

.. seealso::
    Circles in OpenFDEM are defined by four parameters: x coordinate, y coordinate, radius and the number of segments. Users can define a circle by entering **[x_value y_value radius #_of_segements]**.         

.. literalinclude:: examples/ApplyInsituStress/runme.of
    :lines: 52-53

2. Set the mesh size and the `default` method to create the mesh

.. literalinclude:: examples/ApplyInsituStress/runme.of
    :lines: 55-56

3. Group the elements which will be excavated.

.. literalinclude:: examples/ApplyInsituStress/runme.of
    :lines: 58

-------------------------------------------------------------------
2.3 Assign Material Properties
-------------------------------------------------------------------
The material properties of this model is shown as the table below:

+---------------------------------------------+------------------------+
| Parameter                                   | Value                  |
+=============================================+========================+
| **Continuum Triangular Elements**           |                        |
+---------------------------------------------+------------------------+
| model                                       | elastic                |
+---------------------------------------------+------------------------+
| density (:math:`kg/m^3`)                    | 2700                   |
+---------------------------------------------+------------------------+
| E (Pa)                                      | 30e9                   |
+---------------------------------------------+------------------------+
| :math:`\nu`                                 | 0.3                    |
+---------------------------------------------+------------------------+
| damp                                        | 1.0                    |
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
    Check :doc:`element materal<../rst_user_guide/Material/of.mat.element>`, and :doc:`contact materal<../rst_user_guide/Material/of.mat.contact>` to see more materials.

Set the material properties as shown below.

.. literalinclude:: examples/ApplyInsituStress/runme.of
    :lines: 62,64

-------------------------------------------------------------------
2.4 Group the Edges
-------------------------------------------------------------------
Group the four boundaries of the model for applying the `in-situ` stress and boundary conditions.

.. literalinclude:: examples/ApplyInsituStress/runme.of
    :lines: 69-72

-------------------------------------------------------------------
2.5 Assign Boundary Conditions
-------------------------------------------------------------------
1. For this example, 30 MPa compressive stress in the `xx` direction and 5 MPa compressive stresses in the `yy` direction are assigned to the rock.

.. literalinclude:: examples/ApplyInsituStress/runme.of
    :lines: 76

2. To quickly balance the model, absorbing boundary conditions are assigned to four boundaries in the model.

.. literalinclude:: examples/ApplyInsituStress/runme.of
    :lines: 79-82

-------------------------------------------------------------------
2.6 Set the Outputs
-------------------------------------------------------------------
1. Set the output interval to be every 2000 steps and output all fields variables and fracture variables. 

.. literalinclude:: examples/ApplyInsituStress/runme.of
    :lines: 86, 88-89
2. In this step, model will first achieve the equilibrium without excavation under `in-situ` stresses state. The result of velocity or kinematic ratio should be less than 0.00001.

.. literalinclude:: examples/ApplyInsituStress/runme.of
    :lines: 96
3. Insert CZM after achieve the equlibrium of in-situ stresses

+---------------------------------------------+------------------------+
| Parameter                                   | Value                  |
+=============================================+========================+
| **Cohesive Material Properties**            |                        |
+---------------------------------------------+------------------------+
| model                                       | EM                     |
+---------------------------------------------+------------------------+
| tension (Pa)                                | 1e6                    |
+---------------------------------------------+------------------------+
| cohesion (Pa)                               | 20e6                   |
+---------------------------------------------+------------------------+
| friction                                    | 0.8                    |
+---------------------------------------------+------------------------+
| GI (:math:`J/m^2`)                          | 2                      |
+---------------------------------------------+------------------------+
| GII (:math:`J/m^2`)                         | 40                     |
+---------------------------------------------+------------------------+
.. literalinclude:: examples/ApplyInsituStress/runme.of
    :lines: 99-100
4. One step excavation method. Remove the elements in the "excavation" group.

.. literalinclude:: examples/ApplyInsituStress/runme.of
    :lines: 101
5. Clear the absorbing boundaries

.. literalinclude:: examples/ApplyInsituStress/runme.of
    :lines: 104-107

6. Add pressures at the external boundaries

.. literalinclude:: examples/ApplyInsituStress/runme.of
    :lines: 110-113
7. The program will run 500000 steps in total. In other words, it will output 25 files for reference.

.. literalinclude:: examples/ApplyInsituStress/runme.of
    :lines: 116

8. Finalize the model and clear all the temporary memories.

.. literalinclude:: examples/ApplyInsituStress/runme.of
    :lines: 119

9. Save the notepad and double click the .of file to run the program.

==================================
3 Run the Program
==================================
When you run the program, you can first check the mesh that was created by Gmsh as shown in Figure 2. If the mesh has a good quality, you can close the window to continue run the program.

.. figure:: ../../images/Gmsh/In_situ_stress.png
    :alt: Mesh of the sample
    :align: center

    Figure 2: Mesh created by Gmsh


Check the boundary conditions here. Absorbing boundary conditions are on for both normal and shear directions. In-situ stresses are applied to the boundaries.

.. figure:: ../../images/Command/Insitu_BC.png
    :alt: Triangle elements
    :align: center

    Figure 3: Check the mesh setting from command window



==================================
4 Results
==================================

To hide hole of excavation, threshold filter can be used.

Stress XX results.

.. figure:: ../../images/Result/Insitu_StressXX.gif
    :alt: In-situ Stress XX
    :align: center

    Figure 4: In-situ Stress XX

Stress YY results.

.. figure:: ../../images/Result/Insitu_StressYY.gif
    :alt: In-situ Stress YY
    :align: center

    Figure 5: In-situ Stress XX


==================================
5 Full Script
==================================

- `Apply_Insitu_Stress.of`_ (click to download from Gitlab)

.. _Apply_Insitu_Stress.of: https://github.com/OpenFDEM-geomechanics/Examples/blob/main/ApplyInsituStress/runme.of

.. literalinclude:: examples/ApplyInsituStress/runme.of
    :lines: 37-119

.. raw:: html

   <script src="//clustrmaps.com/globe.js?d=IJDdJTOZeBy5TaHUiVkIm7GLGSulnk0C2NzaC4-34QA">
   </script>









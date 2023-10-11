Water flowing in rock dam: fracture flow
########################################
This tutorial will continue the hydro seepage model in tutorial 6 with discrete elements. The hydro flowing is considered only on the cohesive interfaces.

.. figure:: ../../images/Desmos/Hydro.png
    :alt: Geometry of the uniaxial compression test
    :align: center

    Figure 1: Geometry of the uniaxial compression strength test


==================================
1 Code
==================================
Based on the code in tutorial 6, fracture flow parameters will be add to model the hydro fracture.

1. To include the discrete elements, joint elements are added to the model after create the mesh.

.. literalinclude:: examples/HydroFractureFlow/runme.of
    :lines: 20

2. Assign the material properties to CZM.

+---------------------------------------------+------------------------+
| Parameter                                   | Value                  |
+=============================================+========================+
| **Contact Material Properties**             |                        |
+---------------------------------------------+------------------------+
| model                                       | MC                     |
+---------------------------------------------+------------------------+
| friction                                    | 0.5                    |
+---------------------------------------------+------------------------+

.. literalinclude:: examples/HydroFractureFlow/runme.of
    :lines: 61

3. Set fracture flow parameters

+---------------------------------------------+------------------------+
| Parameter                                   | Value                  |
+=============================================+========================+
| **Hydro fluid material**                    |                        |
+---------------------------------------------+------------------------+
| density (:math:`kg/m^3`)                    | 1000.0                 |
+---------------------------------------------+------------------------+
| K (Pa)                                      | 20e9                   |
+---------------------------------------------+------------------------+
| viscosity (Pa)                              | 1e-3                   |
+---------------------------------------------+------------------------+
|                                             |                        |
+---------------------------------------------+------------------------+
| **Hydro Fracture material**                 |                        |
+---------------------------------------------+------------------------+
| a0 (m)                                      | 1e-4                   |
+---------------------------------------------+------------------------+
| amin (m)                                    | 1e-4                   |
+---------------------------------------------+------------------------+
| amax (m)                                    | 3e-4                   |
+---------------------------------------------+------------------------+
| power                                       | 3.0                    |
+---------------------------------------------+------------------------+
| b                                           | 1.0                    |
+---------------------------------------------+------------------------+
.. literalinclude:: examples/HydroFractureFlow/runme.of
    :lines: 64-65

==================================
2 Run the Program
==================================
1. Hydro module, Fracture flow module and CZM module are on to model the hydro fracture flow.

.. figure:: ../../images/Command/Hydro_Fracture_Modulus.PNG
    :alt: Applied Modules
    :align: center

    Figure 2: Applied Modules

2. Contact material, hydro fracture material and hydro fluid material are include in the modeling.

.. figure:: ../../images/Command/Hydro_Fracture_Material.PNG
    :alt: Hydro Fracture Materials
    :align: center

    Figure 3: Hydro Fracture Materials

3. Hydro boundary conditions.

.. figure:: ../../images/Command/Hydro_BC.PNG
    :alt: Hydro Boundary Conditions
    :align: center

    Figure 4: Hydro Boundary Conditions

==================================
3 Results
==================================
Fluid pressure of fracture flow.

.. figure:: ../../images/Result/Fracture_Viridis.gif
    :alt: Hydro Fracture Flow
    :align: center

    Figure 5: Hydro Fracture Flow



==================================
4 Full Script
==================================

- `Hydro_Fracture_Flow.of`_ (click to download from GitHub)

.. _Hydro_Fracture_Flow.of: https://github.com/OpenFDEM-geomechanics/Examples/blob/main/HydroFractureFlow/runme.of

.. literalinclude:: examples/HydroFractureFlow/runme.of
    :lines: 37-97
    :emphasize-lines: 20, 25, 28-29



.. raw:: html

   <script src="//clustrmaps.com/globe.js?d=IJDdJTOZeBy5TaHUiVkIm7GLGSulnk0C2NzaC4-34QA">
   </script>





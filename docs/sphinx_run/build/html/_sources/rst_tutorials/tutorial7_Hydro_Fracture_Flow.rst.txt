Tutorial 7: Hydro Fracture Flow
########################################
This tutorial will continue the hydro seepage model in tutorial 6 with discrete elements.

.. figure:: ../../images/Desmos/Hydro.png
    :alt: Geometry of the uniaxial compression test
    :align: center
    :scale: 40%

    Figure 1: Geometry of the uniaxial compression strength test

|

==================================
1.0 Code
==================================
Based on the code in tutorial 6, fracture flow parameters will be add to model the hydro fracture.

#. To include the discrete elements, joint elements are added to the model after create the mesh.
    .. literalinclude:: ../../../src/examples/HydroFractureFlow/runme.of
        :lines: 55
#. Assign the material properties to CZM.
    +---------------------------------------------+------------------------+
    | Parameter                                   | Value                  |
    +=============================================+========================+
    | **Contact Material Properties**             |                        |
    +---------------------------------------------+------------------------+
    | model                                       | MC                     |
    +---------------------------------------------+------------------------+
    | friction                                    | 0.5                    |
    +---------------------------------------------+------------------------+

    .. literalinclude:: ../../../src/examples/HydroFractureFlow/runme.of
        :lines: 60
#. Set fracture flow parameters
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
    .. literalinclude:: ../../../src/examples/HydroFractureFlow/runme.of
        :lines: 63-64

==================================
2.0 Run the Program
==================================
Hydro module, Fracture flow module and CZM module are on to model the hydro fracture flow.

.. figure:: ../../images/Command/Hydro_Fracture_Modulus.PNG
    :alt: Applied Modules
    :align: center
    :scale: 80%

    Figure 2: Applied Modules

|
Contact material, hydro fracture material and hydro fluid material are include in the modeling.

.. figure:: ../../images/Command/Hydro_Fracture_Material.PNG
    :alt: Hydro Fracture Materials
    :align: center
    :scale: 60%

    Figure 3: Hydro Fracture Materials

|
Hydro boundary conditions.

.. figure:: ../../images/Command/Hydro_BC.PNG
    :alt: Hydro Boundary Conditions
    :align: center
    :scale: 65%

    Figure 4: Hydro Boundary Conditions

|

==================================
3.0 Results
==================================
Wait for updates.



==================================
4.0 Full Script
==================================

- `Hydro_Fracture_Flow.of`_ (click to download from GitHub)

.. _Hydro_Fracture_Flow.of: https://github.com/OpenFDEM-geomechanics/Examples/blob/main/HydroFractureFlow/runme.of

    .. literalinclude:: ../../../src/examples/HydroFractureFlow/runme.of
        :lines: 37-96
        :emphasize-lines: 19, 24, 27-28









About: What Can OpenFDEM Do
==============================

**OpenFDEM** (an Open Hybrid Finite-Discrete Element solver) is a scientific software for the numerical solution of partial differential equations, also open to other coupling of physical problems such as thermal, hydro, fluid dynamics, rigid collision, etc. It can deal with such problems of (1D, 2D and 3D) and time problems (static and/or transient).

Object Oriented Architecture (C++ and CUDA®)
---------------------------------------------
The main feature of **OpenFDEM** is the use of modern C++ object-oriented programming, and the organization of data structure defining from the explicit input keywords. It consists of a working environment in which any problem is defined using a limited number of objects, which makes
•	it approachable and easy to use at both the development and application levels as the initial intention. 
•	the environment structured and concise. 
Thus, it provides researchers with advanced development tools and great freedom to add new features.

Modular & Extensible FEM Kernel and DEM Kernel (OpenFDEMlib)
-------------------------------------------------------------

•	**Fully extendable and portable** - The kernel can be extended in any "direction". Adding new element types, new material models with any number of element types and internal history parameters, new boundary conditions (time-dependent, position-dependent, state-dependent, periodic and flow-in/out) or numerical algorithms (explicit and implicit) is possible, as well as the ability to add and manage arbitrary degrees of freedom is a matter of course. (It is not a Y-like code limited to constant-strain triangular elements, Q4 cohesive elements and triangle-triangle contacts; OpenFDEM is intended to be a more general FEM/DEM solver compatible with arbitrary scenarios.) Like other common open-source FEM solvers, the most important feature of OpenFDEM is its standardization and generality, which allows the continuum-discontinuum method to be used with more general scenarios.

.. figure:: ../../images/elementtype.gif
  :alt: Element Types Gif

  OpenFDEM supports 26 element types and 24 materials.

•	**Highly accurate and reliable** - The kernel provides high-order integration schemes and solving methods to seek more reliable numerical results which are comparable to theoretical solutions. The element type has a maximum order of three to produce the large deformation behavior in the entity, and the new kinematic scheme to construct a nonlinear deformation. The Hilber-Hughes-Taylor (HHT) time integration scheme (second-order accuracy) is employed for the explicit solver. The Y-like codes are limited to the first order time integration and constant strain element.

.. figure:: ../../images/elementshape.png
  :alt: Element Shape

  Quadratic elements are supported in OpenFDEM. Combined linear element (quadrilateral and triangle elements, left), quadratic quadrilateral element (middle) and refined linear quadrilateral element (right).

•	**Friendly preprocessing interface** - The Gmsh is provided to easily create meshes from computer-aided design (CAD), geometry file and third-party commercial software. The built-in commands are accessible to create many basic geometries (e.g. rectangular, circle, ellipse, polygon, line and particles) and initial discontinuities (e.g. single joint, joint sets, DFNs and DFNs from image mapping). This built-in mesh module can quickly assess mesh quality and identify the local bad meshes which will be further optimized by swap, node insertion, node delete, element split techniques, automatically or manually. Meanwhile, for very complex geometric models, users can also import mesh files from third-party software. OpenFDEM supports importing standard mesh files, such as .msh, .inp, .stl, .dxf and .step, etc. Principally, the geometry file can be processed by Gmsh can also be done by OpenFDEM.

# TODO:: DFN picture (page 8)

•	**Parallel processing support** - Most modules can be operated in parallel and very good performance scalability on various platforms. Instead of using no binary searching (NBS) contact method in OpenFDEM, a new element-wise contact searching algorithm with a complexity of O(NlogN) is proposed to make the contact searching process parallelable. The GPU acceleration will also be added shortly.
•	**Mesh adaptive analysis support** - Local adaptive mesh refinement (lAMR) and global adaptive mesh refinement(gAMR) are provided in OpenFDEM for mesh optimization and accuracy enhancement. Based on different remeshing criteria, OpenFDEM supports various error estimations, such as primary unknown, internal variables mapping, high-accuracy internal variable interpolation and fast unbalance equilibrium after refinement. The AMR supports fracture path consistent before and after remeshing.

.. figure:: ../../images/AMR.gif
  :alt: AMR Gif

  Global adaptive mesh refinement (up-left) and local adaptive mesh refinement (down-right) in OpenFDEM.

.. figure:: ../../images/wavebetter.gif
  :alt: Flowing mesh refined stress

  Flowing mesh refined based on the stress level in the bar.

•	**Rich grain-based modelling support** - Voronoi tessellations can be created with the built-in Voronoi module. The optimization is deployed to match the laboratorial mineral distribution from measurements or digital image. The realistic grain-based model (GBM) can be reproduced directly in the project by inputting the binary sample images. The polygonal element type is available for representing the whole mineral individually. Furthermore, transgranular fracturing can be realized by element splitting techniques.

# TODO:: Grain scale fracture imaging

.. figure:: ../../images/voronoi.gif
  :alt: Voronoi

  OpenFDEM implements a Voronoi lib and is able to simulate grains directly based on polygonal elements.

•	**Large material library including the state-of-the-art models for phase field of quasi-brittle materials and rich element library** - currently, OpenFDEM supports 17 element materials (spanning elastic, hyperelastic, plastic, damage, nonlocal, viscous and phas—field models), 7 cohesive materials (spanning static, dynamic and fatigue problems), and 6 contact models (including Mohr-coulomb friction, hertz contact, rate friction, rough dilation shear law and so on). (The OpenFDEM is the only code supports materials beyond the community of rock mechanics)

.. figure:: ../../images/feature.png
  :alt: New material library

  New material library in OpenFDEM.

.. figure:: ../../images/globalAMRPhase.gif
  :alt: Phase field library

  Phasefield module in OpenFDEM.

•	**Advanced analysis solvers** - Linear dynamic solver (implicit and explicit), linear static solver (PETSC), eigenvalue problem (SLEPc), and nonlinear dynamic solver (explicit) are applicable for different problems (The OpenFDEM is the only project provides implicit solver for FDEM-like codes), the implicit solver currently can be run on Linux-like OS.

Particle Discrete Element Method (pDEM)
-----------------------------------------

•	**Rigid DEM support** - built-in module for rigid particles packing, kinematics and collision, the particle-based contact models include linear, Hertz, cohesive bond and rotation resistance model.

.. figure:: ../../images/PDEM.png
  :alt: Sand compression test with membrane (left) and irregular deformable and breakable particles packing (right).

  Sand compression test with membrane (left) and irregular deformable and breakable particles packing (right).

•	**Realistic Particle Modelling** - Overlapping particles and Fourier-Voronoi-based algorithm are used to generate realistic particles having complex shapes. The realistic particles can be rigid or deformable. The breakage of the particles are also possible.

.. figure:: ../../images/landslide.gif
  :alt: landslide gif 
  
  Debris flow of rigid particles due to gravity (left) and debris flow of irregular deformable fragments due to gravity (right, .stl file from Itasca).


Fluid Dynamic Module
---------------------

•	**Analysis Procedures** - matrix flow for pore seepage, transient incompressible fracture flow, transient compressible fracture flow and gas flow problems.

.. figure:: ../../images/gasblast.gif
  :alt: landslide gif 
  
  Blast considering gas expansion, gas flow by hydro module (left) and without gas expansion by mechanical module (right) ((Wang et al. 2021, 2022)).

•	**Element Library** - triangle, quadratic triangle, quadrilateral and quadratic quadrilateral element types are supported for Newtonian fluid and Bingham fluid.

.. figure:: ../../images/Hydraulic.gif
  :alt: Fluid injection in fractured rock block.  
  
  Fluid injection in fractured rock block.

.. figure:: ../../images/tube.gif
  :alt: Water flowing in a tube using CFD in hydro module. 
  
  Water flowing in a tube using CFD in hydro module.

•	**Boundary Types** - water level, pore pressure, flow rate, steady flow and impermeable boundary conditions are supported in hydro module.

Thermal Transportation Module
------------------------------

•	**Analysis Procedures** - matrix thermal transportation, thermal resistance in fractures, heat conduction of fluid in fracture, heat advection of fluid, heat exchange between solid and fluid and contact thermal problems.

.. figure:: ../../images/microwavethermal.gif
  :alt: Gabbro fracturing after microwave treatment in thermal module.
  
  Gabbro fracturing after microwave treatment in thermal module.

•	**Element Library** - triangle, quadratic triangle, quadrilateral and quadratic quadrilateral element types are supported.
•	**Boundary Types** - constant temperature, flux, conduction, advection, radiation, source and adiabatic thermal conditions are supported.

Computational Fluid Dynamics
------------------------------

•	**Material Point Method (MPM)** - is used to simulate the fluid transportation and large deformation. This mesh-free method does not encounter the drawbacks of mesh-based methods (high deformation tangling, advection errors etc.) which makes it a promising and powerful tool for large deformation problems. The coupling between FDEM and MPM makes the solid interacting with fluid possible.

.. figure:: ../../images/tapwater.gif
  :alt: Tap water flow into a tank, MPM + FDEM.
  
  Tap water flow into a tank, MPM + FDEM.

.. figure:: ../../images/vortex.gif
  :alt: Kármán vortex street example, periodic boundary.
  
  Kármán vortex street example, periodic boundary.

**Post-Processing**

•	Export to VTK format is supported, allowing to use VTK based visualization tools (such as ParaView) for postprocessing on different operating platforms.
•	Export to Tecplot format is supported.
•	Export historic variables which are monitored at each step to ``.csv`` is supported.

**Third-Party Packages Used in OpenFDEM**

•	``GMSH`` - 2D and 3D mesh generator
•	``GSL`` - mathematical routines
•	``Eigen`` - matrix calculation
•	``PETSC`` - Portable, Extensible Toolkit for Scientific Computation
•	``ParaView`` - Parallel Visualization Application (for ``.vtk`` files)


Documentation
------------------

The documentation is auto-generated from the ``.of`` and ``.rst`` files throughout
the codebase and the extensive comments in the source code ``.h`` and ``.of`` files. Sphinx is used to compile
the documentation in HTML and PDF formats.
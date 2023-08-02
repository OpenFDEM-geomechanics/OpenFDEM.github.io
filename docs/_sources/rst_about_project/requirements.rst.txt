System Requirements
===================

Build Requirements
---------------------
To compile ``OpenFDEM``, you neeed a complier supporting ``C++ 17`` and the following packages are required:

- **CMake** (>=3.5.1)
- **OpenMP** - a high-performance, freely available package for multi core acceleration
- **Gmsh** -  mesh generation and pre-processing, it is optional and the kernel is implemented in the source code (4.10)
- **Eigen** - a scientific matrix computation, it is optional and the headers are included in source code (>=3.4.0)

Post-Processing
----------------

To use the post-processing outputs (optional steps):

- **ParaView** - Parallel visualization application
- **Tecplot** - Commerical software for field results

Implicit Static/Non-Linear Solvers
--------------------------------------

To use the implicit static or nonlinear solvers, at least one of the following libraries is required:

- **PETSc** - portable, extensible toolkit for scientific computation
- **LAPACK** - a standard software library for numerical linear algebra


``OpenFDEM`` is flexible and can be run on Windows or Linux-like systems. The released version is for Windows x64.

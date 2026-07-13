Installation
==================================

Mandatory Packages
---------------------
To compile ``OpenFDEM``, you neeed a complier supporting ``C++ 17`` and the following packages are required:

- ``CMake`` (>= version 3.15) - cross-platform build system
- C, C++ compiler with Standard Template Library (STL) support, ``C++ 20`` is mandatory
- ``OpenMP`` - a high-performance, freely available package for multi core acceleration
- ``GSL`` - a general software library for numerical computations in applied mathematics and science
- ``Gmsh`` (>= version 4.10) -  mesh generation and pre-processing, it is optional and the kernel is implemented in the source code
- ``Eigen`` (>= version 3.4.0) - a scientific matrix computation, it is optional and the headers are included in source code

Optional Packages
---------------------
- ``CUDA`` - package for GPU parallelization
- ``PETSc`` (>= version 3.13) - portable, extensible toolkit for scientific computation
- ``SLEPc`` - scalable library for eigenvalue problem computations
- ``BLAS/LAPACK`` - optimizes linear algebra kernels
- ``doxygen`` - documentation system for automatic generating reference manual from the source code
- ``Sphinx`` - documentation generator or a tool that translates a set of plain text source files into various output formats, automatically producing cross-references, indices, etc.

Implicit Static/Non-Linear Solvers
--------------------------------------

To use the implicit static or nonlinear solvers, at least one of the following libraries is required:

- ``PETSc`` - portable, extensible toolkit for scientific computation (if ``PETSC`` installed, ``LAPACK`` and ``BLAS`` can be ignored)
- ``BLAS/LAPACK`` - a standard software library for numerical linear algebra

For Python interface
-------------------------
- ``Python`` - (>=3.8 is recommended)
- ``pybind11`` - a package create Python bindings of existing C++ code 

Post-Processing
----------------

To use the post-processing outputs (optional steps):

- ``ParaView`` - Parallel visualization application
- ``Tecplot`` - Commerical software for field results




``OpenFDEM`` is flexible and can be run on Windows or Linux-like systems. The released version is for Windows x64.

.. raw:: html

   <script src="//clustrmaps.com/globe.js?d=IJDdJTOZeBy5TaHUiVkIm7GLGSulnk0C2NzaC4-34QA">
   </script>

How to Install
===========================

There are two ways to use OpenFDEM: **user access** from the pre-compiled
installation package, or **developer access** by compiling the source code
yourself.


********************************
Installing the Compiled Software
********************************

For most users, the easiest way to get started is to download the pre-compiled
software. The compiled package is **self-contained and requires no additional
dependencies** — simply download the installer and follow the on-screen
instructions of the setup wizard step by step to complete the installation.

The released version is for **Windows x64**.

The installation package can be obtained from the :doc:`Downloads
<../rst_downloads>` page.


************************
Building from Source
************************

Advanced users and developers may compile OpenFDEM from the source code. The
source code is available from the `OpenFDEM GitHub repository
<https://github.com/OpenFDEM-geomechanics/OpenFDEM>`_. In the first stage, the
source code is only open to collaborating partners before some benchmark papers
are published. A trial of the source code is accessible on request; contact the
developer `Dr. Xiaofeng Li <xfli@whrsm.ac.cn>`_ to get an invitation to this
repository.

.. note::

   If you plan on collaborating or using OpenFDEM as your base code, it is
   highly recommended that you fork this repository to your own account and
   work on it there.

   **NEVER** push your local code to the master branch. The master branch of
   OpenFDEM is the stable branch that will only be updated after all tests are
   passing.

.. warning::

   Only pull requests from your own fork to the main repository will be
   considered, and they will only be considered if there are **NO CONFLICTS**.
   Push requests which cause **CONFLICTS** will be rejected out of hand.


Dependencies
------------------------

To compile OpenFDEM, you need a compiler supporting ``C++ 17`` (``C++ 20`` is
mandatory) and the following packages.

**Mandatory packages**

- ``CMake`` (>= version 3.15) - cross-platform build system
- C, C++ compiler with Standard Template Library (STL) support
- ``OpenMP`` - a high-performance, freely available package for multi-core acceleration
- ``GSL`` - a general software library for numerical computations in applied mathematics and science
- ``Gmsh`` (>= version 4.10) - mesh generation and pre-processing (optional; the kernel is implemented in the source code)
- ``Eigen`` (>= version 3.4.0) - scientific matrix computation (optional; the headers are included in the source code)

**Optional packages**

- ``CUDA`` - package for GPU parallelization
- ``PETSc`` (>= version 3.13) - portable, extensible toolkit for scientific computation
- ``SLEPc`` - scalable library for eigenvalue problem computations
- ``BLAS/LAPACK`` - optimizes linear algebra kernels
- ``doxygen`` - documentation system for automatically generating the reference manual from the source code
- ``Sphinx`` - documentation generator that translates plain-text source files into various output formats

**Implicit static / non-linear solvers** — to use these solvers, at least one
of the following is required:

- ``PETSc`` (if ``PETSc`` is installed, ``LAPACK`` and ``BLAS`` can be ignored)
- ``BLAS/LAPACK`` - a standard software library for numerical linear algebra

**For the Python interface**

- ``Python`` (>= 3.8 is recommended)
- ``pybind11`` - a package to create Python bindings of existing C++ code

**For post-processing** (optional)

- ``ParaView`` - parallel visualization application
- ``Tecplot`` - commercial software for field results


Microsoft Windows
------------------------

**Software requirements**

For Windows 10, the user must have the following applications installed: CMake,
Visual Studio (>= Visual Studio 2019, SDK should support C++ 20). The Microsoft
Visual C++ 2008 Redistributable Package is required for Windows 7 and 10.

.. note::

    Installing PETSc on Windows can be troublesome. You can uncheck ``Static
    Solver`` in CMakeList or use ``BLAS/LAPACK`` instead. If you insist on
    trying the nonlinear static solver and compiling PETSc on Windows, more
    information can be found in the `PETSc documentation
    <https://petsc.org/release/install/windows/>`_, using

    - `MSYS2 <https://www.msys2.org>`__ or
    - Microsoft Windows Subsystem for Linux 2 (`WSL2 <https://docs.microsoft.com/en-us/windows/wsl/install-win10>`__)

    to install PETSc.

**Obtaining the source code**

From a terminal, ``cd`` to the directory where you want to store OpenFDEM and
type:

.. code::

    export BASEDIR=~/openfdem
    mkdir -p $BASEDIR
    cd $BASEDIR
    git clone https://github.com/OpenFDEM-geomechanics/OpenFDEM.git
    cd openfdem
    git checkout master

**Building OpenFDEM**

Go to the folder that contains the OpenFDEM folder and issue:

.. code::

    mkdir build
    cd build
    cmake ..
    cmake --build . -j$(nproc)

After the project is built, go to ``../build`` and open the project with Visual
Studio. When completed, the executables are located in the ``src/bin`` folder
and the Python module is located in the ``src/lib`` folder.


MacOS
------------------------

**Software requirements**

For MacOS, the user must have the following installed: xcode command line tools,
brew, cmake, gcc, gfortran, python, and open-mpi. All applications are installed
via the command line (some may already be installed).

1. **XCODE Command Line Tools** — to make Apple Clang and git available:

.. code::

    xcode-select install

2. **brew** — to install the HomeBrew package manager:

.. code::

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

3. **cmake, gfortran, python & open-mpi** — use brew to install:

.. code::

    brew install cmake
    brew install gcc
    brew install open-mpi
    brew install scalapack
    brew install python@3.9

    git clone https://github.com/scivision/mumps.git
    cd mumps
    mkdir build
    cd build
    cmake .. -Darith=d
    cmake --build . --config Release --parallel 8
    cd ..

**Obtaining the source code**

.. code::

    export BASEDIR=~/openfdem
    mkdir -p $BASEDIR
    cd $BASEDIR
    git clone https://github.com/OpenFDEM-geomechanics/OpenFDEM.git
    cd openfdem
    git checkout master

**Building OpenFDEM**

.. code::

    cd openfdem
    git pull
    mkdir build
    cd build
    conan install .. --build missing
    cmake .. -DMUMPS_DIR=$PWD/../../mumps/build -DOPENMPI=TRUE -DSCALAPACK_LIBRARIES=/usr/local/Cellar/scalapack/2.2.0_1/lib/libscalapack.dylib
    cmake --build . --config Release


Ubuntu
------------------------

**Software requirements**

For Ubuntu, the user must have a number of packages installed. These can be
installed from a terminal window:

.. code::

    sudo apt-get update
    sudo apt install cmake
    sudo apt install gcc g++ gfortran
    sudo apt install python3-pip
    sudo apt install liblapack-dev
    sudo apt install libopenmpi-dev
    sudo apt install libatlas-base-dev
    sudo apt install libeigen3-dev
    sudo apt install petsc-dev

    git clone https://github.com/scivision/mumps.git
    cd mumps
    mkdir build
    cd build
    cmake .. -Darith=d
    cmake --build . --config Release --parallel 4
    make
    sudo make install

**Obtaining the source code**

.. code::

    export BASEDIR=~/openfdem
    mkdir -p $BASEDIR
    cd $BASEDIR
    git clone https://github.com/OpenFDEM-geomechanics/OpenFDEM.git
    cd openfdem
    git checkout master

**Building the OpenFDEM applications**

.. code::

    cd openfdem
    git pull
    mkdir build
    cd build
    conan install .. --build missing
    cmake --build . --config Release

.. note::

    If you have more than **8** cores available, you can use the extra cores by
    changing the **8** value.


************************
Python Interface
************************

under construction


.. raw:: html

   <script type="text/javascript" id="mapmyvisitors" src="//mapmyvisitors.com/map.js?d=FhQBKeKNkCLqgUfZdslz45dHXRuV_WDVgVzZVYmuX7s&cl=ffffff&w=a"></script>

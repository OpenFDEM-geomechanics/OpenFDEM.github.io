Quick Start for Developers
===========================

This is the source code of C/C++ based OpenFDEM project developed by Dr. Xiaofeng Li, 
since 2017. This project is not limited to an FDEM solver for continuum-discontinuum problems, 
but is also capable of solving particulate DEM, material point method and phasefield problems.

The project can be complied by Visual Studio (> 2015) and compatible with Windows 7, 10 or Linux-like systems.

Tutorial examples can be found in ``..src\test\..``. The main file is located at ``src\solve\openfdem.cpp``. OpenFDEM is run by
parsing the input file. 

General steps to run OpenFDEM models:

1. Open ``.sln`` project in ``\openfdem src\of\OpenFDEM\OpenFDEM.sln`` by your local Visual Studio software.

2. Compile the project in Visual Studio  from the ``src\solve\openfdem.cpp`` main file.

3. The executable code should be in ``x64\Release``(or ``Debug``), be sure to keep the ``.dll`` files in the same folder with ``.exe`` file.

4. Drag the ``.of`` file into the ``.exe`` software then the model will starts to run, or use ``openfdem example.of`` in terminal to run a model.

Source Code Download
---------------------
The source code is hosted on the University of Toronto Gitlab: `OpenFDEM Gitlab`_.

.. _OpenFDEM Gitlab: http://geogroup.utoronto.ca:9191/gitlab/xiaofeng.li/openfdem_solver 

System Requirements
---------------------

- Windows x64
- Visual Studio (> 2015)

All external dependencies are included in the OpenFDEM download.
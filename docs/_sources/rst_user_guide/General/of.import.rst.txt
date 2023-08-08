of.import
================================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`import` :blue:`file_name` <string> 
    Import the file, the file type can be:
        -``.fdem``, which is self-defined for mesh import
        
        -``.fem``, which is save file after insitu stress equilibrium, only deformation, group and dfn information will be imported,
        
        -``.msh2`` or ``.msh``, which is standard mesh file from ``GMSH``, should not be over version 2.0
        
        -``.inp``, which is standard mesh file used by a lot commercial codes,
        
        -``.geo``, which is standard raw geometry file from ``GMSH``
        
        -``.stl``, which is for profile for 3D
        
        -``.dxf``, which is for the geometry build
        
        -``.step``, which is for the standard geometry from CAD
                
        -``.iges``, which is for the standard geometry from CAD
    

**Example:**

.. code-block:: 

    # Example
    of.import “mesh.msh”


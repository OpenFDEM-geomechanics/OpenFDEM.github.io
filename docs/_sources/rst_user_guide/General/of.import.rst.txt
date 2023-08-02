of.import
================================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`import` :blue:`file_name` <string> 
    Import the file, the file type can be:
        -.fdem, which is self-defined
        
        -.fem, which is for insitu balance,
        
        -.msh2 or .msh, which is standard mesh file, should not be over version 2.0
        
        -.inp, which is standard mesh file,
        
        -.geo, which is standard geometry file
        
        -.stl, which is for profile
        
        -.dxf, which is for the geometry
        
        -.step, which is for the standard geometry
    

**Example:**

.. code-block:: 

    # Example
    of.import “mesh.msh”


of.geometry.mesh
================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`geometry.mesh` :blue:`*mesh_algorithm*` <string> :blue:`*order*` <int>
    Set the method to create mesh. 

    **Parameters:** 
        **mesh_algorithm:** The parser forwards the mesh options to the
        geometry module. ``delaunay``, ``meshadapt`` and
        ``frontal-delaunay`` appear in the legacy documentation; their current
        availability should be checked with a minimal run.
        
        **order:** (default 1) The order can be set to 2 or 3 to generate higher order elements.
        

Example:
--------------------------------------------------------------------

.. code-block:: 

    # Default
    of.geometry.mesh delaunay
    # Alternative choice
    of.geometry.mesh meshadapt order 2

.. note::

    ``of.geometry.mesh`` is the parser spelling. The old example contained the
    typo ``of.gemetry.mesh``. The current parser source does not itself define
    the accepted algorithm and order values, so those values remain subject to
    runtime verification.



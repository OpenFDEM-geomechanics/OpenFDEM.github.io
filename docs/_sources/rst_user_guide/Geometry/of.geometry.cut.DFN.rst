of.geometry.cut.DFN
===================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`geometry.cut.DFN` :blue:`*new_geometry_tag*` <string> :blue:`*object_geometry_tag*` <string> :blue:`*dip_method*` <double, double> :blue:`*length_method*` <double, double> :blue:`*threshold_method*` <int>
    The joint may be deleted if you assign wrong minangle or wrong minsize
    Cut DFN sets by assigning the dip, length, threshold method of the joints.

    .. note::
        There are three rules to follow:
        
        - rule 1, you should set the domain firstly when you create jsets and dfns.

        - rule 2, recommend you preset the minangle and minsize to delete bad segments in case of causing bad mesh.

        - rule 3, change the iteration if the generation is not converged.




    **Parameters:** 
        **new_geometry_tag:** tag of the geometry group cut from the original geometry.

        **object_geometry_tag:** tag of the original geometry group

        **dip_method:** There are three methods to define dip:
        
        1. n_dip [mean, dev]
        2. u_dip [min, max]
        3. dip constantAngle;

        **length_method:** There are four methods to define length:
        
        1. length constantlength
        2. n_length [mean, dev]
        3. f_length [fisher1,fisher2]
        4. p_length [poer1, power2]

        **threshold_method:** There are three methods to define threshold:
        
        1. Count
        2. p10
        3. p21
        
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.geometry.cut.dfn [dfn1] [rock] u_dip [20, 60] n_length [4,2] count 200


of.geometry.cut.jset
====================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.** :red:`geometry.cut.jset` :blue:`*geometry_tag*` <string> :blue:`*object_geometry_tag*` <string> :blue:`*dip_method*` <double, double> :blue:`*space_method*` <double, double> :blue:`*trace_method*` <double, double> :blue:`*gap_method*` <double, double> :blue:`*start_point*` <double, double>
    |
    Cut a joint in an object by assign the <x> <y> <x> <y>…

    **Parameters:** 
        **geometry_tag:** tag of the joint set group.

        **object_geometry_tag:** tag of the original geometry group
        
        **dip_method:** There are three methods to define dip:
        1. n_dip [mean, dev]
        2. u_dip [min, max]
        3. dip constantAngle;

        **space_method:** There are two methods to define space:
        1. space constantSpace
        2. n_space [mean, dev]

        **trace_method:** There are two methods to define trace:
        1. trace constanttrace
        2. n_trace [mean, dev]

        **gap_method:** There are two methods to define gap:
        1. gap constantgap
        2. n_gap [mean, dev]

        **start_point:** to define the start points by <x><y>

    .. note::
        
        - rule 1, if you want to create persistent joint sets, only use dip, space and start point. If you want to create nonpersistent joint sets, use dip, space, trace, gap and start point together.
        
        - rule 2, for the dip angle ranging [0-90]. Start point should be located on the left-up corner. When the range is [90-180], it should be located at the down-left corner.
        
        - rule 3, you should set the domain first before you create jsets and dfns.
        
        - rule 4, recommend you preset the minangle and minsize to delete bad segments in case of causing bad mesh.
        
        - rule 5, start point is not mandatory, but it will help you locate the joint sets at the right places if you use that.
        
        - rule 6, the start points must be located within (not on) the domain.

|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.geometry.cut.jset [jset1] [rock] n_dip [60, 10] n_space [3,1] start [-10 10]
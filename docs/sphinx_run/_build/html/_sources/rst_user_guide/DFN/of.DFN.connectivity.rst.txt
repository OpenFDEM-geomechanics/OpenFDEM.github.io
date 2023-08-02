of.DFN.connectivity
===================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`DFN.connectivity` :blue:`*dfn_tag*` <string> :blue:`*N*` <int> :blue:`*node0*` <int> :blue:`*node1*` <int> :blue:`*node2*` <int> ...
    Create DFN groups by knowing its node ids.
    
    **Parameters:** 
        **dfn_tag:** tag of the DFN group

        **N:** size of the group

        **node:** node id      

|

Example:
--------------------------------------------------------------------

.. code-block:: 

    # 3 DFN ids in this DFN group
    of.DFN.connectivity 'dfn1' 3 0 14 27 26 48 56


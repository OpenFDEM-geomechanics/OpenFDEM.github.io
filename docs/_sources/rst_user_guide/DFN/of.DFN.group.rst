of.DFN.group
============

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`DFN.group` :blue:`*dfn_tag*` <string> :blue:`*N*` <int> :blue:`*dfn_id1*` <int> :blue:`*dfn_id2*` <int> ...
    Create DFN groups by knowing its DFN ids.
    
    **Parameters:** 
        **dfn_tag:** tag of the DFN group

        **N:** size of the group

        **dfn_id:** DFN id        

|

Example:
--------------------------------------------------------------------

.. code-block:: 

    # 3 DFN ids in this DFN group
    of.DFN.group 'dfn1' 3 14 27 15


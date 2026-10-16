of.import.FEM.dfn
=================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`import.FEM.dfn` :blue:`*tag*` <string> :blue:`*node_count*` <int> :blue:`*node_id1*` <int> :blue:`*node_id2*` <int> [:blue:`*node_id3*` <int>]
    Import a DFN record from FEM-style data. For two-node records the parser
    reads two node IDs; for other counts it reads two node IDs and a quadratic
    node ID.

    **Parameters:**
        **tag:** (default none) DFN group tag.

        **node_count:** number of nodes in the imported record.

        **node_id1:** first node ID.

        **node_id2:** second node ID.

        **node_id3:** optional quadratic node ID.

Example:
--------------------------------------------------------------------

.. code-block::

    of.import.FEM.dfn 'dfn_1' 2 10 11

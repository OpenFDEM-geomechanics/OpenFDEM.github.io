of.set.module
================================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`set.module` :blue:`*type*` <string> :blue:`*switch*` <bool>
    Turn on or off for special modules.
    
    **Parameters:** 
        **type:** Modules currently available are ``hydro``, ``thermal``, ``blast``,
        ``blast_hydro`` and ``dynamic``.


Example:
--------------------------------------------------------------------

.. code-block:: 

    # Hydro modules
    of.set.module hydro on
    of.set.module hydro off

    # Thermal modules
    of.set.module thermal on
    of.set.module thermal off

    # Blast modules
    of.set.module blast on
    of.set.module blast off

    # Dynamic modules
    of.set.module dynamic on
    of.set.module dynamic off

    # Coupled blast-hydro module
    of.set.module blast_hydro

.. blast_hydro is handled as a combined switch and does not read a
.. following on/off token in the current parser. dynamic off needs runtime
.. verification before documenting it as fully supported.

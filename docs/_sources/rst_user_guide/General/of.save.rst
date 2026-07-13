of.save
================================

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`save` :blue:`*file_name*` <string>
    Save the model. OpenFDEM supports data to be saved in .json, .xml and .bin formats.
    
    .. note::
        Also see :doc:`of.restore<of.restore>`.

    |
    **Parameters:** 
        **file_name:** File name of the data file.

**Example:**

.. code-block:: 

    of.save 'usc.json'




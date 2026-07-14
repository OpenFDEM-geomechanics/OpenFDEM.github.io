of.mat.contact
==============

.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

**of.**\ :red:`mat.contact` :blue:`*element_tag*` <string> :blue:`*material_type*` <string> :blue:`parameter_keyword1` <string> :blue:`parameter_value1` <double> ...
    |
    Assign the material parameters to the target element group pairs. The details of materials in OpenFDEM can be found in the table below.
    

    +-----------------+------------------+----------------------------------------+-------+
    | Material type   | Constitutive     | Parameter keywords                     | Units |
    |                 | keyword          |                                        |       |
    +=================+==================+========================================+=======+
    | Mohr-Coulomb    | *MC*             | *fri*\ ction -                         |       |
    | Slip            |                  | friction                               |       |
    +-----------------+------------------+----------------------------------------+-------+
    |                 |                  | *kn* - normal                          | Pa    |
    |                 |                  | stiffness, will be                     |       |
    |                 |                  | assigned by default                    |       |
    |                 |                  |                                        |       |
    |                 |                  | .. math:: pn = \lambda(K_{1} + K_{2})/2|       |
    +-----------------+------------------+----------------------------------------+-------+
    |                 |                  | ks - tangential                        | Pa    |
    |                 |                  | stiffness, will be                     |       |
    |                 |                  | assigned by default                    |       |
    |                 |                  |                                        |       |
    |                 |                  | .. math:: pn = \lambda(G_{1} + G_{2})/2|       |
    +-----------------+------------------+----------------------------------------+-------+
    | Rate dependent  | *rMC*            | To be added in the                     |       |
    | Mohr-Coulomb    |                  | tutorial, if you want                  |       |
    | Slip            |                  | to use this model,                     |       |
    |                 |                  | contact the developer                  |       |
    +-----------------+------------------+----------------------------------------+-------+
    | Giovanni        | *roughshear*     | *fri*\ ction -                         |       |
    | Grasselli rough |                  | friction                               |       |
    | shear contact   |                  |                                        |       |
    +-----------------+------------------+----------------------------------------+-------+
    |                 |                  | *kn* - normal                          | Pa    |
    |                 |                  | stiffness, will be                     |       |
    |                 |                  | assigned by default                    |       |
    |                 |                  |                                        |       |
    |                 |                  | .. math:: pn = \lambda(K_{1} + K_{2})/2|       |
    +-----------------+------------------+----------------------------------------+-------+
    |                 |                  | ks - tangential                        | Pa    |
    |                 |                  | stiffness, will be                     |       |
    |                 |                  | assigned by default                    |       |
    |                 |                  |                                        |       |
    |                 |                  | .. math:: pn = \lambda(G_{1} + G_{2})/2|       |
    +-----------------+------------------+----------------------------------------+-------+
    |                 |                  | theta -parameter                       |       |
    +-----------------+------------------+----------------------------------------+-------+
    |                 |                  | C -parameter                           |       |
    +-----------------+------------------+----------------------------------------+-------+
    |                 |                  | *A0* - parameter                       |       |
    +-----------------+------------------+----------------------------------------+-------+
    |                 |                  | *B* -parameter                         |       |
    +-----------------+------------------+----------------------------------------+-------+
    |                 |                  | *tension* - tension                    |       |
    |                 |                  | strength                               |       |
    +-----------------+------------------+----------------------------------------+-------+
    | Dynamic         | *dMC*            | *s_fri*\ ction -                       |       |
    | Mohr-Coulomb    |                  | static friction                        |       |
    | Slip            |                  |                                        |       |
    +-----------------+------------------+----------------------------------------+-------+
    |                 |                  | *d_fri*\ ction -                       |       |
    |                 |                  | dynamic friction                       |       |
    +-----------------+------------------+----------------------------------------+-------+
    |                 |                  | *slip_rate*- slip rate                 | /s    |
    +-----------------+------------------+----------------------------------------+-------+
    |                 |                  | *kn* - normal                          | Pa    |
    |                 |                  | stiffness, will be                     |       |
    |                 |                  | assigned by default                    |       |
    |                 |                  |                                        |       |
    |                 |                  | .. math:: pn = \lambda(K_{1} + K_{2})/2|       |
    +-----------------+------------------+----------------------------------------+-------+
    |                 |                  | ks - tangential                        | Pa    |
    |                 |                  | stiffness, will be                     |       |
    |                 |                  | assigned by default                    |       |
    |                 |                  |                                        |       |
    |                 |                  | .. math:: pn = \lambda(G_{1} + G_{2})/2|       |
    +-----------------+------------------+----------------------------------------+-------+
    | Hertz contact   | *HERTZ*          | To be added in the                     |       |
    | model           |                  | tutorial, if you want                  |       |
    |                 |                  | to use this model,                     |       |
    |                 |                  | contact the developer                  |       |
    +-----------------+------------------+----------------------------------------+-------+
    | Friction        | *FRICTION*       | To be added in the                     |       |
    |                 |                  | tutorial, if you want                  |       |
    |                 |                  | to use this model,                     |       |
    |                 |                  | contact the developer                  |       |
    +-----------------+------------------+----------------------------------------+-------+


    
|

Example:
--------------------------------------------------------------------

.. code-block:: 

    of.mat.contact 'default' MC 0.3
    of.mat.contact 'up' ‘rock’ MC 0.0




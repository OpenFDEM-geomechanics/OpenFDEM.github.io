OpenFDEM input files use a Python-like format and the dot is used to
clarify the hierarchy of different classes.

The first layer is OpenFDEM, declared as ``.of`` or ``.OpenFDEM``, but the
commands in other layers cannot be shortened (for example, of.nodal or
OpenFDEM.nodal).

.. contents:: Table of Contents
    :depth: 2
    :backlinks: none

general commands
==================

of.new 
------

**meaning** [Optional]: Clear all variables from your last computation (i.e. start of a new OpenFDEM run).

**demo**::

 of.new

of.restore 
----------

**meaning** [Optional]: call the saved binary computation results.

**demo**::

 of.restore “filename.sav”

of.result 
---------

**meaning** [Optional]: assign the results folder, default value is ``../result``.

**demo**::

 of.result “c:/user/openfdem example/result”

of.save 
-------

**meaning**: save the binary computation results.

**demo**::

 of.save “c:/user/openfdem example/result/insitu.sav”

of.import 
---------

**meaning**: import files, currently supports all formats of ``.inp`` files, ``.msh`` files (no more than 2.0
version), ``.msh2`` files, ``.geo`` files and ``.ofdem`` files (default format for OpenFDEM).

OpenFDEM read all information from your mesh, including nodal physical, group, element physical group.

OpenFDEM 4.6+ version can read ``.tess`` and ``.stl``

**demo**::

 of.import “c:/user/openfdem example/result/ucs.msh”

of.debug on 
-----------

**meaning** [Optional]: turn on the debug mode, the default is off. Debugging will increase the run-time but a ``.log`` file will 
be generated when this mode is on.

**demo**::

 of.debug on or of.debug off

config
========

of.config.type planestress/planestrain 
--------------------------------------

**meaning**: choosing plane stress or plane strain, the default is plane stress

**demo**::

 of.config.type planestrain
 
of.config.module hydro/blast/thermal 
------------------------------------

**meaning**: choosing mechanical module, the default is mechanical

**demo**::

 of.config.module hydro
 of.config.module blast
 of.config.module thermal

geometry
==========

You can create meshes based on the built-in command line functions. OpenFDEM also supports creating ``retangular``, ``circle``, ``ellipse``, 
``arbitary polygon`` from tables.  The bool operators support ``intersection``, ``union``, ``difference``, and ``fragment`` between different entities. 

of.geometry.square name x0 y0 x1 y1 x2 y2 x3 y3
-----------------------------------------------

**meaning**: create a geometry using square range, and the geometry tag
is ‘name’

**demo**::

 of.geometry.square ‘rock1’ 0.0 1.0 1.0 2.0 2.0 3.0 4.0 2.0

of.geometry.polygon name n x0 y0 x1 y1 x2 y2 x3 y3
--------------------------------------------------

**meaning**: create a geometry using polygon range, the geometry tag is
‘name’ and the vertex count is n

**demo**::

 of.geometry.polygon ‘rock1’ 5 0.0 1.0 1.0 2.0 2.0 3.0 4.0 2.0 3.0 5.2

of.geometry.table name ‘table.tab’
----------------------------------

**meaning**: create a geometry. All point cords are put in the
table file.

**table format**: 
   x0, y0
   x1, y1
   x2, y2
   ...

**demo**::

 of.geometry.table ‘rock1’ ‘tablerock.tab’

of.geometry.circle name x0 y0 r n
---------------------------------

**meaning**: create a geometry using circle range, the geometry tag is
‘name’. The centric point is (x1, y1), radius is r and edge count is n, deafault is 50.

**demo**::

 of.geometry.circle ‘tunnel’ 0.0 0.0 1.0 20

of.geometry.ellipse name x0 y0 rmax rmin theta n
------------------------------------------------

**meaning**: create a geometry using ellipse range, where the geometry tag is
‘name’ and the centric point is (x0, y0). Radiuses are rmax and rmin,
and edge count is n, default is 50.

**demo**::

 of.geometry.ellipse ‘ellipsetunnel’ 0.0 0.0 1.0 0.5 20

of.geometry.cut.square name name2 x0 y0 x1 y1 x2 y2 x3 y3
---------------------------------------------------------

**meaning**: cut a rectangular tunnel in existing *‘name2’* group geometry,
but the *‘name’* group is not excavated.

**demo**::

 of.geometry.cut.square ‘square_tunnel’ ‘rock’ 0.0 1.0 1.0 2.0 2.0 3.0 4.0 2.0

of.geometry.cut.polygon name name2 n x0 y0 x1 y1 x2 y2 x3 y3
------------------------------------------------------------

**meaning**: cut a polygon tunnel in existing *‘name2’* group geometry, but
the *‘name’* group is not excavated.

**demo**::

 of.geometry.cut.polygon ‘polygon_tunnel’ ‘rock’ 4 0.0 1.0 1.0 2.0 2.0 3.0 4.0 2.0

of.geometry.cut.table name name2 ‘table.tab’
--------------------------------------------

**meaning**: cut a table tunnel in existing ‘name2’ group geometry, but the
‘name’ group is not excavated.

**demo**::

 of.geometry.cut.table ‘tunnel_from_table’ ‘rock’ ‘tunneltable.tab’

of.geometry.cut.circle name name2 x0 y0 r n
-------------------------------------------

**meaning**: cut a circular tunnel in existing ‘name2’ group geometry, but the
‘name’ group is not excavated.

**demo**::

 of.geometry.cut.circle ‘circle_tunnel’ ‘rock’ 0.0 0.0 1.0 20

of.geometry.cut.ellipse name name2 x0 y0 rmax rmin theta n
----------------------------------------------------------

**meaning**: cut a elliptical tunnel in existing ‘name2’ group geometry, but
the ‘name’ group is not excavated.

**demo**::

 of.geometry.cut.ellipse ‘ellipse_tunnel’ ‘rock’ 0.0 0.0 1.0 0.5 20

of.geometry.cut.jset name name2 dip length space gap
----------------------------------------------------

**meaning**: create jset ‘name2’ group geometry in ‘name’ group

method: default, normal, uniform, exponential, log_normal, power

cdip ndip udip edip logdip pdip

dip: dip udip ndip

length: length nlength flength plength

space: space nspace

gap: gap ngap

**demo**::

 of.geometry.cut.jset 'jset-1' 'rock_0' n_dip 60 20 n_space 0.2 0.1

of.geometry.cut.dfn name name2 method dip length 
------------------------------------------------

method: count, p21(length/area), p10 (n/edge length)

dip: dip udip ndip

length: length nlength flength

**demo**::

 of.geometry.cut.dfn 'dfn-1' 'rock_0' p10 3 n_dip 60 5 n_length 0.3 0.1

of.geometry.import.rdfn pixel_ratio name name2 name 
---------------------------------------------------

**demo**::

 of.geometry.import.rdfn 1.0 'dfn-1' 'rock_0' 'fault.dat'

of.geometry.remove.square name name2 x0 y0 x1 y1 x2 y2 x3 y3
------------------------------------------------------------

**meaning**: remove a rectangular tunnel in existing ‘name2’ group geometry,
the ‘name’ group is excavated as null

**demo**::

 of.geometry.remove.square ‘rock2’ ‘rock’ 0.0 1.0 1.0 2.0 2.0 3.0 4.0 2.0

of.geometry.remove.polygon name name2 n x0 y0 x1 y1 x2 y2 x3 y3
---------------------------------------------------------------

**meaning**: remove a polygon tunnel in existing ‘name2’ group geometry, the
‘name’ group is excavated as null

**demo**::

 of.geometry.remove.polygon ‘rock2’ ‘rock’ 0.0 1.0 1.0 2.0 2.0 3.0 4.0 2.0

of.geometry.remove.table name name2 ‘table.tab’
-----------------------------------------------

**meaning**: remove a table tunnel in existing ‘name2’ group geometry, the
‘name’ group is excavated as null

**demo**::

 of.geometry.remove.table ‘rock2’ ‘rock’ 0.0 1.0 1.0 2.0 2.0 3.0 4.0 2.0

of.geometry.remove.circle name name2 x1 y1 r n
----------------------------------------------

**meaning**: remove a circle tunnel in existing ‘name2’ group geometry, the
‘name’ group is excavated as null

**demo**::

 of.geometry.remove.circle ‘rock2’ ‘rock’ 0.0 1.0 1.0 2.0 2.0 3.0 4.0 2.0

of.geometry.remove.ellipse name name2 x0 y0 rmax rmin theta n
-------------------------------------------------------------

**meaning**: remove a ellipse tunnel in existing ‘name2’ group geometry, the
‘name’ group is excavated as null

**demo**::

 of.geometry.remove.ellipse ‘rock2’ ‘rock’ 0.0 1.0 1.0 2.0 2.0 3.0 4.0 2.0

of.geometry.mesh.size name default
-----------------------------------

**meaning**: assign the mesh size to corresponding geometry groups, ‘all’
means the all geometries

**demo**::

 of.geometry.mesh.size 'all' 0.2

of.geometry.mesh keyword
------------------------

**meaning**: method used to generate mesh, default is delaunay

keyword: meshadapt(default), delaunay, frontal-delaunay

**demo**::

 of.geometry.mesh meshasapt

mesh_insert 
=============

of.mesh.insert elementgroup
---------------------------

**meaning**: insert the CZMs for specific element groups, ‘all’ means insert
CZMs in all model

**demo**::

 of.mesh.insert ‘rock’

 of.mesh.insert ‘all’

.. note: ‘all’ is a reserved keyword indicates all elements in current model, can not be used for group name.

nodal 
=======

of.nodal.coord number_nodes
----------------------------

**meaning**: input nodes for the .fdem format

**demo**::

 of.nodal.coord 3

   0.1 0.3

   0.2 0.6

   0.8 0.2

element 
=========

of.element.connectivity number_nodes number_elements
-------------------------------------------------------

   x1 y1 x2 y2 x3 y3…

**meaning**: input elements for the .fdem format, in anticlockwise order

**demo**::

 of.element.connectivity 3 3

   0 3 15

   1 2 7

   2 4 6

contact
=========

of.contact.detection nbs
------------------------

**meaning**: the contact detection method, current methods are: Munjiza model, NBS,
modified NBS and Li-Grasselli’s method [default].

**demo**::

 of.contact. detection nbs

of.contact.force lig
--------------------

**meaning**: the contact force method, current methods are: Munjiza model,
and Li-Grasselli’s method [default].

**demo**::

 of.contact.force lig

cohelement 
============

of.cohelement.delete cohelementgroup
------------------------------------

group
=======

nodal groups
--------------

of.group.nodal.square nodalgroupname x1 x2 y1 y2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**meaning**: create nodal group using rectangular range

**demo**::

 of.group.nodal.square ‘rock’ -50.0 50.0 -50.0 10.0

of.group.nodal.circle nodalgroupname x1 y1 r
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**meaning**: create nodal group using circle range, the nodes within the
circle

**demo**::

 of.group.nodal.circle ‘tunnel’ 0.0 0.0 2.5

of.group.nodal.circle.outer nodalgroupname x1 y1 r
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**meaning**: create nodal group out of the circle range

**demo**::

 of.group.nodal.circle.outer ‘tunnel’ 0.0 0.0 2.5

of.group.nodal.circle.on nodalgroupname x1 y1 r
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**meaning**: create nodal group on of the circle boundary

**demo**::

 of.group.nodal.circle.on ‘tunnel’ 0.0 0.0 2.5

of.group.nodal.plane.left nodalgroupname x1 y1 x2 y2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**meaning**: create nodal group on the left of the predefined plane

**demo**::

 of.group.nodal.plane.left ‘slope’ 0.0 0.0 1.0 2.7

of.group.nodal.plane.right nodalgroupname x1 y1 x2 y2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**meaning**: create nodal group on the right of the plane

**demo**::

 of.group.nodal.plane.right ‘slope’ 0.0 0.0 1.0 2.7

of.group.nodal.plane nodalgroupname x1 y1 x2 y2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**meaning**: create nodal group on the plane

**demo**::

 of.group.nodal.plane ‘slope’ 0.0 0.0 1.0 2.7

of.group.nodal.from.element ‘up’ ‘up’
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**meaning**: create nodal group from the element group

**demo**::

 of.group.nodal.from.element ‘rock’ ‘rock’

bool
-------

of.group.nodal.bool.union nodalgroupnename nodalgroupnamea nodalgroupnameb
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**meaning**: create nodal group using bool union

**demo**::

 of.group.nodal.bool.union ‘rock1’ ‘rock2’

of.group.nodal.bool.intersect nodalgroupnewname nodalgroupnamea nodalgroupnameb
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**meaning**: create nodal group using bool intersect

**demo**::

 of.group.nodal.bool.intersect ‘rock1’ ‘rock2’

of.group.nodal.bool.subtract nodalgroupnewname nodalgroupnamea nodalgroupnameb a-b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**meaning**: create nodal group using bool subtract

**demo**::

 of.group.nodal.bool.subtract‘rock1’ ‘rock2’

.. _element-1:

element
----------

of.group.element.square elementgroupname x1 x2 y1 y2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**demo**::

 of.group.element.square ‘rock’ -50.0 50.0 -50.0 10.0

of.group.element.circle elementgroupname x1 y1 r
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**demo**::

 of.group.element. circle ‘tunnel’ 0.0 0.0 2.5

of.group.element.circle.outer elementgroupname x1 y1 r
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

of.group.element.plane.left elementgroupname x1 y1 x2 y2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**demo**::

 of.group.element. .left ‘slope’ 0.0 0.0 1.0 2.7

of.group.element.plane.right elementgroupname x1 y1 x2 y2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

of.group.element.bool.union elementgroupnewname elementgroupnamea elementgroupnameb
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

of.group. element.bool.intersect elementgroupnewname elementgroupnamea elementgroupnameb
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _section-1:

of.group. element.bool.subtract elementgroupnewname elementgroupnamea elementgroupnameb a-b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

cohesive element
-------------------

of.group.cohelement.square cohelementgroupname x1 x2 y1 y2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**demo**::

  of.group. cohelement.square ‘rock’ -50.0 50.0 -50.0 10.0

of.group.cohelement.circle cohelementgroupname x1 y1 r (default)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _section-2:

of.group.cohelement.circle.outer cohelementgroupname x1 y1 r
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _section-3:

of.group.cohelement.circle.on cohelementgroupname x1 y1 r
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _section-4:

of.group.cohelement.plane.left cohelementgroupname x1 y1 x2 y2 (default)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _section-5:

of.group.cohelement.plane.right cohelementgroupname x1 y1 x2 y2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _section-6:

of.group.cohelement.plane cohelementgroupname x1 y1 x2 y2 (default)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _section-7:

of.group.cohelement.gbm cohelementgroupname elementgroupname1 elementgroupname2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**demo**::

 of.group.cohelement.gbm 'qtz-qtz' 'qtz' 'qtz' # quartz group

of.group.cohelement.dfn cohelementgroupname dfnname
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**demo**::

 of.group.cohelement.dfn 'dfn1' 'dfn1'

of.group.cohelement.bool.union cohelementgroupnewname cohelementgroupnamea cohelementgroupnameb
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _section-8:

of.group. cohelement.bool.intersect cohelementgroupnewname cohelementgroupnamea cohelementgroupnameb
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _section-9:

of.group. cohelement.bool.subtract cohelementgroupnewname cohelementgroupnamea elementgroupnameb a-b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

boundary
==========

.. _nodal-1:

nodal
-------

of.boundary.nodal.force nodalgroupname xy force_x force_y
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**meaning**: assign force boundary to nodal groups

**demo**::

 of.boundary.nodal.force ‘rock’ xy -50.0 27.0
 of.boundary.nodal.force ‘rock’ x -50.0
 of.boundary.nodal.force ‘rock’ y 27.0

.. note: should group element in advance; ‘all’ is a reserved keyword indicates all elements in current model, can not be used for group name.

of.boundary.nodal.velocity nodalgroupname xy vel_x vel_y
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**meaning**: assign normal velocity boundary to nodal groups (in local
coords)

of.boundary.nodal.inivelocity nodalgroupname xy vel_x vel_y
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**meaning**: assign initial velocity boundary to nodal groups (in local
coords)

of.boundary.nodal.acceleration nodalgroupname xy acc_x acc_y
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**meaning**: assign aceleration boundary to nodal groups (in local coords)

of.boundary.nodal.viscous nodalgroupnamexy viscous_x viscous_y
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**demo**::
 
 of.boundary.nodal.viscous ‘rock’ xy
 of.boundary.nodal.viscous ‘rock’ x
 of.boundary.nodal.viscous ‘rock’ y

.. note: no need value for viscous boundary.

.. _of.boundary.nodal.viscous-nodalgroupnamexy-viscous_x-viscous_y-1:

of.boundary.nodal.viscous nodalgroupnamexy viscous_x viscous_y
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

nodal local edge
------------------

of.boundary.nodal.force.local nodalgroupname xy force_normal force_shear
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

of.boundary.nodal.velocity.local nodalgroupname xy vel\_ normal vel\_ shear
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

of.boundary.nodal.acceleration.local nodalgroupname xy acc\_ normal acc\_ shear
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**demo**::

 of.boundary.nodal.force.local ‘rock’ xy -50.0 27.0
 of.boundary.nodal.force.local ‘rock’ x -50.0
 of.boundary.nodal.force.local ‘rock’ y 27.0

.. note:local boundary is assigned to edge only, two both nodes should be in the nodal group of ‘rock’.

of.boundary.nodal.force.local.table nodalgroupname xy force_normal force_shear tablename
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

of.boundary.nodal.velocity. table nodalgroupname xy vel\_ normal vel\_ shear tablename
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

of.boundary.nodal.acceleration. table nodalgroupname xy acc\_ normal acc\_ shear tablename
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**demo**::

 of.boundary.nodal.force.local ‘rock’ xy -50.0 27.0

   of.boundary.nodal.force.local ‘rock’ x -50.0

   of.boundary.nodal.force.local ‘rock’ y 27.0

.. note:local boundary is assigned to edge only, two both nodes should be in the nodal group of ‘rock’.

nodal table
-------------

of.boundary.nodal.force.table nodalgroupname xy force_x force_y tablename 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**demo**::

 of.boundary.nodal.force.table ‘rock’ xy -50.0 27.0 blast
 of.boundary.nodal.force.local ‘rock’ x -50.0
 of.boundary.nodal.force.local ‘rock’ y 27.0

.. note: table should be defined in advance.

of.boundary.nodal.velocity.table nodalgroupname xy vel_x vel_y tablename tablename
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

of.boundary.nodal.acceleration.table nodalgroupname xy acc_x acc_y tablename tablename
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _section-10:

of.boundary.pressure.normal nodalgroupname value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

of.boundary.pressure.shear nodalgroupname value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**demo**::

 of.boundary.pressure .normal‘rock’ -50.0
 of.boundary.pressure.shear ‘rock’ -50.0

.. note: pressure is added on the edge.

of.boundary.pressure.normal.table nodalgroupname value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

of.boundary.pressure.shear.table nodalgroupname value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**demo**::

 of.boundary.pressure.normal.table ‘rock’ -50.0 gas

hydro
-------

of.boundary.hydro.porepressure nodalgroup p p_x p_y
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

of.boundary.hydro.waterlevel nodalgroup water_y initial_p
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

of.boundary.hydro.pressure nodalgroup value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

of.boundary.hydro.pressure.table nodalgroup value tablename
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

of.boundary.hydro.flow nodalgroup flow_rate_value initial_p
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

of.boundary.hydro.flow.table nodalgroup value value2 tablename
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

of.boundary.hydro.impermeable nodalgroup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

blast
-------

of.boundary.blast nodalgroup value tablename
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

element
---------

of.boundary.element.stress elementgroupname sxx sxy syy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**demo**::

 of.boundary.element.stress ‘all’ -20e6 2e6 -2e6
 of.boundary.element.stress.xgrad elementgroupname sxx.x sxy.x syy.x
 of.boundary.element.stress.ygrad elementgroupname sxx.y sxy.y syy.y


of.boundary.excavation elementgroupname 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

of.boundary.uncontact elementgroupname 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

thermal
---------

of.boundary.thermal.t0 nodalgroupvalue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

of.boundary.thermal.temperature nodalgroupvalue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _section-15:

material
==========

of.mat.element elementgroupname(all) modelname p1 p2 p3 …
---------------------------------------------------------

**demo**::

 of.mat.element ‘all’ elastic den 2500 e 40e9 v 0.2
 of.mat.element ‘rock’ mc den 2500 e 40e9 v 0.2 ten 10e6 coh 30e6 fric 0.3

of.mat.particle elementgroupname(all) modelname p1 p2 p3 …
----------------------------------------------------------

**demo**::

 of.mat.particle ‘all’ rigid den 2500

of.mat.cohesive cohelementgroupname(all) modelname p1 p2 p3 …
-------------------------------------------------------------

**demo**::

 of.mat.cohesive ‘all’ em pn 1e10 pt 0.5e10 ten 30e6 coh 30e6 fric 0.3 gi 100 gii 300 (pn pt ten coh fri gi gii)

of.mat. cohesive ‘rock’ em_het power 0.5 dip 35 ten 30e6 3e6 coh 30e6 3e6 fric 0.3 0 gi 100 20 gii 300 30 (power, dip, mean pn, dev pn, mean pt, dev pt, mean ten, dev ten, mean coh, dev coh, mean fri, dev fri, mean gi, dev gi, mean gii, dev gii)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. _section-16:

of.mat.contact elementgroupname1 elementgroupname2(all) modelname p1 p2 p3 … 
----------------------------------------------------------------------------

**demo**:: 

   of.mat.contact ‘all’ mc kn 2e10 ks 1e10 fric 0.3
   of.mat.contact ‘rock’ ‘plate’ mc kn 2e10 ks 1e10 fric 0.3 kn ks

of.mat.fluid den bulk viscousity cohesion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**demo**::

 of.mat.fluid den 1000.0 k 3e8 viscosity 1e6 cohesion 3e6

of.mat.fluid.matrix elementgroupname(all) permeability m alpha
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**demo**::

 of.mat.fluid.matrix 'all' permeability 1.0e-8 biot_k 22e9 biot_c 0.1

of.mat.fluid.fracture cohelementgroupname(all) aperature_0 apreature_min para_exp para_b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**demo**::

 of.mat.fluid.fracture 'joint' a0 5e-4 power 3.0 b 1.0

of.mat.gas initial_den permeability initial_bulk constant_b alpha
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**demo**::

 of.mat.fluid.fracture 'joint' density0 1.29 permiability 200 k0 1.01e5 b
 1.0 alpha 0.1

gbm
=====

of.gbm numberofminerals m1_name ratio m2_name ratio …
-----------------------------------------------------

**demo**::

 of.gbm 3 'qtz' 0.3 'fel' 0.46 'bio' 0.24 (area ratio)

history
=========

of.history.nodal.force id x1 y1
-------------------------------

of.history.nodal.vel id x1 y1
-----------------------------

of.history.nodal.dis id x1 y1
-----------------------------

of.history.nodal.fluid.pressure id x1 y1
----------------------------------------

of.history.nodal.fracture.pressure id x1 y1
-------------------------------------------

of.history.nodal.matrix.pressure id x1 y1
-----------------------------------------

of.history.nodal.temperature id x1 y1
-------------------------------------

.. _section-17:

of.history.nodal.group.force id groupname
-----------------------------------------

of.history.nodal.group.vel id groupname
---------------------------------------

of.history.nodal.group.dis id groupname
---------------------------------------

of.history.nodal.group.fluid.pressure id groupname
--------------------------------------------------

of.history.nodal.group.fracture.pressure id groupname
-----------------------------------------------------

of.history.nodal.group.matrix.pressure id groupname
---------------------------------------------------

of.history.nodal.group.temperature id groupname
-----------------------------------------------

   note: average value in this group

of.history.element.stress id x1 y1
----------------------------------

of.history.element.strain id x1 y1
----------------------------------

of.history.element.strainrate id x1 y1
--------------------------------------

.. _section-18:

of.history.element.group.stress id groupname
--------------------------------------------

of.history.element.group.strain id groupname
--------------------------------------------

of.history.element.group.strainrate id groupname
------------------------------------------------

.. _section-19:

of.history.cohelement.dis id x1 y1
----------------------------------

of.history.cohelement.force id x1 y1
------------------------------------

of.history.cohelement.vel id x1 y1
----------------------------------

of.history.cohelement.shearstrength id x1 y1
--------------------------------------------

.. _section-20:

of.history.cohelement.group.dis id groupname
--------------------------------------------

of.history.cohelement.group.force id groupname
----------------------------------------------

of.history.cohelement.group.vel id groupname
--------------------------------------------

of.history.cohelement.group.shearstrength id groupname
------------------------------------------------------

.. _section-21:

.. _section-22:

of.history.energy
-----------------

of.history.unbalance
--------------------

of.history.solveratio
---------------------

.. _section-23:

of.history.interval intervalvalue
---------------------------------

of.history.pv.interval intervalvalue
------------------------------------

of.history.pv.reduced.interval intervalvalue fracturethreshold intervalvalue 
----------------------------------------------------------------------------

paraview 
------------

of.history.pv.field fieldkeywords
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   fieldkeywords: velocity force displacement fluid_pressure nodal_group
   element_group gbm_group mass stress strain strain_rate
   principal_stress mat_id fragment

of.history.pv.fracture fracturekeywords
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   fracturekeywords: mode sliding opening area time length energy

of.history.pv.damage damagekeywords
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   damagekeywords: mode sliding opening area time length

of.history.pv.cohesive cohesivekeywords
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   cohesivekeywords: velocity force displacement shear_strength dfn
   mat_id group

of.history.pv.ae aekeywords
~~~~~~~~~~~~~~~~~~~~~~~~~~~

   aekeywords: mode time win_time win_kinetic kinetic magnitude energy

dfn
=====

of.dfn.connectivity dfnnum 
--------------------------

   n1 n2 …

**demo**::

   of.dfn.connectivity 1000 1 15 2 19 1000 999 …
   of.dfn.group dfnname setnum dfn1 dfn4 dfn12…

**demo**::

 of.dfn.group ‘dfn_1’ 3 1 7 12

.. _section-24:

of.dfn.type dfnname dfn_enum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**demo**::

 of.dfn.type ‘jset1’ cohesive

table 
=======

of.table tablename ‘table1.dat’
-------------------------------

format of table::

   t1 t2 num
   n1 n2 n3 …
   struct table:
   {char\* tag;
   double t1;
   double t2;
   unsigned int num;
   double\* data;}

**demo**::

 of.table tab1 ‘table1.dat’

damping
=========

of.damp.global value
--------------------

**demo**::

 of.damp.global 0.7

.. note: global damping value should not be > 1.0.

**demo**::

 of.damp.rayleigh elementgroupname value1 value2
 of.damp.rayleigh.mass elementgroupname value
 of.damp.rayleigh.stiffness elementgroupname value

hydro
=======

of.hydro.timestep value
-----------------------

**demo**::

 of.hydro.timestep 1e-9
 of.hydro.matrix off
 of.hydro.mechanical off
 of.hydro.fracture on

gravity 
=========

of.gravity x y
--------------

**demo**:: 
   of.gravity 0.0 -9.8

.. note: the default gravity is 0.0.

seismic
=========

of.seismic.window value
-----------------------

**demo**::

 of.seismic.window 1.0e-3

.. note: the default method is instantaneous. Value == 0 is instantaneous method, !=0 uses the window method. 

1. of.timestep auto or fix value

2. of.step

3. of.stop



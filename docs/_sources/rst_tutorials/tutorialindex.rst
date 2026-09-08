Examples
===================================

.. raw:: html

   <script>
   // 页面无锚点时,加载后自动定位到 "How to create a geometry" 小节
   if (!window.location.hash) {
     window.addEventListener('DOMContentLoaded', function () {
       var el = document.getElementById('how-to-create-a-geometry');
       if (el) { el.scrollIntoView(); }
     });
   }
   </script>

.. toctree::
   :maxdepth: 1

   tutorial0_Geometry
   tutorial1_UCS_Test
   tutorial2_UCS_with_Gmsh
   tutorial3_UCS_Test_with_Quadrangle_Elements
   tutorial4_BD_Test
   tutorial5_In_Situ_Stress
   tutorial6_Hydro_Seepage
   tutorial7_Hydro_Fracture_Flow
   tutorial8_Thermal_Flux
   tutorial9_GBM
   tutorial10_Phase_Field


How to create a geometry
-----------------------------------------
|

.. grid:: 2
   
   .. grid-item-card:: Geometry
      :img-top: ../_static/Desmos/UCS.png
      :link: tutorial0_Geometry
      :link-type: doc


Benchmark tests
-----------------------------------------
|

.. grid:: 2
   
   .. grid-item-card:: Uniaxial Compression Test
      :img-top: ../_static/Desmos/UCS.png
      :link: tutorial1_UCS_Test
      :link-type: doc

   .. grid-item-card:: UCS with Gmsh
      :img-top: ../_static/Desmos/UCS.png
      :link: tutorial2_UCS_with_Gmsh
      :link-type: doc

.. grid:: 2

   .. grid-item-card:: UCS Test with Quadrangle Elements
      :img-top: ../_static/Desmos/UCS.png
      :link: tutorial3_UCS_Test_with_Quadrangle_Elements
      :link-type: doc

   .. grid-item-card:: Brazilian Disc Test
      :img-top: ../_static/Desmos/BD_Test.png
      :link: tutorial4_BD_Test
      :link-type: doc

How to excavate a tunnel
-----------------------------------------
|

.. grid:: 2
   
   .. grid-item-card:: In-Situ Stress
      :img-top: ../_static/Desmos/Apply_Insitu_Stress.png
      :link: tutorial5_In_Situ_Stress
      :link-type: doc


Rocks fractured by water
-----------------------------------------
|

.. grid:: 2
   
   .. grid-item-card:: Hydro Seepage
      :img-top: ../_static/Desmos/Hydro.png
      :link: tutorial6_Hydro_Seepage
      :link-type: doc

   
   .. grid-item-card:: Hydro Fracture Flow
      :img-top: ../_static/Desmos/Hydro.png
      :link: tutorial7_Hydro_Fracture_Flow
      :link-type: doc



Thermal transportation in rock
-----------------------------------------
|

.. grid:: 2
   
   .. grid-item-card:: Thermal Flux
      :img-top: ../_static/Desmos/Thermal.png
      :link: tutorial8_Thermal_Flux
      :link-type: doc


Grain based model
-----------------------------------------
|

.. grid:: 2
   
   .. grid-item-card:: Grain Based Model
      :img-top: ../_static/Desmos/UCS.png
      :link: tutorial9_GBM
      :link-type: doc


Phase Field
-----------------------------------------
|

.. grid:: 2
   
   .. grid-item-card:: Phase Field
      :img-top: ../_static/Desmos/Phase_Field.png
      :link: tutorial10_Phase_Field
      :link-type: doc

.. raw:: html

   <script type="text/javascript" id="mapmyvisitors" src="//mapmyvisitors.com/map.js?d=FhQBKeKNkCLqgUfZdslz45dHXRuV_WDVgVzZVYmuX7s&cl=ffffff&w=a"></script>
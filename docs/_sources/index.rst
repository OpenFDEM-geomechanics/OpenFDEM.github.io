.. OpenFDEM_common documentation master file, created by
   sphinx-quickstart on Mon Oct 10 22:38:15 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. raw:: html

    <style> .red {color:#F64A8A; font-weight:bold;} </style>
    <style> .blue {color:#4169E1; font-weight:bold;} </style>

.. role:: red
.. role:: blue

OpenFDEM 
==================================================

*Open-Source Finite and Discrete Element Solver*

Copyright (©) 2017 - 2026 by Dr. Xiaofeng Li.


What is OpenFDEM
----------------

**OpenFDEM** is a free and open finite-discrete element simulation framework for
accurately and efficiently solving diverse **multiscale, multiphase, and
multiphysics** (3M) problems. Based on the **Finite-Discrete Element Method (FDEM)** , OpenFDEM integrates advanced
numerical methods, including the Material Point Method (MPM), Phase-Field Method
(PFM), and Finite Difference Method (FDM), to simulate complex problems involving
solid mechanics, fluid dynamics, heat transfer, and their coupled processes.
Developed in C++, OpenFDEM provides flexible modules for geometry, mesh, and
material management. It is widely applicable to fracture, fragmentation, impact,
fluid-solid interaction, and large-deformation problems.


Introduction to FDEM
--------------------

FDEM is a hybrid numerical method that combines the advantages of the Finite
Element Method (FEM) and the Discrete Element Method (DEM). Similar to FEM, FDEM
describes the deformation of continuous media through spatial discretization and
differential equations. Meanwhile, it incorporates DEM-based contact detection
and contact force calculation algorithms to simulate interactions between
separated bodies. Unlike conventional hybrid methods, discrete elements in FDEM
are generated naturally after the failure of continuous elements. Therefore, the
transition from a continuous state to a fractured and fully fragmented state
occurs automatically during the simulation process.

Benefiting from this unique capability, FDEM can realistically reproduce the
complete failure process of brittle materials, including elastic deformation,
crack initiation, crack propagation, fragmentation, and post-failure motion,
making it suitable for simulations of materials such as glass, rocks, ceramics,
and concrete.

.. raw:: html

   <div style="text-align:center;">
     <video autoplay loop muted playsinline style="max-width:45%;border-radius:4px;">
       <source src="_static/videos/hn_glass_real.mp4" type="video/mp4">
     </video>
     <p style="color:#555;font-style:italic;margin-top:4px;">Figure 1. Glass fragmentation in reality.</p>
   </div>

   <div style="text-align:center;">
     <video autoplay loop muted playsinline style="max-width:80%;border-radius:4px;">
       <source src="_static/videos/hn_glass_sim.mp4" type="video/mp4">
     </video>
     <p style="color:#555;font-style:italic;margin-top:4px;">Figure 2. Simulation of glass fragmentation (Left: continuous method; Middle: continuum damage method; Right: FDEM simulation).</p>
   </div>


Applications of OpenFDEM
------------------------

**1. Underground Excavation**

OpenFDEM can simulate excavation and blasting processes in underground
engineering, including stress wave propagation, crack growth, fragmentation, and
rock mass failure. By considering material heterogeneity and damage evolution,
OpenFDEM helps analyze excavation-induced damage and optimize engineering
designs.

.. raw:: html

   <div style="text-align:center;">
     <div style="display:flex;gap:2%;justify-content:center;flex-wrap:wrap;">
       <video autoplay loop muted playsinline style="width:32%;border-radius:4px;">
         <source src="_static/videos/hn_excav_static.mp4" type="video/mp4">
       </video>
       <video autoplay loop muted playsinline style="width:32%;border-radius:4px;">
         <source src="_static/videos/hn_excav_dynamic.mp4" type="video/mp4">
       </video>
       <video autoplay loop muted playsinline style="width:32%;border-radius:4px;">
         <source src="_static/videos/hn_excav_blast.mp4" type="video/mp4">
       </video>
     </div>
     <p style="color:#555;font-style:italic;margin-top:4px;">Figure 3. Tunnel excavation simulations (static / dynamic / drill-and-blast).</p>
   </div>

**2. Fluid-Solid Coupling**

OpenFDEM can simulate complex fluid-solid interaction problems, such as
seepage-induced failure, tunnel water inrush, and underground storage leakage.
By coupling solid deformation with fluid flow, it enables the analysis of
hydro-mechanical processes and related geological hazards.

.. raw:: html

   <div style="text-align:center;">
     <video autoplay loop muted playsinline style="max-width:70%;border-radius:4px;">
       <source src="_static/videos/hn_tapwater.mp4" type="video/mp4">
     </video>
     <p style="color:#555;font-style:italic;margin-top:4px;">Figure 4. Tap water flow into a tank.</p>
   </div>

**3. Granular Flow and Particle Dynamics**

OpenFDEM is suitable for simulating granular materials, including particle flow,
deposition, crushing, and rearrangement processes. The explicit treatment of
particle interactions makes it applicable to high-density granular systems and
particle-structure interaction problems.

.. raw:: html

   <div style="text-align:center;">
     <video autoplay loop muted playsinline style="max-width:70%;border-radius:4px;">
       <source src="_static/videos/hn_landslide.mp4" type="video/mp4">
     </video>
     <p style="color:#555;font-style:italic;margin-top:4px;">Figure 5. Landslide simulation.</p>
   </div>

**4. Impact and Dynamic Loading**

OpenFDEM can reproduce material responses under high-rate loading conditions,
including stress wave propagation, dynamic fracture, and fragment generation. It
is applicable to impact, blast, and penetration problems for analyzing failure
mechanisms of materials and structures.

.. raw:: html

   <div style="text-align:center;">
     <video autoplay loop muted playsinline style="max-width:70%;border-radius:4px;">
       <source src="_static/videos/hn_impact.mp4" type="video/mp4">
     </video>
     <p style="color:#555;font-style:italic;margin-top:4px;">Figure 6. Impact simulation.</p>
   </div>

**5. Large Deformation Problems**

OpenFDEM provides robust solutions for large-displacement and strongly nonlinear
problems involving severe deformation and contact evolution. It can be applied to
landslides, ground deformation, and soft soil settlement simulations.

.. raw:: html

   <div style="text-align:center;">
     <video autoplay loop muted playsinline style="max-width:70%;border-radius:4px;">
       <source src="_static/videos/hn_large_deform.mp4" type="video/mp4">
     </video>
     <p style="color:#555;font-style:italic;margin-top:4px;">Figure 7. Large deformation.</p>
   </div>

**6. Complex Contact Problems**

OpenFDEM is capable of handling complex contact interactions, including sliding,
separation, fracture, and interface debonding. It is suitable for studying rock
block movement, structural failure, and composite material interface damage.

.. raw:: html

   <div style="text-align:center;">
     <div style="display:flex;gap:2%;justify-content:center;align-items:center;flex-wrap:wrap;">
       <video autoplay loop muted playsinline style="width:53.7%;border-radius:4px;">
         <source src="_static/videos/hn_contact_interface.mp4" type="video/mp4">
       </video>
       <video autoplay loop muted playsinline style="width:42.3%;border-radius:4px;">
         <source src="_static/videos/hn_contact_update.mp4" type="video/mp4">
       </video>
     </div>
     <p style="color:#555;font-style:italic;margin-top:4px;">Figure 8. Complex interface contact simulation (left) and dynamic updating of contact lists (right).</p>
   </div>

..
   去掉过期call for papers
   Call for papers
   ----------------

   .. raw:: html

      <div style="height: 5px;"></div>

   .. image:: ../images/Introduction/special_issue.png
     :alt: special_issue png


   .. raw:: html

      <div style="height: 25px;"></div>

   We would like to invite you to submit a contribution to a featured journal issue on FDEM that will be published on **J. Rock Mech. Geotech.** (Impact Factor = 7.3, ranking 2/41 in Engineering and geological) in 2024.

   https://www.sciencedirect.com/journal/journal-of-rock-mechanics-and-geotechnical-engineering.

   The combined hybrid finite-discrete element method (FDEM) is widely used for modeling fracturing and fragmentation processes in brittle materials such as rock and concrete. The intrinsic advantage of FDEM derives by its ability to combine continuum mechanics formulations, such as finite strain-based deformability and non-linear fracture mechanics, with discrete element method, allowing the seamless transition from a continuum to a discontinuum model. FDEM allows to model multiple crack initiation, propagation and nucleation at micro scale to fractures or fragments at macro scale. These advances promote the applications of FDEM in geomechanics, energy storage, geothermal energy extraction, rock engineering, oil and gas exploration and mining. In recent decades, the FDEM has matured into a more general-purpose numerical method, covering mechanical, hydraulic, thermal and chemical coupling, that can be used to tackle increasingly more complex multiphase, multiphysics and multiscale problems.


   This **Special Issue** aims to highlight the new advances and future developments of combined finite-discrete element method or continuum-discontinuum method,
   for fracturing and fragmentation in geomechanics, underground energy storage, nuclear waste disposal, enhanced geothermal system, civil engineering or mining.
   All the papers on this special issue will be **open access and free**.


   The main topic includes but not limited to:
    - Multiscale, multiphase, and multiphysics modeling of fracture and fragmentation in rock mechanics and rock engineering
    - New advances and future developments of combined finite-discrete element method
    - High-Performance computing application and large-scale modelling in combined finite-discrete element method
    - Novel contact algorithms for high efficiency and accuracy
    - Hydraulic fracturing and fluid transportation modelling in energy storage or fractured reservoirs
    - THM© coupling in enhanced geothermal systems (EGS), underground hydrogen storage (UHS), nuclear waste disposal and CO₂ storage
    - Computational fluid dynamics and fluid-solid interaction for rock fracturing modelling
    - Artificial intelligence and machine learning technique in combined finite-discrete element method

   You are invited to submit your manuscript at any time before the submission deadline. For any inquiries about the appropriateness of contribution topics, please contact Dr. Xiaofeng Li via xiaofeng.li@utoronto.ca.

   Guest Editors
   ~~~~~~~~~~~~~

   Dr. Giovanni Grasselli
       | Department of Civil & Mineral Engineering
       | University of Toronto, Toronto, CA, Canada
       | Email: giovanni.grasselli@utoronto.ca

   Dr. Haibo Li
       | Institute of Rock and Soil Mechanics
       | Chinese Academy of Sciences, Wuhan, China
       | Email: hbli@whrsm.ac.cn

   Dr. Xiaofeng Li
       | Department of Civil & Mineral Engineering
       | University of Toronto, Toronto, CA, Canada
       | Email: xiaofeng.li@utoronto.ca

|
.. toctree::
   :maxdepth: 2
   :hidden:

   rst_about_introduction/index


.. toctree::
   :maxdepth: 2
   :hidden:

   rst_theory/index

.. toctree::
   :maxdepth: 2
   :hidden:

   rst_tutorials/index


.. toctree::
   :maxdepth: 2
   :hidden:

   rst_user_guide/index

.. toctree::
   :maxdepth: 2
   :hidden:

   rst_downloads

.. toctree::
   :maxdepth: 2
   :hidden:

   rst_about_us/index

.. toctree::
   :maxdepth: 2
   :hidden:

   rst_appendix/index

.. raw:: html

   <script type="text/javascript" id="mapmyvisitors" src="//mapmyvisitors.com/map.js?d=FhQBKeKNkCLqgUfZdslz45dHXRuV_WDVgVzZVYmuX7s&cl=ffffff&w=a"></script>



History
==========================================

The OpenFDEM project started from 2017 when I was a PhD candidate in Monash University, it has evolved from continuum-discontinuum method (CDM), also written in C++.  At that time, it only had matrix solving capabilities, 
while preprocessing required help from other commercial software, mesh data was only available from external codes, and the kernel itself could not perform meshing.

The very basic version was finished in 2020 after I graduated from Institute of Rock and Soil Mechanics, CAS. The post-processing working with Paraview is available and the Munjiza's No Binary Search (NBS) was introduced to this project to enhance the contact detection.
This update helps OpenFDEM get rid of the low efficiency resulting from direct search method. The potential conact model is also used to increase the reliability for the contact interaction, but how to calculate the potential within in a master or slave element
is slightly different from the method used in other FDEM codes. 

After that, I turned to a full-time developer and co-PI of this project in University of Toronto since 2021. The new blueprint aims for developing a new modern, efficient, standardized, and general-purpose FDEM-like software. 
We hope this new prject is not limited to specific element types (not just constant strain element), not limited to elastic materials (is suitable for a more general material type), not limited to a specific type of contact, 
and not limited to solving conventional mechanical problems. Although much advanced software has been developed by many FDEM research teams in recent years, much of the software is still developed using a process-oriented approach (C programming), 
relies on primitive Y-programs, or still focuses on the development of commercial and closed-source software.

Therefore, OpenFDEM hopes to make some progress in these areas and further develop a kind of open-source code, thus contributing to the development of FDEM.

.. figure:: ../../images/Introduction/timeline.svg
  :alt: timeline
  
  Timeline of the OpenFDEM project

The milestones of OpenFDEM project
-----------------------------------


**2017**

Start from continuum-discontinuum method, which relied on the cohesive method, contact interaction is not considered at that time, by Xiaofeng Li.
  

**2018** 

Rewrite the keneral in C++. The post-processing based on Paraview was available, by Xiaofeng Li.
  

**2020** 

Add contact class to this project, the NBS and potential contact model was added, by Xiaofeng Li.
  

**2021**

OpenFDEM rewrite with an finite element kernel and the pre-processing was considered.

**2022.06**

OpenFDEM 2D kernel is finished, the AMR module is available in OpenFDEM.
  

**2022.09**

OpenFDEM is boosted by OpenMP, 6-10 times faster.
  
**2022.12** 

Global FDEM workshop is held in Toronto, OpenFDEM start to  be noted by outside.
  
**2023.02** 

OpenFDEM 3D is inherited from 2D kernel, and most functionalities are available in 3D.

**2023.05**

Rewrite the frames and construct the basic classes to enhance the readability and efficiency for OpenFDEM. The computation speed 2.5X times increased after create the wheels for OpenFDEM.

**2023.08**

OpenFDEM website is online, and the binary code is available to public.
  

.. raw:: html

   <script src="//clustrmaps.com/globe.js?d=IJDdJTOZeBy5TaHUiVkIm7GLGSulnk0C2NzaC4-34QA">
   </script>
Tutorial A: Paraview
########################################
ParaView is an open source post-processing visualization engine users can use to visualize their model results. 
Users can go to `ParaView <https://www.paraview.org/download/>`_ to download their software. There is an `official 
PraView documentation <https://docs.paraview.org/en/latest/index.html>`_ online. This tutorial will just briefly 
introduce a few useful functions to view the results from OpenFDEM.

#. Go to the toolbar > File > Open... and choose the file path of the results and click OK. It will import all results under this category. You may also expand the group and select a single file.
    .. figure:: ../../images/ParaView/ParaView_import_Files.png
        :alt: Import Files to ParaView
        :align: center
        :scale: 60%

        Figure 1: Import Files to ParaView

#. Click Apply to show the data.
    .. figure:: ../../images/ParaView/Apply.png
        :alt: Apply the data to show
        :align: center
        :scale: 40%

        Figure 2: Apply the data to show

#. If the figure of the result is too small, choose reset to rescale the model.
    .. figure:: ../../images/ParaView/Reset.png
        :alt: Reset the view.
        :align: center
        :scale: 40%

        Figure 3: Reset the view

#. Select "runme_field_0.vtu" and change the result to "Stress"
    .. figure:: ../../images/ParaView/Stress.png
        :alt: Show the Stress
        :align: center
        :scale: 40%

        Figure 4: Show the Stress

#. To go to the next frame, users may use the arrow, select specific frame number, or enter the frame number. In this example, the last frame will be used.
    .. figure:: ../../images/ParaView/Frames.png
        :alt: Show a specific frame.
        :align: center
        :scale: 40%

        Figure 4: Show a specific frame

#. Select "Clamp and update every timestep" for Automatic Rescale Range Mode.
    .. figure:: ../../images/ParaView/Clamp_range.png
        :alt: Clamp the range.
        :align: center
        :scale: 40%

        Figure 5: Clamp the range

#. Go to the last step of the result. The sample is fractured under compression.
    .. figure:: ../../images/ParaView/Last_step.png
        :alt: Last step of the UCS test
        :align: center
        :scale: 40%

        Figure 6: Last step of the UCS test

#. If the result is not shown in the correct color scheme, click "Rescale to Visible Data Range".
    .. figure:: ../../images/ParaView/Rescale.png
        :alt: Rescale to the data range
        :align: center
        :scale: 40%

        Figure 7: Rescale to the data range

#. Select "runme_fracture_elements_0" and choose "Fracture Mode" with type of "Feature Edges" to show the cracking boundaries.
    .. figure:: ../../images/ParaView/Fracture_mode.png
        :alt: Fracture_mode
        :align: center
        :scale: 40%

        Figure 8: Fracture mode

#. To only show the sample without platens, users can select the "runme_field_0.vtu" file and use threshold filter in filters.
    .. figure:: ../../images/ParaView/Filters.png
        :alt: Filters
        :align: center
        :scale: 40%

        Figure 9: Filters

#. To filter the sample out, choose "ele_group_rock" with condition of above upper thresold 1 and apply.
    .. figure:: ../../images/ParaView/Threshold.png
        :alt: Threshold
        :align: center
        :scale: 40%

        Figure 10: Threshold

#. You may show results with the rock sample only now.
    .. figure:: ../../images/ParaView/Result.png
        :alt: Result
        :align: center
        :scale: 40%

        Figure 11: Result


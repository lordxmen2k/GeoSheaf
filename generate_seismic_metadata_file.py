import json

# The input dictionary (correcting single quotes and keys)
seismic_metadata = {
    "1_Original_Seismics.cbvs": {},
    "2_Steering_BG_Detailed.cbvs": {"Data storage": "3 - 16 bit signed", "Type": "Steering"},
    "3_Steering_BG_Background.cbvs": {"Data storage": "3 - 16 bit signed", "Type": "Steering"},
    "3a_Steering_PCA111_MF225.cbvs": {"Created At": "Mon 10 Aug 2020, 13:28:22", "Created By": "cases`assia",
                                      "Data storage": "3 - 16 bit signed", "Type": "Steering"},
    "3b_Steering_FFT225_MF113.cbvs": {"Created At": "Tue 25 Aug 2015, 16:39:50", "Created By": "cases`testing",
                                      "Data storage": "3 - 16 bit signed", "Type": "Steering"},
    "4_Dip_steered_median_filter.cbvs": {"Data storage": "3 - 16 bit signed", "Type": "Attribute"},
    "5_ChimneyCube.cbvs": {"Data storage": "3 - 16 bit signed", "Type": "Attribute"},
    "6_Wheeler-stratal-slicing.cbvs": {"Data storage": "3 - 16 bit signed", "ZDomain": "Wheeler"},
    "7a_AI_Cube_Std.cbvs": {},
    "7b_AI_Cube_from_HorizonCube.cbvs": {"Data storage": "0 - auto"},
    "8a_PorosityCube_from_HC-NN.cbvs": {"Data storage": "0 - auto", "Type": "Attribute"},
    "8b_Gamma_from_HorizonCube.cbvs": {"Data storage": "0 - auto"},
    "9-1_Similarity_on_FEF_seismic.cbvs": {"Data storage": "0 - auto", "Type": "Attribute"},
    "9-2_Dip-steered_diffusion_filter.cbvs": {"Data storage": "3 - 16 bit signed", "Type": "Attribute"},
    "9-3_Fault_enhancement_filter.cbvs": {"Data storage": "3 - 16 bit signed", "Type": "Attribute"},
    "9_Similarity_on_Original_seismic.cbvs": {"Data storage": "0 - auto", "Type": "Attribute"},
    "BLI_RhoB.cbvs": {"Created At": "Mon 23 Mar 2020, 13:27:39", "Created By": "demo",
                      "Created From": "H:\\surveys\\F3_Demo_2020_training_v7\\temp_HJ\\RHOB_BLI.cbvs"},
    "BLI_Vp.cbvs": {"Created At": "Mon 23 Mar 2020, 13:00:33", "Created By": "demo",
                    "Created From": "H:\\surveys\\F3_Demo_2020_training_v7\\temp_HJ\\VP_BLI.cbvs"},
    "BLI_Vs.cbvs": {"Created At": "Mon 23 Mar 2020, 13:26:04", "Created By": "demo",
                    "Created From": "H:\\surveys\\F3_Demo_2020_training_v7\\temp_HJ\\VS_BLI.cbvs"},
    "BLI_seismic_18deg.cbvs": {"Created At": "Fri 20 Mar 2020, 14:13:16", "Created By": "demo",
                               "Created From": "H:\\surveys\\F3_Demo_2020_training_v7\\temp_HJ\\seismic_18deg.cbvs"},
    "BLI_seismic_28deg.cbvs": {"Created At": "Fri 20 Mar 2020, 14:39:42", "Created By": "demo",
                               "Created From": "H:\\surveys\\F3_Demo_2020_training_v7\\temp_HJ\\seismic_28deg.cbvs"},
    "BLI_seismic_8deg.cbvs": {"Created At": "Fri 20 Mar 2020, 13:12:41", "Created By": "demo",
                              "Created From": "H:\\surveys\\F3_Demo_2020_training_v7\\temp_HJ\\seismic_8deg.cbvs"},
    "BLI_trend_RHO.cbvs": {"Created At": "Sat 21 Mar 2020, 15:14:03", "Created By": "demo",
                           "Created From": "H:\\surveys\\F3_Demo_2020_training_v7\\temp_HJ\\trend_RHO.cbvs"},
    "BLI_trend_VP.cbvs": {"Created At": "Fri 20 Mar 2020, 15:54:06", "Created By": "demo",
                          "Created From": "H:\\surveys\\F3_Demo_2020_training_v7\\temp_HJ\\trend_VP.cbvs"},
    "BLI_trend_VS.cbvs": {"Created At": "Fri 20 Mar 2020, 17:21:57", "Created By": "demo",
                          "Created From": "H:\\surveys\\F3_Demo_2020_training_v7\\temp_HJ\\trend_VS.cbvs"},
    "BLI_wavelet_18degree.wvlt": {},
    "BLI_wavelet_28degree.wvlt": {},
    "BLI_wavelet_8degree.wvlt": {},
    "Fault_Likelihood_Thinned_from_DSMF_seis.cbvs": {"Created At": "Wed 09 Sep 2015, 14:25:42", "Created By": "cases`farrukh15",
                                                     "Data storage": "0 - auto"},
    "Ricker_20Hz.wvlt": {"User": "cases`arnaud6"},
    "Ricker_30Hz.wvlt": {"User": "cases`arnaud6"},
    "Ricker_40Hz.wvlt": {"User": "cases`arnaud6"},
    "Ricker_50Hz.wvlt": {"User": "cases`arnaud6"},
    "Seis": {"Created At": "wo 26 mrt 2014, 11:26:35", "Created By": "demo"},
    "Seismics": {"Data storage": "3 - 16 bit signed"},
    "Steering_2D": {"Created At": "Wed 09 Sep 2015, 19:36:17", "Created By": "cases`hardeep", "Type": "Steering"},
    "Velocity_model__INT_.cbvs": {"Bottom Vavg": "1350`4500", "Data storage": "0 - auto", "Is Velocity": "Yes",
                                  "Top Vavg": "1350`4500", "Type": "Attribute", "Velocity Type": "Vint"},
    "Velocity_model__RMS_.cbvs": {"Data storage": "0 - auto", "Is Velocity": "Yes", "Statics Horizon": "",
                                  "Type": "Attribute", "Velocity Type": "Vrms"},
    "stat_120.wvlt": {"Scaled": "100010.70`100020.3`100010.4`FS8"},
    "stat_120_raw.wvlt": {}
}

# Save the corrected JSON file
json_file_path = "seismic_metadata_fixed.json"

with open(json_file_path, "w", encoding="utf-8") as json_file:
    json.dump(seismic_metadata, json_file, indent=4)

json_file_path

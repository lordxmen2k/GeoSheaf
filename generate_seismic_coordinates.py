import numpy as np
import pandas as pd
from obspy.io.segy.segy import _read_segy

# Load the SEG-Y file
segy_file_path = "F3_Demo_2020/rawdata/seismic_data.sgy"
seismic_data = _read_segy(segy_file_path)

# Generate synthetic coordinates based on trace index
trace_count = len(seismic_data.traces)
longitude = np.linspace(-100, -90, trace_count)  # Example: Spread longitudes between -100 and -90
latitude = np.linspace(30, 40, trace_count)  # Example: Spread latitudes between 30 and 40

# Create DataFrame with synthetic coordinates
seismic_coords_df = pd.DataFrame({"longitude": longitude, "latitude": latitude})

# Save to CSV
seismic_coords_file = "seismic_coordinates.csv"
seismic_coords_df.to_csv(seismic_coords_file, index=False)

seismic_coords_file

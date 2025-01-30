import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from obspy.io.segy.segy import _read_segy

### --- STEP 1: LOAD SEISMIC DATA FROM SEG-Y --- ###
print("Loading seismic data from SEG-Y...")

# Define file paths
segy_file_path = "F3_Demo_2020/rawdata/seismic_data.sgy"
seismic_coords_file = "seismic_coordinates.csv"
well_data_file = "wwc5_wells/wwc5_wells.txt"

# Load seismic coordinates
seismic_coords_df = pd.read_csv(seismic_coords_file)

# Remove duplicate seismic coordinates
seismic_coords_df = seismic_coords_df.drop_duplicates(subset=["longitude", "latitude"])

# Load SEG-Y data
seismic_data = _read_segy(segy_file_path)
seismic_amplitudes = np.array([trace.data for trace in seismic_data.traces[:len(seismic_coords_df)]])

# Add seismic amplitudes to coordinates dataframe
seismic_coords_df["seismic_amplitude"] = seismic_amplitudes[:, 0]  # Use first sample per trace

# Save updated seismic data with amplitudes
seismic_data_file = "seismic_data_with_amplitudes.csv"
seismic_coords_df.to_csv(seismic_data_file, index=False)
print("✅ Seismic data with amplitudes saved.")

### --- STEP 2: LOAD WELL LOG DATA --- ###
print("Loading well log data...")

# Load well data
well_data = pd.read_csv(well_data_file, delimiter=",", encoding="utf-8")

# Rename key columns if needed
well_data.rename(columns={"LONGITUDE": "longitude", "LATITUDE": "latitude"}, inplace=True)

print("✅ Well data loaded successfully.")

### --- STEP 3: VERIFY WELL LOCATIONS WITHIN SEISMIC GRID --- ###
print("Verifying well locations within seismic grid...")

# Filter wells that fall within seismic grid
well_data = well_data[
    (well_data["longitude"] >= seismic_coords_df["longitude"].min()) &
    (well_data["longitude"] <= seismic_coords_df["longitude"].max()) &
    (well_data["latitude"] >= seismic_coords_df["latitude"].min()) &
    (well_data["latitude"] <= seismic_coords_df["latitude"].max())
]

# Save filtered wells data
filtered_well_data_file = "filtered_well_data.csv"
well_data.to_csv(filtered_well_data_file, index=False)
print(f"✅ Filtered well data saved. Remaining wells: {len(well_data)}")

### --- STEP 4: INTERPOLATE SEISMIC DATA TO WELL LOCATIONS --- ###
print("Interpolating seismic values to well locations...")

# Use 'nearest' method instead of 'linear' to avoid QhullError
well_data["seismic_value"] = griddata(
    (seismic_coords_df["longitude"], seismic_coords_df["latitude"]),
    seismic_coords_df["seismic_amplitude"],
    (well_data["longitude"], well_data["latitude"]),
    method="nearest"  # Changed from "linear" to "nearest"
)

# Save interpolated well data
interpolated_well_data_file = "well_data_with_seismic.csv"
well_data.to_csv(interpolated_well_data_file, index=False)
print("✅ Interpolated seismic data saved.")

### --- STEP 5: BUILD SHEAF-THEORETIC GRAPH MODEL --- ###
print("Building sheaf-theoretic graph model...")

# Create an empty graph
G = nx.Graph()

# Add well data as nodes
for idx, row in well_data.iterrows():
    G.add_node(row["WELL_ID"], type="well", value=row["seismic_value"])

# Add seismic data as nodes
for idx, row in seismic_coords_df.iterrows():
    G.add_node(f"seismic_{idx}", type="seismic", value=row["seismic_amplitude"])

# Add edges enforcing sheaf constraints
for idx, row in well_data.iterrows():
    if f"seismic_{idx}" in G.nodes:
        G.add_edge(row["WELL_ID"], f"seismic_{idx}", weight=1)

print("✅ Graph model built successfully!")

### --- STEP 6: VISUALIZE THE GRAPH --- ###
print("Visualizing the graph...")

plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G)
labels = {node: f"{node}\n{round(G.nodes[node]['value'], 3)}" for node in G.nodes}

nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=500, font_size=8)
nx.draw_networkx_labels(G, pos, labels=labels, font_size=8, font_color="black")

plt.title("Sheaf-Theoretic Graph of Seismic & Well Data")
plt.show()

print("✅ Process completed successfully! 🚀")

# Return paths to generated files
(seismic_data_file, filtered_well_data_file, interpolated_well_data_file)
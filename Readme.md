# **GeoSheaf: A Sheaf-Theoretic Framework for Seismic-Well Integration**

## **Overview**
GeoSheaf is an advanced mathematical framework that integrates seismic reflection amplitudes and well log data using **sheaf theory** and **graph-based models**. This repository provides a novel approach to **reservoir characterization**, ensuring consistent, high-fidelity integration of multi-source geophysical data.

## **🔬 Research Goals**
- **Apply sheaf theory** to unify seismic and well log datasets in a mathematically rigorous way.
- **Improve seismic-well data integration** using graph Laplacian-based sheaf cohomology solvers.
- **Enhance subsurface modeling** by enforcing geophysical constraints with algebraic topology.

## **📂 Dataset Sources**
This repository utilizes publicly available datasets from major geological and geophysical repositories:

### **1️⃣ Integrate Real Seismic Data**
- **Dataset:** Netherlands Offshore F3 3D Seismic (F3 Demo 2020)
- **Source:** SEG Open Data Repository
- **Download Link:** [F3 Demo 2020](https://terranubis.com/datainfo/F3-Demo-2020)
- **Create Folder Inside Project:** F3_Demo_2020
- **Processing Steps:**
  - Extract SEG-Y seismic reflection amplitudes.
  - Convert reflection amplitudes into sheaf node values.
  - Normalize and align spatial coordinates for well integration.

### **2️⃣ Incorporate Well Log Data**
- **Dataset:** Kansas Geological Survey Well Logs (WWC5 Wells)
- **Source:** Kansas Geological Survey (KGS)
- **Download Link:** [WWC5 Wells](https://www.kgs.ku.edu/Magellan/WaterWell/index.html)
- **Create Folder Inside Project:** wwc5_wells
- **Processing Steps:**
  - Extract porosity, permeability, and lithology data.
  - Use these attributes as observed data values in well log nodes.
  - Align well locations with seismic traces using geospatial constraints.

### **3️⃣ Implement a More Advanced Sheaf Constraint Solver**
- **Mathematical Model:**
  - Traditional methods use simple **least-squares fitting**.
  - This repository leverages **graph Laplacian-based sheaf cohomology solvers** for error correction.
  - This approach ensures **robust data fusion** and minimizes inconsistencies between seismic and well logs.

## **⚙️ Installation & Dependencies**
To run this framework, install the required dependencies:

```bash
pip install numpy pandas scipy matplotlib networkx obspy
```

## **🚀 Running the Framework**
1. Download and extract the seismic and well log datasets.
2. Process SEG-Y files to extract reflection amplitudes.
3. Process well log data to extract key reservoir attributes.
4. Construct a sheaf-theoretic graph model.
5. Solve sheaf constraints using a Laplacian-based approach.
6. Visualize the integrated model.

Run the full pipeline with:
```bash
python seismic_well_simulation.py
```

## **📊 Visualization & Interpretation**
- The final **sheaf graph** shows **consistent integration** of seismic and well log data.
- Advanced **error correction techniques** ensure reliability in reservoir modeling.
- The framework is extendable to incorporate **machine learning-based constraint solvers**.

## **📜 License & Citation**
This project is open-source under the **MIT License**. If you use this framework in your research, please cite:

```
@article{GeoSheaf2024,
  author = {Gerald Enrique Nelson Mc Kenzie},
  title = {GeoSheaf: A Sheaf-Theoretic Framework for Seismic-Well Integration},
  journal = {Zenodo},
  year = {2024},
  doi = {10.5281/zenodo.14774480},
  url = {https://github.com/lordxmen2k/GeoSheaf}
}
```

## **🤝 Contributions & Future Work**
Contributions are welcome! Future work includes:
- Integrating **machine learning** for constraint solving.
- Extending the framework for **real-time reservoir monitoring**.
- Incorporating **3D visualization** tools for enhanced interpretation.

For questions, please contact: **lordxmen2k@gmail.com** 🚀
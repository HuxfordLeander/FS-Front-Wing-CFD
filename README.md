# FS Front Wing CFD

Independent CFD project investigating NACA 0012 aerodynamics and a simplified Formula Student front wing.

## Current Progress

- Parametric NACA 0012 geometry generation in Python
- Geometry validation against reference data
- STL generation for CFD meshing
- Thin-3D quasi-2D background mesh using `blockMesh`
- Surface refinement and snapping using `snappyHexMesh`
- Mesh-quality verification using `checkMesh`

## Current Mesh

- Approximately 181,880 cells
- Thin-span 3D computational domain
- Spanwise symmetry-plane boundary conditions
- Final mesh passed `checkMesh`

## Planned Work

- Boundary-condition setup
- Turbulence-model selection and setup
- Baseline `simpleFoam` simulation
- Mesh-independence study
- Ground-effect investigation
- 3D front-wing and endplate study
- Python post-processing and automated comparison of aerodynamic coefficients

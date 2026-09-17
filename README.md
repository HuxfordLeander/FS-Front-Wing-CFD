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

## Baseline CFD Simulation

A baseline steady-state CFD simulation was performed for a NACA0012 airfoil using OpenFOAM `simpleFoam` with the Spalart–Allmaras RANS turbulence model.

### Simulation Conditions

| Parameter | Value |
|---|---:|
| Airfoil | NACA0012 |
| Chord length | 0.20 m |
| Freestream velocity | 20 m/s |
| Angle of attack | 0° |
| Kinematic viscosity | 1.5 × 10⁻⁵ m²/s |
| Reynolds number | 2.67 × 10⁵ |
| Mesh size | 181,880 cells |

### Mesh Quality

The final mesh passed `checkMesh` successfully.

| Mesh metric | Value |
|---|---:|
| Maximum non-orthogonality | 62.64° |
| Average non-orthogonality | 3.60° |
| Maximum skewness | 2.98 |
| Maximum aspect ratio | 16.02 |

### Solver and Turbulence Model

- Solver: `simpleFoam`
- Flow assumption: steady-state, incompressible
- Turbulence modelling: RANS
- Turbulence model: Spalart–Allmaras
- Pressure–velocity coupling: SIMPLE

### Convergence

The baseline solution converged after **566 SIMPLE iterations**.

Runtime on an Apple M4 MacBook Pro using OpenFOAM in Docker was approximately **235 seconds**.

### Aerodynamic Results

| Coefficient | Result |
|---|---:|
| Lift coefficient, CL | 0.00185 |
| Drag coefficient, CD | 0.01673 |
| Pitching moment coefficient, Cm | -0.000929 |

The near-zero lift coefficient is consistent with the expected symmetric behaviour of a NACA0012 airfoil at 0° angle of attack.

The drag coefficient consisted of approximately:

- Pressure contribution: 0.01140
- Viscous contribution: 0.00533

### Current Project Status

Completed:

- Parametric NACA0012 geometry generation
- STL preparation
- OpenFOAM meshing
- Mesh quality verification
- Boundary-condition setup
- Spalart–Allmaras turbulence-model setup
- Baseline steady-state CFD solution
- Lift, drag and pitching-moment coefficient extraction

Next steps:

- y+ assessment
- Pressure and velocity-field visualisation in ParaView
- Mesh-independence study
- Ground-clearance investigation
- 3D front-wing modelling
- Endplate geometry study
- Python post-processing and comparison plots

> The baseline solution has converged numerically. Mesh independence and further validation are still required before the aerodynamic results are treated as validated CFD data.


### Near-Wall Resolution

The converged baseline case produced the following airfoil-surface y+ values:

| y+ metric | Value |
|---|---:|
| Minimum | ~15.0 |
| Maximum | ~195.9 |
| Average | ~63.9 |

The current mesh therefore provides a preliminary wall-function-based solution rather than a fully wall-resolved boundary-layer simulation.

The wide y+ range indicates that improved near-wall meshing and prism-layer refinement should be investigated before drawing final aerodynamic conclusions, particularly for drag prediction.

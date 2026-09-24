import shutil
from pathlib import Path

template_dir = Path("/Users/huxford/Desktop/FS_frontwing_project/03_mesh_independence/layered_case_v2")

chord=0.20
airfoil_y_min=-0.0120033

cases={"h025":0.25,"h050":0.50,"h075":0.75,"h100":1.00,"h150":1.50}
project_dir=Path("/Users/huxford/Desktop/FS_frontwing_project")
ground_dir = project_dir / "04_ground_effect" / "generated_multiblock_test"

for name,h_over_c in cases.items():
    height=h_over_c*chord
    ground_y=airfoil_y_min-height
    target_dy=0.02
    interface_y=-0.04
    upper_ny=52
    lower_height=interface_y-ground_y
    lower_ny=round(lower_height/target_dy)
    lower_actual_dy=lower_height/lower_ny

    case_dir=ground_dir/name
    case_dir.mkdir(parents=True,exist_ok=True)

    shutil.copytree(template_dir/"0",case_dir/"0",dirs_exist_ok=True)
    shutil.copytree(template_dir/"system",case_dir/"system",dirs_exist_ok=True)

    (case_dir/"constant").mkdir(parents=True,exist_ok=True)

    shutil.copytree(template_dir/"constant"/"triSurface",case_dir/"constant"/"triSurface",dirs_exist_ok=True)
    shutil.copy2(template_dir/"constant"/"transportProperties",case_dir/"constant"/"transportProperties")
    shutil.copy2(template_dir/"constant"/"turbulenceProperties",case_dir/"constant"/"turbulenceProperties")

    blockmesh_file=case_dir/"system"/"blockMeshDict"
    blockmesh_text = f"""FoamFile
{{
    format      ascii;
    class       dictionary;
    object      blockMeshDict;
}}

convertToMeters 1;

vertices
(
    (-1.0 {ground_y:.7f} -0.01)
    ( 2.2 {ground_y:.7f} -0.01)
    ( 2.2 {interface_y:.7f} -0.01)
    (-1.0 {interface_y:.7f} -0.01)

    (-1.0 {ground_y:.7f}  0.01)
    ( 2.2 {ground_y:.7f}  0.01)
    ( 2.2 {interface_y:.7f}  0.01)
    (-1.0 {interface_y:.7f}  0.01)

    ( 2.2 1.0000000 -0.01)
    (-1.0 1.0000000 -0.01)
    ( 2.2 1.0000000  0.01)
    (-1.0 1.0000000  0.01)
);

blocks
(
    hex (0 1 2 3 4 5 6 7) (160 {lower_ny} 10) simpleGrading (1 1 1)
    hex (3 2 8 9 7 6 10 11) (160 {upper_ny} 10) simpleGrading (1 1 1)
);

boundary
(
    inlet
    {{
        type patch;
        faces
        (
            (0 4 7 3)
            (3 7 11 9)
        );
    }}

    outlet
    {{
        type patch;
        faces
        (
            (1 2 6 5)
            (2 8 10 6)
        );
    }}

    top
    {{
        type patch;
        faces
        (
            (9 11 10 8)
        );
    }}

    bottom
    {{
        type wall;
        faces
        (
            (0 1 5 4)
        );
    }}

    front
    {{
        type symmetryPlane;
        faces
        (
            (0 3 2 1)
            (3 9 8 2)
        );
    }}

    back
    {{
        type symmetryPlane;
        faces
        (
            (4 5 6 7)
            (7 6 10 11)
        );
    }}
);
"""

    blockmesh_file.write_text(blockmesh_text)
    snappy_file=case_dir / "system" / "snappyHexMeshDict"
    snappy_text=snappy_file.read_text()

    old_layer = "firstLayerThickness 0.0005;"

    if old_layer not in snappy_text:
        raise ValueError(
            f"Could not find {old_layer} in {snappy_file}"
        )

    snappy_text = snappy_text.replace(
        old_layer,
        "firstLayerThickness 0.00020;"
    )

    snappy_file.write_text(snappy_text)

    print(f"Created {case_dir}")
    print(f'ground_y={ground_y: .6f}m')
    print(f"lower_ny={lower_ny}")
    print(f"upper_ny={upper_ny}")
    print(f"lower_actual_dy={lower_actual_dy:.6f} m")
    
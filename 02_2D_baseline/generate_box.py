c=0.20
left=-1.0
right=2.2
top=1.0
bottom=-1.0

z_front=-0.01
z_back=0.01

p0=(left,bottom,z_front)
p1=(right,bottom,z_front)
p2=(right, top,z_front)
p3=(left, top,z_front)

p4=(left,bottom,z_back)
p5=(right,bottom,z_back)
p6=(right, top,z_back)
p7=(left, top,z_back)

def foam_point(p):
    return f"({p[0]} {p[1]} {p[2]})"
print(foam_point(p0))
print(foam_point(p1))
print(foam_point(p2))
print(foam_point(p3))
print(foam_point(p4))
print(foam_point(p5))
print(foam_point(p6))
print(foam_point(p7))

with open(
    "/Users/huxford/Desktop/FS_frontwing_project/02_2D_baseline/blockMeshDict",
    "w"
) as f:

    f.write(
f"""
FoamFile
{{
    format      ascii;
    class       dictionary;
    object      blockMeshDict;
}}

convertToMeters 1;

vertices
(
    {foam_point(p0)}
    {foam_point(p1)}
    {foam_point(p2)}
    {foam_point(p3)}
    {foam_point(p4)}
    {foam_point(p5)}
    {foam_point(p6)}
    {foam_point(p7)}
);
blocks
(
    hex (0 1 2 3 4 5 6 7) (160 100 10) simpleGrading (1 1 1)
);
boundary
(
    inlet
    {{
        type patch;
        faces
        (
            (0 4 7 3)
        );
    }}
    outlet
    {{
        type patch;
        faces
        (
            (1 2 6 5)
        );
    }}
    topandbottom
    {{
        type patch;
        faces
        (
            (3 7 6 2)
            (0 1 5 4)
        );
    }}
        front
        {{
            type symmetryPlane;
            faces
            (
                (0 3 2 1)
            );
        }}
   back
   {{type symmetryPlane;
    faces
    (
        (4 5 6 7)
    );
}}
);
"""
     )
    
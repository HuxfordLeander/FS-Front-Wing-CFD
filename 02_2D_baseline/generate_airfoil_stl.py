import numpy as np

airfoil=np.loadtxt(
    "/Users/huxford/Desktop/FS_frontwing_project/01_geometry/naca0012_generated.txt")

x=airfoil[:, 0]
y=airfoil[:, 1]

print(x[:5])
print(y[:5])

z_front=-0.011
z_back=0.011
front_points=np.column_stack((x, y, np.full_like(x, z_front)))
back_points=np.column_stack((x, y, np.full_like(x, z_back)))
triangles=[]
for i in range(len(front_points)-1):
 triangle1=(front_points[i], front_points[i+1], back_points[i+1])
 triangle2=(front_points[i], back_points[i+1], back_points[i])
 triangles.append(triangle1)
 triangles.append(triangle2)
triangle1 = (front_points[-1],front_points[0],back_points[0])

triangle2 = (front_points[-1],back_points[0],back_points[-1])

triangles.append(triangle1)
triangles.append(triangle2)
print(len(triangles))
print(triangles[0])
front_center=np.array([0.1, 0.0, z_front])
back_center=np.array([0.1, 0.0, z_back])
print(front_center)
print(back_center)
for i in range(len(front_points)-1):
 front_triangle=(front_center,front_points[i+1],front_points[i])
 triangles.append(front_triangle)
front_triangle=(front_center,front_points[0],front_points[-1])
triangles.append(front_triangle)
print(len(triangles))
for i in range(len(back_points)-1):
    back_triangle=(back_center,back_points[i],back_points[i+1])
    triangles.append(back_triangle)
back_triangle=(back_center,back_points[-1],back_points[0])
triangles.append(back_triangle)
print(len(triangles))

stl_path = "/Users/huxford/Desktop/FS_frontwing_project/02_2D_baseline/naca0012.stl"

with open(stl_path, "w") as f:
    f.write("solid naca0012\n")

    for triangle in triangles:
        p1, p2, p3 = triangle

        f.write("  facet normal 0 0 0\n")
        f.write("    outer loop\n")

        f.write(f"      vertex {p1[0]} {p1[1]} {p1[2]}\n")
        f.write(f"      vertex {p2[0]} {p2[1]} {p2[2]}\n")
        f.write(f"      vertex {p3[0]} {p3[1]} {p3[2]}\n")

        f.write("    endloop\n")
        f.write("  endfacet\n")

    f.write("endsolid naca0012\n")
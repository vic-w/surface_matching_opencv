import open3d as o3d
import numpy as np

def showResults(scenePath, modelPath, pose):
    mesh = o3d.io.read_triangle_mesh(modelPath)
    mesh.transform(pose)
    scenePc = o3d.io.read_point_cloud(scenePath)

    o3d.visualization.draw_geometries([scenePc, mesh])
    

if __name__=='__main__':
    modelPath = 'parasaurolophus_6700.ply'
    scenePath = 'rs1_normals.ply'
    pose = [[0.9950469121388202, -0.07934151931800362, 0.05988794499153427, -74.13557928411987],
            [0.09419411370259408, 0.5600339904489541, -0.8230974416711565, -602.2765800301789],
            [0.03176651675555509, 0.8246616596241945, 0.56473359698099, -293.2440945892855],
            [0, 0, 0, 1]]
    showResults(scenePath, modelPath, pose)

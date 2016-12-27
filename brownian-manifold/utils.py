"""
A few helper functions for brownian-manifold
"""

import numpy as np


def vector_cross(v,w):
    """
    helper to compute the cross product
    of two vectors.

    Parameters
    ----------
    v: array
    w: float, threshold parameter

    Returns
    -------
    v_cross_w: array, the resulting cross product of
               v and w (v X w)

    """
    v_cross_w = np.array([v[1]*w[2] - v[2]*w[1],
                          v[2]*w[0] - v[0]*w[2],
                          v[0]*w[1] - v[1]*w[0]])
    return v_cross_w


    
def arctan2(y,x):
    """
    helper to compute
    the azimuth angle when converting from Cartesian coordinates
    to other coordinate systems


    Given an array of two coordinates (y,x) representing
    points on a plane, this function computes angles (in radians)
    mapped to range [0,2*pi)



    Parameters
    ----------
    y: array
    
    x: array

    Returns
    -------
    theta: array, the resulting angle:
                  arctan(y/x) --inverse tangent
                  mapped to range [0,2*pi)
    """

    
    theta = np.asarray(np.arctan2(y,x))
    for i in range(theta.size-1):
        if theta[i] < 0:
            theta[i]+=2*np.pi
    return theta


    
    
def surface_sphere(radius):
    """
    
    """
    phi, theta = np.mgrid[0.0:np.pi:100j, 0.0:2.0*np.pi:100j]
    x_blank_sphere = radius*np.sin(phi)*np.cos(theta)
    y_blank_sphere = radius*np.sin(phi)*np.sin(theta)
    z_blank_sphere = radius*np.cos(phi)
    sphere_surface = np.array(([x_blank_sphere,
                                y_blank_sphere,
                                z_blank_sphere]))
    return sphere_surface
    
    
    
def surface_cylinder(radius, height):
    """
    
    """
    
    
    
    p0 = np.array([0, 0, height]) #point at one end
    p1 = np.array([0, 0, -height]) #point at other end
    #vector in direction of axis
    v = p1 - p0
    #find magnitude of vector
    mag = np.linalg.norm(v)
    #unit vector in direction of axis
    v = v / mag
    #make some vector not in the same direction as v
    not_v = np.array([1, 0, 0])
    if (v == not_v).all():
        not_v = np.array([0, 1, 0])
    #make vector perpendicular to v
    n1 = np.cross(v, not_v)
    #normalize n1
    n1 /= np.linalg.norm(n1)
    #make unit vector perpendicular to v and n1
    n2 = np.cross(v, n1)
    #surface ranges over t from 0 to length of axis and 0 to 2*pi
    t = np.linspace(0, mag, 2)
    theta = np.linspace(0, 2 * np.pi, 100)
    rsample = np.linspace(0, radius, 2)
    #use meshgrid to make 2d arrays
    t, theta2 = np.meshgrid(t, theta)
    rsample,theta = np.meshgrid(rsample, theta)
    # "Finite Cylinder" surface
    x_blank_cylinder, y_blank_cylinder, z_blank_cylinder = \
                                                [p0[i] + v[i] * t + radius * 
                                                np.sin(theta2) * n1[i]+radius* 
                                                np.cos(theta2)*
                                                n2[i] for i in [0, 1, 2]] 
    cylinder_surface = np.array(([x_blank_cylinder,
                                  y_blank_cylinder,
                                  z_blank_cylinder]))
    return cylinder_surface
    
    


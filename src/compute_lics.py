import math
from utils import *

def compute_lics(NUMPOINTS, POINTS, PARAMETERS):
    """
    Compute the Conditions Met Vector (CMV) for the given points and parameters.

    Args:
        NUMPOINTS (int): Number of planar data points.
        POINTS (list): List of tuples [(x1, y1), (x2, y2), ...].
        PARAMETERS (dict): Parameters for the LICs.

    Returns:
        list: CMV (Conditions Met Vector).
    """
    CMV = [False] * 15  # Placeholder for 15 LIC conditions

    # Placeholder: Implement logic for each LIC (0-14)
    # Example:
    # CMV[0] = lic_0(NUMPOINTS, POINTS, PARAMETERS)
    CMV[5] = lic_5(NUMPOINTS, POINTS)
    CMV[6] = lic_6(NUMPOINTS, POINTS, PARAMETERS['N_PTS'], PARAMETERS['DIST'])
    CMV[7] = lic_7(NUMPOINTS, POINTS, PARAMETERS['K_PTS'], PARAMETERS['LENGTH1'])
    CMV[8] = lic_8(NUMPOINTS, POINTS, PARAMETERS['A_PTS'], 
                   PARAMETERS['B_PTS'], PARAMETERS['RADIUS1'])
    CMV[9] = lic_9(NUMPOINTS, POINTS, PARAMETERS['C_PTS'], 
                   PARAMETERS['D_PTS'], PARAMETERS['EPSILON'])

    return CMV

# Placeholder functions for individual LIC computations
def lic_0(NUMPOINTS, POINTS, PARAMETERS):
    """
    LIC 0: Check if there exists at least one set of two consecutive data points
    that are a distance greater than LENGTH1 apart.
    """
    if NUMPOINTS < 2:
        return False
    
    for i in range(NUMPOINTS-1):
        dist = distance(POINTS[i],POINTS[i+1])

        if dist > PARAMETERS['LENGTH1']:
            return True
        
    return False

def lic_1(NUMPOINTS, POINTS, PARAMETERS):
    """
    LIC 1: Check if three consecutive data points cannot all be contained within
    or on a circle of radius RADIUS1.
    """
    if NUMPOINTS < 3:
        return False
    
    for i in range(NUMPOINTS-2):
        if (max(distance(POINTS[i],POINTS[i+1]),
                distance(POINTS[i],POINTS[i+2]),
                distance(POINTS[i+1],POINTS[i+2])) > PARAMETERS['RADIUS1']):
            return True
        
    return False

def lic_2(NUMPOINTS, POINTS, PARAMETERS):
    """
    LIC 2: Returns True if there exists at least one set of three consecutive data points which form an angle such that angle < (PI - EPSILON) OR angle > (PI + EPSILON).
    """
    if NUMPOINTS < 3:
        return False
    
    for i in range(NUMPOINTS-2):
        angle = calculate_angle(POINTS[i],POINTS[i+1],POINTS[i+2])

        if triangle_area(POINTS[i],POINTS[i+1],POINTS[i+2]) == 0:
            continue

        if (angle < (math.pi - PARAMETERS['EPSILON']) or angle > (math.pi + PARAMETERS['EPSILON'])):
            return True
        
        return False
    
def lic_3(NUMPOINTS, POINTS, PARAMETERS):
    """
    There exists at least one set of three consecutive consecutive elements in pts that are the vertices of a triangle with area greater than AREA1 > 0.
    """

    if NUMPOINTS < 3:
        return False
    
    for i in range(NUMPOINTS-2):
        area = triangle_area(POINTS[i],POINTS[i+1],POINTS[i+2])

        if area > PARAMETERS['AREA1']:
            return True
        
    return False

def lic_5(NUMPOINTS, POINTS):
    """Check if there are two consecutive points where x coordinate decreases"""
    for i in range(NUMPOINTS - 1):
        if POINTS[i + 1][0] < POINTS[i][0]:  # if x coordinate decreases
            return True
    return False

def lic_6(NUMPOINTS, POINTS, N_PTS, DIST):
    """Check if any point is further than DIST from line between first and last points"""
    if NUMPOINTS < 3:
        return False
        
    def point_to_line_distance(point, start, end):
        if start == end:
            return ((point[0] - start[0])**2 + (point[1] - start[1])**2)**0.5
            
        # Calculate perpendicular distance from point to line
        num = abs((end[1] - start[1])*point[0] #(y₂-y₁)x
        - (end[0] - start[0])*point[1] # -(x2-x1)y
        + end[0]*start[1] #x2y1
        - end[1]*start[0]) #-y2x1
        
        den = ((end[1] - start[1])**2 #(y2-y1)^2
        + (end[0] - start[0])**2)**0.5 # +(x2-x1)^2
        
        return num/den
    #Sliding window Check: Example N_PTS of 3 and will give [0] to [2], [1] to [3]...[n-3] to [n-2]
    for i in range(NUMPOINTS - N_PTS + 1):
        first = POINTS[i]
        last = POINTS[i + N_PTS - 1]
        
        # Check all points between first and last
        for j in range(i + 1, i + N_PTS - 1):
            if point_to_line_distance(POINTS[j], first, last) > DIST:
                return True
    return False

def lic_7(NUMPOINTS, POINTS, K_PTS, LENGTH1):
    """Check if there are two points K_PTS apart with distance > LENGTH1"""
    if NUMPOINTS < 3:
        return False
        
    for i in range(NUMPOINTS - K_PTS):
        p1 = POINTS[i]
        p2 = POINTS[i + K_PTS]
        dist = ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5
        if dist > LENGTH1:
            return True
    return False

def lic_8(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1):
    """Check if there are three points that can't fit in circle of RADIUS1"""
    if NUMPOINTS < 5:
        return False
        
    def cant_fit_in_circle(p1, p2, p3, radius):
        # Calculate distances between points
        a = ((p2[0] - p3[0])**2 + (p2[1] - p3[1])**2)**0.5
        b = ((p1[0] - p3[0])**2 + (p1[1] - p3[1])**2)**0.5
        c = ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
        
        # If points form a line, check max distance
        # (a,b), (m,n) and (x,y) are collinear if (n-b)(x-m) = (y-n)(m-a); due to floating point used < epsilon instead 
        if abs((p2[1] - p1[1])*(p3[0] - p1[0]) - 
               (p3[1] - p1[1])*(p2[0] - p1[0])) < 1e-10:
            return max(a, b, c) > 2*radius
            
        # Calculate circumradius; Heron's formula for area of triangle
        s = (a + b + c)/2 
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        circumradius = (a*b*c)/(4*area) #R = abc/4*area when a,b,c are three sides of triangle and A is the area of triangle
        return circumradius > radius
    
    #Seperated by exactly A_PTS, B_PTS consecutive intervening points; give 3 consecutive points for calculation (Sliding window)
    for i in range(NUMPOINTS - A_PTS - B_PTS - 2):
        if cant_fit_in_circle(POINTS[i], 
                            POINTS[i + A_PTS + 1],
                            POINTS[i + A_PTS + B_PTS + 2], 
                            RADIUS1):
            return True
    return False

def lic_9(NUMPOINTS, POINTS, C_PTS, D_PTS, EPSILON):
    """Check if three points form angle < (PI-EPSILON) or > (PI+EPSILON)"""
    if NUMPOINTS < 5:
        return False
        
    def get_angle(p1, vertex, p2):
        if p1 == vertex or p2 == vertex:
            return 0  # undefined angle
            
        # Calculate vectors
        v1 = (p1[0] - vertex[0], p1[1] - vertex[1]) #v1 = p1 - vertex
        v2 = (p2[0] - vertex[0], p2[1] - vertex[1]) #v2 = p2 - vertex
        
        # Calculate dot product and magnitudes
        dot = v1[0]*v2[0] + v1[1]*v2[1]
        mag1 = (v1[0]**2 + v1[1]**2)**0.5
        mag2 = (v2[0]**2 + v2[1]**2)**0.5
        
        if mag1 == 0 or mag2 == 0:
            return 0  # undefined angle
            
        # Calculate angle
        return math.acos(max(min(dot/(mag1*mag2), 1), -1)) #cos(θ) = (v1·v2)/(|v1|*|v2|), hence θ = acos...

    #Sequence of 3 points to check angles
    for i in range(NUMPOINTS - C_PTS - D_PTS - 2):
        angle = get_angle(POINTS[i],
                         POINTS[i + C_PTS + 1],
                         POINTS[i + C_PTS + D_PTS + 2])
        if angle != 0 and (angle < math.pi - EPSILON or angle > math.pi + EPSILON):
            return True
    return False

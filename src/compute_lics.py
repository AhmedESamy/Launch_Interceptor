import math
import src.utils as utils

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
    CMV[0] = lic_0(NUMPOINTS, POINTS, PARAMETERS['LENGTH1'])
    CMV[1] = lic_1(NUMPOINTS, POINTS, PARAMETERS['RADIUS1'])
    CMV[2] = lic_2(NUMPOINTS, POINTS, PARAMETERS['EPSILON'])
    CMV[3] = lic_3(NUMPOINTS, POINTS, PARAMETERS['AREA1'])
    CMV[4] = lic_4(NUMPOINTS, POINTS, PARAMETERS['Q_PTS'], PARAMETERS['QUADS'])
    CMV[5] = lic_5(NUMPOINTS, POINTS)
    CMV[6] = lic_6(NUMPOINTS, POINTS, PARAMETERS['N_PTS'], PARAMETERS['DIST'])
    CMV[7] = lic_7(NUMPOINTS, POINTS, PARAMETERS['K_PTS'], PARAMETERS['LENGTH1'])
    CMV[8] = lic_8(NUMPOINTS, POINTS, PARAMETERS['A_PTS'], 
                   PARAMETERS['B_PTS'], PARAMETERS['RADIUS1'])
    CMV[9] = lic_9(NUMPOINTS, POINTS, PARAMETERS['C_PTS'], 
                   PARAMETERS['D_PTS'], PARAMETERS['EPSILON'])
    CMV[10] = lic_10(NUMPOINTS, POINTS, PARAMETERS['E_PTS'], PARAMETERS['F_PTS'], 
                     PARAMETERS['AREA1'])
    CMV[11] = lic_11(NUMPOINTS, POINTS, PARAMETERS['G_PTS'])
    CMV[12] = lic_12(NUMPOINTS, POINTS, PARAMETERS['K_PTS'], PARAMETERS['LENGTH1'],
                     PARAMETERS['LENGTH2'])
    CMV[13] = lic_13(NUMPOINTS, POINTS, PARAMETERS['A_PTS'], PARAMETERS['B_PTS'], 
                     PARAMETERS['RADIUS1'], PARAMETERS['RADIUS2'])
    CMV[14] = lic_14(NUMPOINTS, POINTS, PARAMETERS['E_PTS'], PARAMETERS['F_PTS'], 
                     PARAMETERS['AREA1'], PARAMETERS['AREA2'])
    return CMV

# Placeholder functions for individual LIC computations
def lic_0(NUMPOINTS, POINTS, LENGTH1):
    """
    LIC 0: Check if there exists at least one set of two consecutive data points
    that are a distance greater than LENGTH1 apart.
    """
    if NUMPOINTS < 2:
        return False
    
    for i in range(NUMPOINTS-1):
        dist = utils.distance(POINTS[i],POINTS[i+1])

        if dist > LENGTH1:
            return True
        
    return False

def lic_1(NUMPOINTS, POINTS, RADIUS1):
    """
    LIC 1: Check if three consecutive data points cannot all be contained within
    or on a circle of radius RADIUS1.
    """
    if NUMPOINTS < 3:
        return False
    
    for i in range(NUMPOINTS-2):
        if (max(utils.distance(POINTS[i],POINTS[i+1]),
                utils.distance(POINTS[i],POINTS[i+2]),
                utils.distance(POINTS[i+1],POINTS[i+2])) > 2*RADIUS1):
            return True
        
    return False

def lic_2(NUMPOINTS, POINTS, EPSILON):
    """
    LIC 2: Returns True if there exists at least one set of three consecutive data points which form an angle such that angle < (PI - EPSILON) OR angle > (PI + EPSILON).
    """
    if NUMPOINTS < 3:
        return False
    
    for i in range(NUMPOINTS-2):
        angle = utils.calculate_angle(POINTS[i],POINTS[i+1],POINTS[i+2])

        if utils.triangle_area(POINTS[i],POINTS[i+1],POINTS[i+2]) == 0:
            continue

        if (angle < (math.pi - EPSILON) or angle > (math.pi + EPSILON)):
            return True
        
    return False
    
def lic_3(NUMPOINTS, POINTS, AREA1):
    """
    There exists at least one set of three consecutive consecutive elements in pts that are the vertices of a triangle with area greater than AREA1 > 0.
    """

    if NUMPOINTS < 3:
        return False
    
    for i in range(NUMPOINTS-2):
        area = utils.triangle_area(POINTS[i],POINTS[i+1],POINTS[i+2])

        if area > AREA1:
            return True
        
    return False

def lic_4(NUMPOINTS, POINTS, Q_PTS, QUADS):
    """
    Return True if there exists at least one set of 2 <= Q_PTS consecutive elements in pts that lie in more than QUADS quadrants.    
    """

    if NUMPOINTS < Q_PTS:
        return False
    
    for i in range(NUMPOINTS-Q_PTS+1):
        q_consec = POINTS[i:i+Q_PTS]
        quad_count = [0,0,0,0] # Counters for Quadrants I, II, III, VI respectively
        for p in q_consec:
            if p[1] >= 0: # Quadrant I or II
                if p[0] >= 0:
                    quad_idx = 0 # Quadrant I
                else: 
                    quad_idx = 1 # Quadrant II
            else: # Quadrant III or IV
                if p[0] <= 0:
                    quad_idx = 2 # Quadrant III
                else: 
                    quad_idx = 3 # Quadrant VI 
            
            quad_count[quad_idx] += 1

        if (4 - quad_count.count(0)) > QUADS:
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
            return utils.distance(point, start)
            
        # Calculate perpendicular distance from point to line
        area = abs(utils.triangle_area(point, start, end)) * 2
        base = utils.distance(start, end)
        
        return area/base if base != 0 else utils.distance(point, start)
    
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
        
    for i in range(NUMPOINTS - K_PTS - 1):
        p1 = POINTS[i]
        p2 = POINTS[i + K_PTS + 1]
        if utils.distance(p1, p2) > LENGTH1:
            return True
    return False

def lic_8(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1):
    """Check if there are three points that can't fit in circle of RADIUS1"""
    if NUMPOINTS < 5:
        return False
        
    def cant_fit_in_circle(p1, p2, p3, radius):
        # Calculate distances between points
        a = utils.distance(p2, p3)
        b = utils.distance(p1, p3)
        c = utils.distance(p1, p2)
        
        # If points form a line, check max distance
        area = utils.triangle_area(p1, p2, p3)
        if abs(area) < 1e-10:  # Points are collinear
            return max(a, b, c) > 2*radius
            
        # Calculate circumradius using R = abc/(4A)
        circumradius = (a * b * c)/(4 * area)
        return circumradius > radius
    
    #Seperated by exactly A_PTS, B_PTS consecutive intervening points
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

    #Sequence of 3 points to check angles
    for i in range(NUMPOINTS - C_PTS - D_PTS - 2):
        angle = utils.calculate_angle(POINTS[i],
                              POINTS[i + C_PTS + 1],
                              POINTS[i + C_PTS + D_PTS + 2])
        if not math.isnan(angle) and (angle < math.pi - EPSILON or angle > math.pi + EPSILON):
            return True

    return False

def lic_10(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1):
    """ 
    Check if there exists a set of three data points separated by exactly E_PTS and F_PTS
    consecutive points, that are the vertices of a triangle with area greater than AREA1.
    This condition does not hold for NUMPOINTS < 5.
    """
    assert E_PTS >= 1, f"AssertionError: E_PTS must be at least 1, but got {E_PTS}"
    assert F_PTS >= 1, f"AssertionError: F_PTS must be at least 1, but got {F_PTS}"
    assert E_PTS + F_PTS <= NUMPOINTS - 3, f"AssertionError: Sum of E_PTS and F_PTS must be at most {NUMPOINTS - 3}, but got {E_PTS + F_PTS}"

    if NUMPOINTS < 5:
        return False
    
    for i in range(NUMPOINTS - E_PTS - F_PTS - 2):
        if utils.triangle_area(POINTS[i], 
                               POINTS[i + E_PTS + 1],
                               POINTS[i + E_PTS + F_PTS + 2]) > AREA1:
            return True

    return False

def lic_11(NUMPOINTS, POINTS, G_PTS):
    """ 
    Check if there exists a set of two data points (X[i], Y[i]) and 
    (X[j], Y[j]), separated by exactly G_PTS, where i < j and
    X[j] - X[i] < 0.
    """
    assert G_PTS >= 1 and G_PTS <= NUMPOINTS - 2, f'AssertionError: G_PTS must be between 1 and {NUMPOINTS-2}, but got {G_PTS}'
    
    if NUMPOINTS < 3:
        return False
    
    for i in range(NUMPOINTS - G_PTS - 1):
        if POINTS[i + G_PTS + 1][0] < POINTS[i][0]:
            return True
    return False

def lic_12(NUMPOINTS, POINTS, K_PTS, LENGTH1, LENGTH2):
    """
    Check that there exists two sets of two data points, separated
    by exactly K_PTS, which are greater than LENGTH1 length apart 
    and less than LENGTH2 length apart respectively. Note that the
    two sets can contain the same data points. 
    """
    assert LENGTH2 >= 0, f"AssertionError: LENGTH2 must be at least 0, but got {LENGTH2}" 
    
    if NUMPOINTS < 3:
        return False
    length1_condition = False
    length2_condition = False
    for i in range(NUMPOINTS - K_PTS - 1):
        if length1_condition and length2_condition:
            # Early break, if both conditions are fulfilled
            # before iterating all points
            break
        
        dist = utils.distance(POINTS[i + K_PTS + 1], POINTS[i])
        if dist > LENGTH1:
            length1_condition = True
        if dist < LENGTH2:
            length2_condition = True
    return length1_condition and length2_condition

def lic_13(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1, RADIUS2):
    """
    Check if there exists at least two sets of three points, separated by
    exactly A_PTS and B_PTS consecutive points, that cannot be contained
    withing or on a circle of radius RADIUS1 and that can be contained
    in or on a circle of radius RADIUS2. The two sets may contain the
    same points.
    """
    if NUMPOINTS < 5:
        return False
    
    radius1_condition = False
    radius2_condition = False
    for i in range(NUMPOINTS - A_PTS - B_PTS - 2):
        if radius1_condition and radius2_condition:
            # Early break, if both conditions are fulfilled
            # before iterating all points
            break
        p1 = POINTS[i]
        p2 = POINTS[i + A_PTS + 1]
        p3 = POINTS[i + A_PTS + B_PTS + 2]
        """ 
        Sources used:
        user856, Given a set of 3 2D points, how to find if they lie within 
        a circle of a given radius?, URL (version: 2017-04-15): 
        https://math.stackexchange.com/q/2234810
        
        joriki (https://math.stackexchange.com/users/6622/joriki), 
        Is there any way to judge if a triangle is acute or obtuse?, 
        URL (version: 2012-09-24): https://math.stackexchange.com/q/201640
        """
        a = utils.distance(p1, p2)
        b = utils.distance(p1, p3)
        c = utils.distance(p2, p3)
        k = utils.triangle_area(p1, p2, p3)
        
        squares = [a*a, b*b, c*c]
        c2 = max(squares)
        squares.remove(max(squares))
        two_shortest_sum = sum(squares)
        min_radius = math.nan
        if two_shortest_sum > c2:
            # a^2 + b^2 > c^2 => Acute triangle
            # Smallest enclosing circle given by the circumradius
            min_radius = (a * b * c) / (4 * k)
        else:
            # a^2 + b^2 <= c^2 => Right/Obtuse triangle
            # Smallest enclosing circle given by longest edge
            # of the triangle, giving the diameter
            min_radius = max(a, b, c) / 2
        if min_radius > RADIUS1:
            radius1_condition = True
        if min_radius <= RADIUS2:
            radius2_condition = True

    return radius1_condition and radius2_condition

def lic_14(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1, AREA2):
    """
    Check if there exists at least two sets of three points, separated by
    exactly E_PTS and F_PTS consecutive points, that create a triangle with
    area greater than AREA1 and a triangle with area less than AREA2 respectively.
    The two sets may contain the same points.
    """
    if NUMPOINTS < 5:
        return False    
    
    area1_condition = False
    area2_condition = False
    
    for i in range(NUMPOINTS - E_PTS - F_PTS - 2):
        if area1_condition and area2_condition:
            break
        area = utils.triangle_area(POINTS[i],
                                   POINTS[i + E_PTS + 1],
                                   POINTS[i + E_PTS + F_PTS + 2])
        if area > AREA1:
            area1_condition = True
        if area < AREA2:
            area2_condition = True

    return area1_condition and area2_condition
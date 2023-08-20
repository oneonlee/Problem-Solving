import math

def solve_intersection_point(line_x, line_y):
    """
    line_x: Ax + By + E = 0
    line_y: Cx + Dy + F = 0
    intersection_point: ( (B*F-E*D)/(A*D-B*C), (E*C-A*F)/(A*D-B*C) )
    """
    
    A, B, E = line_x[0], line_x[1], line_x[2]
    C, D, F = line_y[0], line_y[1], line_y[2]
    
    
    if A*D - B*C == 0: # AD - BC = 0인 경우 두 직선은 평행 또는 일치합니다.
        is_solved = False
        intersection_point = None
    else:
        is_solved = True
        intersection_point = [ (B*F-E*D)/(A*D-B*C), (E*C-A*F)/(A*D-B*C) ]
    
    return is_solved, intersection_point


def draw_stars(points):
    inf = math.inf
    max_x, max_y = -inf, -inf
    min_x, min_y = inf, inf
    
    for (x, y) in points:
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    
    len_x = max_x - min_x + 1
    len_y = max_y - min_y + 1
    
    # 최좌하단에 있는 좌표가 원점에 오도록 교점들을 절대적으로 이동
    new_points = []
    for (x, y) in points:
        x = x - min_x
        y = y - min_y
        new_points.append( (x, y) )
    
    # 빈 좌표계 만들기
    coordinate = []
    for _ in range(len_y):
        coordinate.append(['.' for _ in range(len_x)])
        
    for (x, y) in new_points:
        coordinate[y][x] = '*'
    
    answer = [''.join(x_axis) for x_axis in coordinate]
    answer.reverse()
    return answer
    
def solution(lines):
    int_points = []
    
    for idx_x, line_x in enumerate(lines):
        if idx_x == len(lines)-1:
            break
        for idx_y in range(idx_x+1, len(lines)):
            line_y = lines[idx_y]
            is_solved, point = solve_intersection_point(line_x, line_y)
            
            if is_solved == True:
                if point[0].is_integer() and point[1].is_integer():
                    if (int(point[0]), int(point[1])) not in int_points:
                        int_points.append( ( int(point[0]), int(point[1]) ) )
                    
        
    answer = draw_stars(int_points)
    
    
    return answer
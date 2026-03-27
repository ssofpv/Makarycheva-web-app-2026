import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __sub__(self, no):
        return Point(self.x - no.x, self.y - no.y, self.z - no.z)
        
    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z
        
    def cross(self, no):
        return Point(
            self.y * no.z - self.z * no.y,
            self.z * no.x - self.x * no.z,
            self.x * no.y - self.y * no.x
        )
        
    def absolute(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

def plane_angle(a, b, c, d):
    # Векторы AB и BC
    ab = b - a
    bc = b - c # В задании написано AB=B-A, BC=B-C. 
               # Обычно вектор BC это C-B, но следуем формуле из условия:
               # X = AB x BC, где AB=B-A, BC=B-C.
               # ВНИМАНИЕ: В условии формула BC=B-C, что фактически вектор CB.
               # Следуем условию буквально.
    
    # Векторы для второй плоскости: BC (тот же B-C) и CD (C-D? или D-C?)
    # Условие: "плоскости, образованными точками A, B, C и B, C, D"
    # Y = BC x CD. (тут не уточнено определение CD в условии, но по аналогии CD = C-D)
    
    # Однако, стандартное определение нормали к плоскости ABC - это векторное произведение (B-A)x(C-B).
    # Но в задании даны четкие формулы:
    # X = AB x BC, где AB = B - A, BC = B - C.
    # Y = BC x CD. По логике задачи CD = C - D (или D - C, если это вектор C->D). 
    # Обычно в таких задачах на Hackerrank подразумевается последовательность:
    # X = (B-A) x (C-B) и Y = (C-B) x (D-C).
    # Но раз в условии написано BC=B-C, значит это вектор из C в B.
    # Допустим CD = C - D.
    
    cd = c - d
    
    x_vec = ab.cross(bc)
    y_vec = bc.cross(cd)
    
    try:
        cos_phi = x_vec.dot(y_vec) / (x_vec.absolute() * y_vec.absolute())
        # Коррекция для float precision errors
        if cos_phi > 1.0: cos_phi = 1.0
        if cos_phi < -1.0: cos_phi = -1.0
        
        angle_rad = math.acos(cos_phi)
        return math.degrees(angle_rad)
    except ZeroDivisionError:
        return 0.0

if __name__ == '__main__':
    points = []
    for _ in range(4):
        points.append(list(map(float, input().split())))
    
    a = Point(*points[0])
    b = Point(*points[1])
    c = Point(*points[2])
    d = Point(*points[3])
    
    print(f"{plane_angle(a, b, c, d):.2f}")
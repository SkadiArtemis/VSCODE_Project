import math
from random import random
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius 
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        random_radius = math.sqrt(random()) * self.radius
        random_angle = 2 * math.pi * random()
        random_x = self.x_center + random_radius * math.cos(random_angle)
        random_y = self.y_center + random_radius * math.sin(random_angle)
        
        return [random_x, random_y]
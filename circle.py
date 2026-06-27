import matplotlib.pyplot as plt 
# %matplotlib inline 
class Circle(object):
    def __init__(self, radius=3, color="blue"):
        self.radius=radius
        self.color=color
    def add_radius(self,radius):
        self.radius+=radius
        return (self.radius)
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0,0) ,radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()
RedCircle=Circle(10,'red')
print(dir(RedCircle))
print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)
RedCircle.drawCircle()

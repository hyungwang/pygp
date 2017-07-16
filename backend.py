__Author__ = 'Olaitan'
class GP:
    def __init__(self):
        self.new_course = {}
        self.gp = []


    def add(self, course, grade, unit):
        #self.new_course["course"] = course
        #self.new_course["grade"] = grade
        #self.new_course["unit"] = unit
        #self.gp.append(self.new_course)
        self.gp.append({
                "course":course,
                "grade":grade,
                "unit":unit
                })
        print(self.gp)

    def new(self):
        self.gp = []

    def view(self):
        return self.gp

    def calculate(self):
        print(self.gp)
        self.mark = 0
        for grade in range(len(self.gp)):
           self.mark = self.mark + (self.grade_conv(self.gp[grade]['grade']) * self.gp[grade]['unit'])

        self.units = sum([i["unit"] for i in self.gp])
        print(self.mark/self.units)
        return (self.mark/self.units)





    def grade_conv(self, grade):
        conv = {'A':5,'B':4,'C':3,'D':2,'E':1,'F':0}
        return conv.get(grade.upper(),0)
        

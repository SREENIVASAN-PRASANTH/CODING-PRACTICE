class human:
    def __init__(fun,teeth,eyes,ears):
        fun.teeth = teeth
        fun.eyes = eyes
        fun.ears = ears

    # def __str__(self):
    #     print(f"Teeth : {self.teeth}")

    def printAttribute(self):
        print(f"{self.teeth} {self.eyes} {self.ears}")

thamizh = human(32,2,2)
prashant = human(32,3,3)
thamizh.printAttribute()


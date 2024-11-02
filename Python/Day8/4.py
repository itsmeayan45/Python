import math
def paint_calc(height,width,coverage):
    cans=math.ceil((height*width)//coverage)
    return cans
test_h=int(input("Height of Wall: "))
test_w=int(input("Width of Wall: "))
coverage=5
can=paint_calc(height=test_h,width=test_w,coverage=5)
print(f"You'll need to buy {can} pieces of can.")
for _ in range(int(input())):
    x1,y1,x2,y2=map(int, input().split());x3,y3,x4,y4=map(int, input().split())
    # Check if given line is a point instead of line (INVALID)
    if (x1-x2 == 0 and y1-y2 == 0) or (x3-x4 == 0 and y3-y4 == 0):
        print("INVALID")
    # Check if line is parallel (NO)
    elif (y1-y2==0 and y3-y4==0 and x1-x2!=0 and x3-x4!=0) or (x1-x2==0 and x3-x4==0 and y1-y2!=0 and y3-y4!=0):
        print("NO")
    # Check if one line is horizontal or vertical and the other is not (NO)
    elif (x1-x2==0 and x3-x4!=0 and y3-y4!=0) or (x3-x4==0 and x1-x2!=0 and y1-y2!=0) or (y1-y2==0 and x3-x4!=0 and y3-y4!=0) or (y3-y4==0 and x1-x2!=0 and y1-y2!=0):
        print("NO")
    # Check if one line is vertical and the other is horizontal (YES)
    elif (x1-x2==0 and y3-y4==0) or (y1-y2==0 and x3-x4==0):
        print("YES")
    # Check if line is perpendicular with rounded gradient avoid floating point difference
    elif round((y2-y1)/(x2-x1),5) == round((-1/((y4-y3)/(x4-x3))),5):
        print("YES")
    # If nothing matches, then lines are not perpendicualr and are of weird orientation
    else:
        print("NO")

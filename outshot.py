def calculateOuthsot(point):
    helper = point

    if point > 170:
        return "No checkout"
    else:
        with open("checkouts.txt") as f:
            lines = f.readlines()
            for i in range(0, len(lines)):
                values = lines[i].split()
                if values[0] == str(helper):
                    values.pop(0)
                    return ", ".join(values)


result = calculateOuthsot(117)
print(result)




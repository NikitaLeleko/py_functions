def open_or_senior(data: list):
    output = []
    for i in range(len(data)):
        if -2 < data[i][1] < 26 and data[i][0] > 54 and data[i][1] > 6:
            output.append("Senior")
        else:
            output.append("Open")
    return output

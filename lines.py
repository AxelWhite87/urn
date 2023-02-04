counts = [100,1000,10000,100000]

for c in counts:
    line_data = "Ipsum lorem dolores moret"
    lines_to_write = []
    for lines in range(c):
        lines_to_write.append(line_data)
    with open(f"{c}.txt", "w") as f:
        f.writelines(lines_to_write)


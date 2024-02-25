def max_particle_speed(positions, time_interval):
    speeds = []
    for i in range(len(positions) - 1):
        speed = abs((positions[i+1] - positions[i]) / time_interval)
        speeds.append(speed)
    return round(max(speeds), 2)

positions = [1, 3, 4, 7, 8, 9, 10]
time_interval = 0.01
result = max_particle_speed(positions, time_interval)
print(int(result))

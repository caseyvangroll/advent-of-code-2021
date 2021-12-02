def get_depth_increase_ct(depth_measurements):
    depth_increase_ct = 0
    for i in range(1, len(depth_measurements)):
        if depth_measurements[i] > depth_measurements[i - 1]:
            depth_increase_ct += 1
    return depth_increase_ct


if __name__ == '__main__':
    with open('./input.txt') as f:
        depth_measurements = [int(line.strip()) for line in f.readlines()]
        depth_increase_ct = get_depth_increase_ct(depth_measurements)
        print('Depth increased {} times.'.format(depth_increase_ct))

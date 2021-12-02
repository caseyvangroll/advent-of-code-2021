def get_depth_increase_ct(depth_measurements, window_size=1):
    depth_increase_ct = 0
    for i in range(window_size, len(depth_measurements)):
        # The two windows almost entirely overlap
        if depth_measurements[i] > depth_measurements[i - window_size]:
            depth_increase_ct += 1
    return depth_increase_ct


if __name__ == '__main__':
    with open('./input.txt') as f:
        depth_measurements = [int(line.strip()) for line in f.readlines()]
        for window_size in [1, 3]:
            depth_increase_ct = get_depth_increase_ct(depth_measurements, window_size)
            print('Depth increased {} times with a window size of {}.'.format(depth_increase_ct, window_size))

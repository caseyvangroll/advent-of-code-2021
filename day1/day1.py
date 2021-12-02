def get_depth_increase_ct(inputs):
    depth_increase_ct = 0
    for i in range(1, len(inputs)):
        if inputs[i] > inputs[i - 1]:
            depth_increase_ct += 1
    return depth_increase_ct


if __name__ == "__main__":
    with open('./input.txt') as f:
        inputs = [int(line.strip()) for line in f.readlines()]
        depth_increase_ct = get_depth_increase_ct(inputs)
        print("Depth increased {} times.".format(depth_increase_ct))

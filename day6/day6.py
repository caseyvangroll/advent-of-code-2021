def get_fish_ct(fish_at_each_age, day_ct):
    while day_ct > 0:
        birthing_fish_ct = fish_at_each_age.pop(0)
        fish_at_each_age.append(birthing_fish_ct)
        fish_at_each_age[6] += birthing_fish_ct
        day_ct -= 1

    return sum(fish_at_each_age)


if __name__ == '__main__':
    with open('./input.txt') as f:
        fish_ages = [int(fish_age) for fish_age in f.readline().strip().split(',')]
        fish_at_each_age = [0] * 9
        for fish_age in fish_ages:
            fish_at_each_age[fish_age] += 1

        for day_ct in [80, 256]:
            fish_ct = get_fish_ct(fish_at_each_age[:], day_ct)
            print('Fish count after {} days: {}'.format(day_ct, fish_ct))

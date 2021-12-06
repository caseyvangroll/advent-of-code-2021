import webbrowser
import sys
import os


def create_local_dir(day_num):
    dir_name = './day{}'.format(day_num)
    script_filename = '{}/day{}.py'.format(dir_name, day_num)
    input_filename = '{}/input.txt'.format(dir_name)

    if not os.path.exists(dir_name):
        print('Creating {}'.format(dir_name))
        os.mkdir(dir_name)
    if not os.path.exists(script_filename):
        print('Creating {}'.format(script_filename))
        with open('./template.py', 'r') as f:
            template = f.readlines()
        with open(script_filename, 'w') as f:
            f.writelines(template)
    if not os.path.exists(input_filename):
        print('Creating {}'.format(input_filename))
        open(input_filename, 'a').close()


def open_puzzle_in_chrome(day_num):
    url = "https://adventofcode.com/2021/day/{}".format(day_num)
    webbrowser.get('open -a /Applications/Google\ Chrome.app %s').open(url)


if __name__ == "__main__":
    day_num = sys.argv[1]
    if not day_num.isdigit():
        raise Exception('start.py requires single argument: digit day of advent calendar')
    create_local_dir(day_num)
    open_puzzle_in_chrome(day_num)

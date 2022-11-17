from enum import Enum


class BorderSymbol(Enum):
    top_left_border = '┌'
    filler_character = '─'
    middle_top_div = '┬'
    top_right_border = '┐'
    bottom_left_border = '└'
    middle_bottom_div = '┴'
    bottom_right_border = '┘'


def grab_border_symbols():
    print("Do you wish to customize the table border symbols?(y/n)")
    choice = input('> ')
    if choice in ['y', 'Y', 'Yes', 'yes', 'YES']:
        display_table()
    elif choice in ['n', 'N', 'No', 'no', 'NO']:
        print()
    else:
        print("Invalid choice! Use only full word choices. ")


def display_top_borders(l_corners="╔", filler_character="═", middle_div="╦", r_corners="╗", column_length=1):
    print(l_corners + filler_character * column_length + middle_div + filler_character * column_length + r_corners)


def display_bottom_borders(l_corners='╚', filler_character="═", middle_div="╩", r_corners="╝", column_length=1):
    print(l_corners + filler_character * column_length + middle_div + filler_character * column_length + r_corners)


def display_row(value_dict, start_div="║", end_div="║", mid_div="║", line_length=79, is_header=False):
    print_err = line_length // len(value_dict) - 1
    print(start_div, end='')
    for index, key in enumerate(value_dict.keys()):
        if not is_header:
            key = value_dict[key]
        print(key.ljust(print_err), end=mid_div if index != len(value_dict) - 1 else '')
    print(end_div)


def display_table(*args, line_length=79):
    for index, value_dict in enumerate(*args):
        print_column_length = line_length // len(value_dict) - 1
        # print(value_dict)
        if index == 0:
            display_top_borders(BorderSymbol.top_left_border.value, BorderSymbol.filler_character.value,
                                BorderSymbol.middle_top_div.value,
                                BorderSymbol.top_right_border.value,
                                print_column_length)
            display_row(value_dict, start_div='│', end_div='│', mid_div='┇', line_length=line_length, is_header=True)
        display_row(value_dict, start_div='│', end_div='│', mid_div='┇', line_length=line_length)
        if index == len(value_dict):
            display_bottom_borders(BorderSymbol.bottom_left_border.value, BorderSymbol.filler_character.value,
                                   BorderSymbol.middle_bottom_div.value, BorderSymbol.bottom_right_border.value,
                                   print_column_length)


# still a wip. Maybe i'll add classes to the main menu before starting a solution for a dict update
def dict_update(*args):
    pass


def main():
    all_option_dict = [
        {'Opt. no.': '1', 'Req': 'Symbol rotation'},
        {'Opt. no.': '2', 'Req': 'Factorial functions'},  # optional comma
        {'Opt. no.': '3', 'Req': 'Harmonic Mean'},  # optional comma
    ]
    display_table(all_option_dict)

    # ------------------------------------------
    # testing
    # grab_border_symbols()


if __name__ == "__main__":
    main()

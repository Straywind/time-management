from interface_common import (
    parse_ascii_banner,
    print_ascii_banner,
    quit_program,
    clear_screen,
)


def prompt_time_management():
    print_ascii_banner(parse_ascii_banner("banners/tm.txt"))
    return input(
        """1: Make a note
2: Set a task and completion goal
3: Print notes and tasks
4: Complete a task
5: Print overdue tasks
6: Print SCRUM notes
7: Quit
"""
    )


def run_menu_loop_tm(facade):
    while True:
        choice = prompt_time_management()
        clear_screen()
        map_choice_to_function(choice, facade)


def map_choice_to_function(choice, facade):
    if choice == "1":
        make_a_note(facade)
    elif choice == "2":
        set_a_task(facade)
    elif choice == "3":
        print_contents(facade)
    elif choice == "4":
        complete_task(facade)
    elif choice == "5":
        print_overdue_tasks(facade)
    elif choice == "6":
        print_scrum_notes(facade)
    elif choice == "7":
        quit_program(facade)
    else:
        print("Choice not recognized.")


def make_a_note(facade):
    clear_screen()
    note = input("Make a note: ")
    facade.update_table_with_note(note)
    clear_screen()


def set_a_task(facade):
    clear_screen()
    note = input("Set a task: ")
    days_until_completion = input("Set number of days to complete: ")
    facade.update_table_with_task(note, days_until_completion)
    clear_screen()


def print_contents(facade):
    clear_screen()
    table_rows = facade.get_all_items()
    if len(table_rows) == 0:
        return
    else:
        for row in table_rows:
            print(row)
        print("\n\n")


def complete_task(facade):
    clear_screen()
    row_id = input("Select note id for completion: ")
    facade.update_completion(row_id)
    clear_screen()


def print_overdue_tasks(facade):
    clear_screen()
    table_rows = facade.get_overdue_items()
    for row in table_rows:
        print(row)


def print_scrum_notes(facade):
    clear_screen()
    print_ascii_banner(parse_ascii_banner("banners/scrum.txt"))
    table_rows = facade.get_last_days_items()
    for row in table_rows:
        print(row)

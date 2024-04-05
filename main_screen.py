import curses



from utils import shutdown_computer,get_ip_address




def main(stdscr):
    # Initialize curses
    curses.start_color()
    curses.use_default_colors()

    # Set up color pairs
    curses.init_pair(1, curses.COLOR_BLACK,242)  # Grey background
    curses.init_pair(2, curses.COLOR_BLACK, 130)  # Orange background

    # Get screen dimensions
    screen_height, screen_width = stdscr.getmaxyx()

    # Calculate dimensions for the two partitions
    top_height = int(0.6 * screen_height)
    bottom_height = screen_height - top_height

    # Create windows for each partition
    top_win = curses.newwin(top_height, screen_width, 0, 0)
    bottom_win = curses.newwin(bottom_height, screen_width, top_height, 0)

    # Set background colors for each partition
    top_win.bkgd(' ', curses.color_pair(1))  # Grey background
    bottom_win.bkgd(' ', curses.color_pair(2))  # Orange background

    # Draw borders to distinguish the partitions
    stdscr.hline(top_height, 0, '-', screen_width)
    stdscr.refresh()

    # Refresh the windows to apply changes
    top_win.refresh()
    bottom_win.refresh()

    # Define labels
    novaigu_label = "Novaigu Udr 1.0.0"
    novaigu_platform_label = "Novaigu Inc Platform"
    ip_address = get_ip_address()
    novaigu_http_label = "Https://{}".format(ip_address)

    # Calculate positions for labels
    label_width = max(len(novaigu_label), len(novaigu_platform_label), len(novaigu_http_label))
    label_height = 2
    label_x = (screen_width - label_width) // 2
    label_y = top_height // 2

    # Add labels to top_win
    top_win.addstr(label_y, label_x, novaigu_label)
    top_win.addstr(label_y + label_height, label_x, novaigu_platform_label)
    top_win.addstr(label_y + 2 * label_height, label_x, novaigu_http_label)

    # Refresh the top_win to apply changes
    top_win.refresh()

    # Add clickable label at the bottom-left corner
    bottom_win.addstr(bottom_height - 2, 1, "<F2> Configuration System", curses.A_UNDERLINE)
    bottom_win.addstr(bottom_height - 2, screen_width-len("<F12> Shut down/Restart")-2, "<F12> Shut down/Restart", curses.A_UNDERLINE)
    bottom_win.refresh()

    
    # Create a pop-up window
    popup_height = 10
    popup_width = 40
    popup_y = (screen_height - popup_height//2) // 2
    popup_x = (screen_width - popup_width) // 2
    popup_win = curses.newwin(popup_height, popup_width, popup_y, popup_x)

    # Calculate dimensions for the two partitions within the pop-up window
    popup_top_height = int(0.3 * popup_height)
    popup_bottom_height = popup_height - popup_top_height

    # Create windows for each partition within the pop-up window
    popup_top_win = popup_win.subwin(popup_top_height, popup_width, popup_y, popup_x)
    popup_bottom_win = popup_win.subwin(popup_bottom_height, popup_width, popup_y + popup_top_height, popup_x)

    # Set background colors for each partition within the pop-up window
    popup_top_win.bkgd(' ', curses.color_pair(1))  # Yellow background
    popup_bottom_win.bkgd(' ', curses.color_pair(2))  # Grey background


    # Add label to popup_top_win
    label_text = "Shut Down/Restart"
    label_x = (popup_width - len(label_text)) // 2
    label_y = (popup_top_height - 1) // 2  # Center vertically
    popup_top_win.addstr(label_y, label_x, label_text)

    # Add label to popup_bottom_win
    label_text_bottom = "<F2> Shut down"
    label_x_bottom = 3
    label_y_bottom =1 # Center vertically
    popup_bottom_win.addstr(label_y_bottom, label_x_bottom, label_text_bottom)

    # Add label to popup_bottom_win
    label_text_bottom_12 = "<F11> Restart"
    label_x_bottom = 3
    label_y_bottom =3 # Center vertically
    popup_bottom_win.addstr(label_y_bottom, label_x_bottom, label_text_bottom_12)

    # Add label to popup_bottom_win
    label_text_bottom_esc = "<Esc> Cancle"
    label_x_bottom = 25
    label_y_bottom =5 # Center vertically
    popup_bottom_win.addstr(label_y_bottom, label_x_bottom, label_text_bottom_esc)


    # Wait for F2 key press
    while True:
        key = stdscr.getch()   
        print(key,"=======================key")
        if key == curses.KEY_F2:
            if popup_win:
                shutdown_computer() 
            stdscr.addstr(bottom_height - 2, 0, "test2")
            stdscr.refresh()
        # if if key == curses.KEY_EXIT:
        #         if popup_win:
        elif key == curses.KEY_F12:
            top_win.bkgd(' ', curses.color_pair(0))  # Black background
            bottom_win.bkgd(' ', curses.color_pair(0))
            top_win.refresh()
            bottom_win.refresh()            
            popup_win.refresh()
        elif key == 27:
            popup_win.clear()  # KEY_ESC the pop-up window
            popup_win.refresh() 
            top_win.bkgd(' ', curses.color_pair(1))  # Grey background
            bottom_win.bkgd(' ', curses.color_pair(2))  # Orange background
            top_win.refresh()
            bottom_win.refresh()

curses.wrapper(main)

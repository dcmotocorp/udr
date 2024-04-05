import curses

def authentication_page(stdscr):
    # Clear screen and enable color
    stdscr.clear()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    stdscr.bkgd(' ', curses.color_pair(1))
    
    # Get screen dimensions
    height, width = stdscr.getmaxyx()
    
    # Calculate center coordinates
    center_y = height // 2
    center_x = width // 2
    
    # Print title
    title = "Authentication Page"
    title_x = center_x - (len(title) // 2)
    stdscr.addstr(center_y - 5, title_x, title, curses.color_pair(1) | curses.A_BOLD)
    
    # Print username label
    username_label = "Username: "
    stdscr.addstr(center_y - 2, center_x - (len(username_label) // 2) - 10, username_label, curses.color_pair(1))
    
    # Create username input box
    username_win = curses.newwin(1, 20, center_y - 2, center_x - 8)
    username_win.refresh()
    username_input = ""
    
    # Print password label
    password_label = "Password: "
    stdscr.addstr(center_y, center_x - (len(password_label) // 2) - 10, password_label, curses.color_pair(1))
    
    # Create password input box
    password_win = curses.newwin(1, 20, center_y, center_x - 8)
    password_win.refresh()
    password_input = ""
    
    # Enable cursor for input boxes
    curses.curs_set(1)
    stdscr.refresh()
    # Get username input
    while True:
        username_win.addstr(0, 0, username_input, curses.color_pair(1))
        username_win.refresh()
        ch = username_win.getch()
        if ch == curses.KEY_ENTER or ch == 10:
            break
        elif ch == curses.KEY_BACKSPACE or ch == 127:
            username_input = username_input[:-1]
        else:
            username_input += chr(ch)
    
    # Get password input
    while True:
        password_win.addstr(0, 0, "*" * len(password_input), curses.color_pair(1))
        password_win.refresh()
        ch = password_win.getch()
        if ch == curses.KEY_ENTER or ch == 10:
            break
        elif ch == curses.KEY_BACKSPACE or ch == 127:
            password_input = password_input[:-1]
        else:
            password_input += chr(ch)
    
    # Clear input boxes
    username_win.clear()
    password_win.clear()
    username_win.refresh()
    password_win.refresh()
    
    # Disable cursor
    curses.curs_set(0)
    
    # Authenticate user (dummy authentication for demonstration)
    if username_input == "admin" and password_input == "password":
        authentication_result = "Authentication Successful!"
    else:
        authentication_result = "Authentication Failed!"
    
    # Print authentication result
    stdscr.addstr(center_y + 2, center_x - (len(authentication_result) // 2), authentication_result, curses.color_pair(1) | curses.A_BOLD)
    stdscr.refresh()
    stdscr.getch()

# Initialize curses
curses.wrapper(authentication_page)

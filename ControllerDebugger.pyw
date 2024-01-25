import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Controller Debugger 🎮")

def display_controllers(joystick):
    font = pygame.font.Font(None, 36)
    text_y = 10

    # Display connected controllers
    connected_controllers_text = font.render(f"Connected Controllers: {num_controllers}", True, (255, 255, 255))
    screen.blit(connected_controllers_text, (10, text_y))
    text_y += 40

    # Display button, axis, and hat information
    text_y = display_buttons(joystick, font, text_y)
    text_y = display_axes(joystick, font, text_y)
    text_y = display_hats(joystick, font, text_y)

def display_buttons(joystick, font, text_y):
    # Define button labels for different controllers
    button_labels = []
    # Get the name of the device, if not on the list needs to be added here
    if joystick.get_name() == 'PC Game Controller':
        button_labels = ['X', 'A', 'B', 'Y', 'LB', 'RB', None, None, 'SELECT', 'START']

    elif joystick.get_name() == 'Controller (XBOX 360 For Windows)':
        button_labels = ['A', 'B', 'X', 'Y', 'LB', 'RB', 'BACK', 'START', 'LS', 'RS', 'XBOX BUTTON', 'UP', 'DOWN', 'LEFT', 'RIGHT']
    #else:
    # Have it use default labels
    for k in range(joystick.get_numbuttons()):
        if k < len(button_labels) and joystick.get_button(k):
            button_color = get_button_color(k)
            button_text = font.render(f"Button {k} = {button_labels[k]} is being used", True, button_color)
            screen.blit(button_text, (10, text_y))
            text_y += 40

    return text_y

def axis_test():
    # Function to test joystick axes
    cursor_radius = 10

    # Get joystick positions for the left and right sticks
    left_stick_x = joystick.get_axis(0)
    left_stick_y = joystick.get_axis(1)
    right_stick_x = joystick.get_axis(2)
    right_stick_y = joystick.get_axis(3)

    # Map joystick values to screen coordinates for the left stick (adjust as needed)
    left_cursor_x = int((left_stick_x + 1) * (width / 2))
    left_cursor_y = int((left_stick_y + 1) * (height / 2))

    # Map joystick values to screen coordinates for the right stick (adjust as needed)
    right_cursor_x = int((right_stick_x + 1) * (width / 2))
    right_cursor_y = int((right_stick_y + 1) * (height / 2))

    # Draw circles around the cursors for left and right sticks with different colors
    left_cursor_color = (150, 0, 100)  # Red for the left stick
    right_cursor_color = (200, 100, 0)  # Blue for the right stick

    pygame.draw.circle(screen, left_cursor_color, (left_cursor_x, left_cursor_y), cursor_radius)
    pygame.draw.circle(screen, right_cursor_color, (right_cursor_x, right_cursor_y), cursor_radius)

def display_axes(joystick, font, text_y):
    for a in range(joystick.get_numaxes()):
        axis_value = joystick.get_axis(a)
        if axis_value != 0.0:
            color = get_axis_color(a)
            axis_text = font.render(f"Axis {a}: {axis_value:.2}", True, color)
            screen.blit(axis_text, (10, text_y))
            text_y += 40

    return text_y

def display_hats(joystick, font, text_y):
    for h in range(joystick.get_numhats()):
        hat_value = joystick.get_hat(h)
        if hat_value != (0, 0):
            color = (0, 255, 255)  # Cyan for hat info
            hat_text = font.render(f"Hat {h} is being used: {hat_value}", True, color)
            screen.blit(hat_text, (10, text_y + 10))

            arrow_text = get_arrow_text(hat_value, font, color)
            if arrow_text:
                screen.blit(arrow_text, (320, text_y + 10))

            text_y += 40

    return text_y

def get_button_color(button_index):
    if joystick.get_name() == 'Controller (XBOX 360 For Windows)':
        button_colors = {
            0: (0, 255, 25),  # Green A
            1: (255, 0, 0),  # Red B
            2: (0, 0, 255),  # Blue X
            3: (255, 255, 0),  # Yellow Y
            6: (255, 50, 0),  # Orange Back
            7: (100, 100, 100),  # Light Yellow LS
            8: (255, 255, 100),  # Dark Blue RS
            9: (100, 100, 255),  # Dark Gray Start
            10: (10, 100, 75)  # Dark Green Xbox Button
        }
    elif joystick.get_name() == 'PC Game Controller':
         button_colors = {
            0: (0, 0, 255),  # Blue X
            1: (255, 0, 0),  # Red A
            2: (255, 255, 0),  # Yellow B
            3: (0, 255, 0),  # Green Y
            4: (255, 50, 0),  # Orange Back
            5: (100, 100, 100),  # Light Yellow LS
            6: (255, 255, 100),  # Dark Blue RS
            7: (100, 100, 255),  # Dark Gray Start
            8: (255, 255, 100),  # Dark Blue RS
            9: (100, 100, 255),  # Dark Gray Start

        }
       
    return button_colors.get(button_index, (255, 255, 255))  # Default to white if not found

def get_axis_color(axis_index):
    # Function to determine color based on axis index
    color = (255, 255, 255)  # Default color

    if 0 <= axis_index <= 1:  # X and Y axes
        color = (150, 0, 100)  # Left
    elif 2 <= axis_index <= 3:  # Z and R axes
        color = (200, 100, 0)  # Right
    elif 4 <= axis_index <= 5:  # L and R triggers
        color = (0, 0, 255)  # Blue

    return color

def get_arrow_text(hat_value, font, color):
    # D-Pad Arrows
    arrow_text = None

    if hat_value == (0, -1):  # Down
        arrow_text = font.render("DOWN", True, color)
    elif hat_value == (0, 1):  # Up
        arrow_text = font.render("UP", True, color)
    elif hat_value == (-1, 0):  # Left
        arrow_text = font.render("LEFT", True, color)
    elif hat_value == (1, 0):  # Right
        arrow_text = font.render("RIGHT", True, color)

    return arrow_text

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Continuously check for controller input
    num_controllers = pygame.joystick.get_count()

    for i in range(num_controllers):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        display_controllers(joystick)
        
    if num_controllers == 0:
        font = pygame.font.Font(None, 36)
        no_joystick_text = font.render("<!(-Connect a Controller-)!>", True, (200, 10, 0), (0,20,20))
        screen.blit(no_joystick_text, (250, 40))
        font = pygame.font.Font(None, 23)
        text = font.render(("*"*5) + "none connected*****", True, (255, 255, 255))
        screen.blit(text, (300, 80))
    if num_controllers > 0:
        font = pygame.font.Font(None, 40)
        text_here = font.render(f"{joystick.get_name()} w/ {joystick.get_numbuttons()} Buttons", True, (125, 180, 85))
        screen.blit(text_here, (10, 500))
        axis_test()
        screen.blit(font.render(f"**Battery Level: {joystick.get_power_level()}**", True, (255, 255, 0)), (10, 460))

    pygame.display.flip()
    screen.fill((0, 0, 0))

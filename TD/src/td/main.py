import pygame

def run_event_processing():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (mouse_x, mouse_y) in menu_zone:
                    ...
                    #if coor in button of menu do something

                mouse_x = mouse_x // 100
                mouse_y = mouse_y // 100
                print("left ", mouse_x, mouse_y)

        if event.type == pygame.BUTTON_WHEELUP:
            ...

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_x2, mouse_y2 = pygame.mouse.get_pos()
                mouse_x2 = mouse_x2 // 100
                mouse_y2 = mouse_y2 // 100
                print("right ", mouse_x2, mouse_y2)


def draw_map(gamewindow, background, list_of_roads):
    gamewindow.fill(background)
    # draw fon
    # while for objects road - rect
    for r in list_of_roads:
        pygame.draw.rect(gamewindow, (175, 121, 61), r, 0)


def main():
    # draw fon - picture
    # def for save road in file


    # def for read road from file
    # add editor mode for key F2
    list_of_roads = []




    pygame.init()
    FON_BLUE = (203, 156 , 105)
    pygame.display.set_caption("TD")
    gamewindow = pygame.display.set_mode((800, 800))

    while True:
        mouse_result = run_event_processing()
        if not mouse_result is None:

            draw_map(gamewindow, FON_BLUE,list_of_roads)

            pygame.display.flip()

menu_zone = [(900,0), (1100,200)]

if __name__ == "__main__":
    main()
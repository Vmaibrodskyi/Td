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

                x, y = pygame.mouse.get_pos()
                m_type = 'D'
                print(x, y, m_type)
                return x, y, m_type


        if event.type == pygame.BUTTON_WHEELUP:
            ...

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                x, y = pygame.mouse.get_pos()
                m_type = 'U'
                print(x, y, m_type)
                return x, y, m_type


def draw_map(gamewindow, background, list_of_roads):
    gamewindow.fill(background)
    # draw fon
    # while for objects road - rect
    for r in list_of_roads:
        print(r)
        pygame.draw.rect(gamewindow, (175, 121, 61), r, 0)


def main():
    # draw fon - picture
    # def for save road in file


    # def for read road from file
    # add editor mode for key F2
    list_of_roads = []

    pygame.init()
    FON_BLUE = (0, 50 , 100)
    pygame.display.set_caption("TD")
    gamewindow = pygame.display.set_mode((800, 800))

    cur_x = 0
    cur_y = 0
    while True:
        mouse_result = run_event_processing()

        if not mouse_result is None:
            x, y, m_type = mouse_result[0], mouse_result[1], mouse_result[2]
            if m_type == 'D':
                cur_x = x
                cur_y = y
            else:

                new_rect = pygame.Rect(cur_x,cur_y, x-cur_x,y-cur_y)
                print(cur_x,cur_y, x-cur_x,y-cur_y)
                cur_x = 0
                cur_y = 0
                list_of_roads.append(new_rect)
            draw_map(gamewindow, FON_BLUE,list_of_roads)

            pygame.display.flip()

menu_zone = [(900,0), (1100,200)]

if __name__ == "__main__":
    main()
import classes
import rendering
import game_logic
import pygame 


def main():
    clock = pygame.time.Clock()
    run = True

    # "Game states":
    ship_selected = None
    settlement_selected = None

    game_logic.initialize_game()
    #rendering.draw_window()

    while run:
        clock.tick(rendering.FPS)
        game_logic.update(game_logic.player_1)
        rendering.draw_window()
        rendering.draw_player_elements(game_logic.player_1)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


            elif settlement_selected != None:
                rendering.show_menu()

            elif ship_selected != None and event.type == pygame.MOUSEBUTTONDOWN:
                ship_selected.destination = [
                    pygame.mouse.get_pos()[0],
                    pygame.mouse.get_pos()[1],
                ]
                ship_selected = None

            else: #  event.type == pygame.MOUSEBUTTONDOWN:
                # Check if a ship is clicked
                for shi in game_logic.player_1.ships:
                    ship_selected = shi.is_clicked(event)
                # Check if a settlement is clicked
                for setl in game_logic.player_1.settlements:
                    settlement_selected = setl.is_clicked(event)
                



if __name__ == "__main__":
    game_logic.initialize_game()
    main()

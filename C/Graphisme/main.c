
/*
    compilation:
        Linux: 
            sudo apt-get install libsdl2-dev 
            gcc main.c -lSDL2
        Windows:

            pratique : visual studio 2022 vcpkg install sdl2:x86-windows sdl2:x64-windows
            cl main.c /I "C:\Users\GAMER\vcpkg\installed\x86-windows\include" /link /LIBPATH:"C:\Users\GAMER\vcpkg\installed\x86-windows\lib"  SDL2.lib
            SDL2.dll à portée lors de l'éxécution
            théorie : gcc main.c -o prog -I include -L lib -lmingw32 -lSDL2main -lSDL2

*/

#include <stdio.h>
#include <SDL2/SDL.h>

int SCREEN_WIDTH=640;
int SCREEN_HEIGHT=480;
#ifdef _WIN32
    #define main main
#endif
int main(int argc, char *argv[]) {
    SDL_Window *window = NULL;
    SDL_Renderer *renderer = NULL;
    SDL_Rect rect;

    // Initialisation de la SDL
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        printf("Erreur lors de l'initialisation de la SDL : %s\n", SDL_GetError());
        return 1;
    }

    // Création de la fenêtre
    window = SDL_CreateWindow("Application SDL2", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN|SDL_WINDOW_RESIZABLE);
    if (window == NULL) {
        printf("Erreur lors de la création de la fenêtre : %s\n", SDL_GetError());
        return 1;
    }

    // Création du renderer
    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if (renderer == NULL) {
        printf("Erreur lors de la création du renderer : %s\n", SDL_GetError());
        return 1;
    }



    

    // Position et dimensions du carré
    rect.x = SCREEN_WIDTH / 4;
    rect.y = SCREEN_HEIGHT / 4;
    rect.w = SCREEN_WIDTH / 2;
    rect.h = SCREEN_HEIGHT / 2;

    // Dessin du carré
    SDL_RenderFillRect(renderer, &rect);

    // Affichage du rendu à l'écran
    SDL_RenderPresent(renderer);

    // Boucle principale
    int quit = 0;
    SDL_Event event;
    while (!quit) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                quit = 1;
            }else if(event.type == SDL_KEYDOWN)
            {
                if(event.key.keysym.sym == SDLK_ESCAPE)
                    quit=1;
                else if(event.key.keysym.sym == SDLK_RIGHT)
                {
                    printf("La touche RIGHT a ete presse\n");
                }else if(event.key.keysym.sym == SDLK_DOWN)
                {
                     printf("La touche DOWN a ete presse\n");
                }else if(event.key.keysym.sym== SDLK_LEFT)
                {
                     printf("La touche LEFT a ete presse\n");
                }else if(event.key.keysym.sym == SDLK_UP)
                {
                     printf("La touche UP a ete presse\n");
                }
            }else if (event.type == SDL_WINDOWEVENT) 
            if (event.window.event == SDL_WINDOWEVENT_RESIZED) {
                SCREEN_WIDTH = event.window.data1;
                SCREEN_HEIGHT = event.window.data2;
                printf("Fenêtre redimensionnée : %d x %d\n", SCREEN_HEIGHT, SCREEN_WIDTH);
            }
        }
        
        //On efface tout
        // Couleur du fond : noir
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderClear(renderer);

        //On dessine notre carré
        // Couleur du carré : blanc
        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
        // Dessin du carré
        SDL_RenderFillRect(renderer, &rect);

        // Affichage du rendu à l'écran
        SDL_RenderPresent(renderer);
    }

    // Libération des ressources
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}

/*
    compilation ligne de commande:
        Linux: 
            sudo apt-get install libsdl2-dev libsdl2-mixer-dev
            gcc -lSDL2 -lSDL2_mixer main.c 
        Windows:


            gcc main.c -o prog -I include -L lib -lmingw32 -lSDL2main -lSDL2

*/

/*
    VisualStudio 2022
    Pour lancer ce programme : 
            décharger les autres projets
            installer SDL via vcpk (mettre la souris sur les includes, une proposition apparait)
            lancer
    ce programme afficher un carré blanc manipulable avec les touche du clavier
    il joue de la musique depuis le fichier(musique.wav)
    gère le redimensionnement de la fenêtre

    Ce code est entièrement écris en C pur. pas de C++ donc je ne m'attarderai pas dessus, il est ici à titre d'exemple.
    Le principal à retenir est l'installation de librairie avec vcpkg, qui offre une solution simple à l'un des plus gros calvaire du C/C++.

*/
#define max(a,b) (a>b)?a:b

#include <stdio.h>
#include <SDL2/SDL.h>
#include <stdlib.h>
#include <string.h>
#include <SDL2/SDL_mixer.h>




int SCREEN_WIDTH=640;
int SCREEN_HEIGHT=480;
int SCREEN_POS_X = 0;
int SCREEN_POS_Y = 0;

#ifdef _WIN32
#define main main
#endif // _WIN

int main(int argc, char *argv[]) {
    SDL_Window *window = NULL;
    SDL_Renderer *renderer = NULL;
    SDL_Rect rect;

    // Initialisation de la SDL
    if (SDL_Init(SDL_INIT_VIDEO| SDL_INIT_AUDIO) < 0) {
        printf("Erreur lors de l'initialisation de la SDL : %s\n", SDL_GetError());
        return 1;
    }

    //Initialisation de la musique
    char* musiquePath = (argc > 1) ? argv[1] : NULL;
    if (musiquePath == NULL)
    {
        musiquePath = (char*)malloc(100);
        #ifdef _WIN32
        strcpy_s(musiquePath,100 , "musique.wav");
        #else
        strcpy(musiquePath,"musique.wav");
        #endif
    }
    
    if (Mix_OpenAudio(44100, MIX_DEFAULT_FORMAT, 2, 2048) < 0) {
        printf("Erreur lors de l'initialisation de SDL_mixer : %s\n", Mix_GetError());
        return 1;
    }

    //Chargement du fichier audio
    Mix_Music* music = Mix_LoadMUS(musiquePath);
    if (music == NULL) {
        printf("Erreur lors du chargement de la musique : %s\n", Mix_GetError());
        return 1;
    }
    //Lecture de la musique
    if (Mix_PlayMusic(music, -1) == -1) {
        printf("Erreur lors de la lecture de la musique : %s\n", Mix_GetError());
        return 1;
    }

    // Création de la fenêtre
    window = SDL_CreateWindow("Application SDL2", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN|SDL_WINDOW_RESIZABLE);
    if (window == NULL) {
        printf("Erreur lors de la création de la fenêtre : %s\n", SDL_GetError());
        return 1;
    }

    SDL_GetWindowPosition(window,&SCREEN_POS_X,&SCREEN_POS_Y);

    // Création du renderer
    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if (renderer == NULL) {
        printf("Erreur lors de la création du renderer : %s\n", SDL_GetError());
        return 1;
    }



    

    // Position et dimensions du carré
    rect.x = SCREEN_WIDTH / 4;
    rect.y = SCREEN_HEIGHT / 4;
    rect.w = 100;
    rect.h = 100;

    int vx = 0;
    int vy = 0;

    SDL_Color rectColor = { 255,255,255,255 };

    // Dessin du carré
    SDL_RenderFillRect(renderer, &rect);

    // Affichage du rendu à l'écran
    SDL_RenderPresent(renderer);

    // Boucle principale
    int quit = 0;
    int iterations = 0;

    //Gestion des événements
    SDL_Event event;
    while (!quit) {
        iterations++;
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                quit = 1;
            }else if(event.type == SDL_KEYDOWN)
            {
                switch (event.key.keysym.sym)
                {
                case SDLK_ESCAPE:
                    quit = 1;
                    break;
                case SDLK_RIGHT:
                    vx = 1;
                    break;
                case SDLK_LEFT:
                    vx = -1;
                    break;
                case SDLK_UP:
                    vy = -1;
                    break;
                case SDLK_DOWN:
                    vy = 1;
                    break;
                default:
                    break;
                }            

            }
            else if (event.type == SDL_KEYUP)
            {
                switch (event.key.keysym.sym)
                {
                case SDLK_ESCAPE:
                    quit = 1;
                    break;
                case SDLK_RIGHT:
                    vx = 0;
                    break;
                case SDLK_LEFT:
                    vx = 0;
                    break;
                case SDLK_UP:
                    vy = 0;
                    break;
                case SDLK_DOWN:
                    vy = 0;
                    break;
                default:
                    break;
                }
            }
            else if (event.type == SDL_WINDOWEVENT)
            {
                if (event.window.event == SDL_WINDOWEVENT_RESIZED) {
                    SCREEN_WIDTH = event.window.data1;
                    SCREEN_HEIGHT = event.window.data2;
                    SDL_GetWindowPosition(window,&SCREEN_POS_X,&SCREEN_POS_Y);
                    printf("Fenetre redimensionnee : %d x %d\n", SCREEN_HEIGHT, SCREEN_WIDTH);
                }
                else if (event.window.event == SDL_WINDOWEVENT_MOVED)
                {
                    
                    SDL_GetWindowPosition(window,&SCREEN_POS_X,&SCREEN_POS_Y);
                    printf("Fenetre redimensionnee : %d x %d\n", SCREEN_POS_X, SCREEN_POS_Y);
                }
            }
        }
        
        //On efface tout
        // Couleur du fond : noir
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderClear(renderer);

        //On dessine notre carré
        // Couleur du carré : blanc
        SDL_SetRenderDrawColor(renderer, rectColor.r, rectColor.g, rectColor.b, rectColor.a);
        // Dessin du carré
        SDL_RenderFillRect(renderer, &rect);

        // Affichage du rendu à l'écran
        SDL_RenderPresent(renderer);


        //On déplace le carré
        rect.x += vx;
        rect.y += vy;

        //Si le carré est en dehors de l'écran
        int deltax = max(-rect.x, rect.x+rect.w-SCREEN_WIDTH );
        int deltay = max(-rect.y,rect.y+rect.h -SCREEN_HEIGHT );

        if (deltax>0 || deltay>0)
        {
            printf("Sortie de l'ecran : rect = %d;%d  sizeindow = %d,%d decalage de %d;%d \n",rect.x,rect.y,SCREEN_WIDTH,SCREEN_HEIGHT,deltax,deltay);

            //on cgange la couleur
            rectColor.g = 0;
            rectColor.b = 0;

            //on agrandit l'écran 
            SCREEN_WIDTH += (deltax > 0) ? deltax : 0;
            SCREEN_HEIGHT += (deltay > 0) ? deltay : 0;

            SDL_SetWindowSize(window, SCREEN_WIDTH, SCREEN_HEIGHT);
            //on déplace l'écran et le rectangle du mouvement inverse de l'écran (on annule son mouvement = il ne bouge pas)
            SCREEN_POS_X -= (rect.x<0)?deltax:0;
            SCREEN_POS_Y -= (rect.y<0)?deltay:0;
            rect.x += (rect.x < 0) ? deltax : 0;
            rect.y += (rect.y < 0) ? deltay : 0;
            SDL_SetWindowPosition(window, SCREEN_POS_X, SCREEN_POS_Y);
        }
        else {
            rectColor.r = 255;
            rectColor.g = 255;
            rectColor.b = 255;
            if (iterations % 100 == 0)
            {
                //on rétrecit la fenêtre
                SCREEN_WIDTH -= 2;
                SCREEN_HEIGHT -= 2;
                //on déplace l'origine de la fenêtre
                SCREEN_POS_X+=1;
                SCREEN_POS_Y+=1;
                //on compense le déplacement de la fenêtre
                rect.x-=1;
                rect.y-=1;

                SDL_SetWindowPosition(window,SCREEN_POS_X,SCREEN_POS_Y);
                SDL_SetWindowSize(window, SCREEN_WIDTH, SCREEN_HEIGHT);
            }

        }



        
    }





    // Libération des ressources
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    Mix_FreeMusic(music);
    Mix_CloseAudio();

    SDL_Quit();

    return 0;
}
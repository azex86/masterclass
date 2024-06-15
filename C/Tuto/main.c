//Exemple d'utilisation de la SDL  graphisme + musique

//git clone ssh://personne@grandmont-aze.freeboxos.fr:2000/Stockage/Ressources/Git/C/Tuto

/*
    compilation en ligne de commande:
        Linux: 
            sudo apt-get install libsdl2-dev 
            gcc -lSDL2 main.c 
        Windows:
            gcc main.c -o prog -I include -L lib -lmingw32 -lSDL2main -lSDL2

*/

//Librairie standard Input/Output 
#include <stdio.h>
//librairie standard pour manipulation mémoire et allocation dynamique (appel système)
#include <stdlib.h>
//librairie de manipulation de char*
#include <string.h>

//librairie SDL principal
#include <SDL2/SDL.h>
//librairie SDL Musique
#include <SDL2/SDL_mixer.h>

#include <SDL2/SDL_ttf.h>

int SCREEN_WIDTH=640;
int SCREEN_HEIGHT=480;


#ifdef _WIN32
#undef main
#endif // _WIN

int main(int argc, char *argv[]) {
    SDL_Window *window = NULL;
    SDL_Renderer *renderer = NULL;
    SDL_Rect rect;

    // Initialisation de la SDL
    if (SDL_Init(SDL_INIT_VIDEO| SDL_INIT_AUDIO|SDL_INIT_EVERYTHING) < 0) {
        printf("Erreur lors de l'initialisation de la SDL : %s\n", SDL_GetError());
        return 1;
    }

    //Initialisation de la musique
    char* musiquePath = (argc > 1) ? argv[1] : NULL;
    if (musiquePath == NULL)
    {
        musiquePath = malloc(100);

        strcpy_s(musiquePath,100 , "musique.wav");
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
    //deplacement du rcarré
    int vx = 0;
    int vy = 0;
    //Couleur du carré
    SDL_Color rectColor = { 255,255,255,255 };


    //Affichage de text
    if (TTF_Init() == -1)
    {
        printf("Erreur lors du chargement de la police : %s", TTF_GetError());
        return -1;
    }
    TTF_Font* font = TTF_OpenFont("police.ttf", 24);
    if (font == NULL) {
        printf("Erreur lors du chargement de la police : %s", TTF_GetError());
        return -1;
    }
    // Boucle principale
    int quit = 0;



    while (!quit) {
        //Gestion des événements : on boucle pour chaque éénement s'étant produit depuis la dernière gestion des événements
        SDL_Event event;
        while (SDL_PollEvent(&event)) 
        {
            //l'OS nous envoie le signale de fin
            if (event.type == SDL_QUIT) {
                quit = 1;
            }
            //un touche est préssée
            else if(event.type == SDL_KEYDOWN)
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
            //une touche est relaché
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
            //la fenêtre a été modifié 
            else if (event.type == SDL_WINDOWEVENT)
            {
                if (event.window.event == SDL_WINDOWEVENT_RESIZED) {
                    SCREEN_WIDTH = event.window.data1;
                    SCREEN_HEIGHT = event.window.data2;
                    printf("Fenetre redimensionnee : %d x %d\n", SCREEN_HEIGHT, SCREEN_WIDTH);
                }
                else if (event.window.event == SDL_WINDOWEVENT_MOVED)
                {
                    int x, y;
                    SDL_GetWindowPosition(window, &x, &y);
                    printf("Fenetre redimensionnee : %d x %d\n", x, y);
                }
            }
        }
        //couleur de la prochaine opération :  Couleur du fond : noir : 0,0,0
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);

        //On efface tout = on remplit l'écran de noir
        SDL_RenderClear(renderer);

        //On dessine notre carré
        //couleur de la prochaine opération :  Couleur du carré : rectColor
        SDL_SetRenderDrawColor(renderer, rectColor.r, rectColor.g, rectColor.b, rectColor.a);
        // Dessin du carré
        SDL_RenderFillRect(renderer, &rect);

        //coloration des contours
        SDL_SetRenderDrawColor(renderer, 0, 0, 255, 255);

        SDL_RenderDrawLine(renderer, 0, 0, 0, SCREEN_HEIGHT-1);
        SDL_RenderDrawLine(renderer, 0, 0, SCREEN_WIDTH-1, 0);
        SDL_RenderDrawLine(renderer, SCREEN_WIDTH-1, 0, SCREEN_WIDTH-1, SCREEN_HEIGHT-1);
        SDL_RenderDrawLine(renderer, 0, SCREEN_HEIGHT-1, SCREEN_WIDTH-1, SCREEN_HEIGHT-1);

        //Affichage du texte
        SDL_Color textColor = { 255, 255, 255, 255 };
        SDL_Surface* textSurface = TTF_RenderText_Solid(font, "Text", textColor);
        SDL_Texture* textTexture = SDL_CreateTextureFromSurface(renderer, textSurface);

        SDL_Rect textRect = { 100, 100, textSurface->w, textSurface->h };
        SDL_RenderCopy(renderer, textTexture, NULL, &textRect);
        SDL_DestroyTexture(textTexture);
        SDL_FreeSurface(textSurface);
        

        // Affichage du rendu à l'écran
        SDL_RenderPresent(renderer);



        //On déplace le carré de la vitesse
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
            int xpos, ypos;
            SDL_GetWindowPosition(window, &xpos, &ypos);
            xpos -= (rect.x<0)?deltax:0;
            ypos -= (rect.y<0)?deltay:0;
            rect.x += (rect.x < 0) ? deltax : 0;
            rect.y += (rect.y < 0) ? deltay : 0;
            SDL_SetWindowPosition(window, xpos, ypos);
        }
        else {
            rectColor.r = 255;
            rectColor.g = 255;
            rectColor.b = 255;
        }





    }





    // Libération des ressources
    TTF_CloseFont(font);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    Mix_FreeMusic(music);
    Mix_CloseAudio();

    SDL_Quit();

    return 0;
}
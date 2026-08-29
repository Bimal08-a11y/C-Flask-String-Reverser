#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char text[256] ="";
    
    fgets(text,sizeof(text),stdin);
    int len = strlen(text);
    
    for(int i = len-1; i>=0;i--){
        if(text[i]=='\n'){
            
            continue;
        }
        printf("%c",text[i]);

    }
    printf("\n");
    



    

    return 0;
}

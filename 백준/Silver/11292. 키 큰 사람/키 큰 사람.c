#include <stdio.h>

int main(){
    char name[100][10];
    float height[100];
    
    int N;
    
    scanf("%d", &N);
    
    while (N>0) {
        for (int i=0; i<N; i++){
            scanf("%s %f", &name[i], &height[i]);
        }
        float max_height = 0;
        for (int i=0; i<N; i++){
            if (height[i] > max_height){
                max_height = height[i];
            }
        }
        for (int i=0; i<N; i++){
            if (height[i]==max_height) {
                printf("%s\n", name[i]);
            }
        }
        scanf("%d", &N);       
    }
  
    return 0;
}
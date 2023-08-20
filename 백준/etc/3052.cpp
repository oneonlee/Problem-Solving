#include <iostream>

using namespace std;

int main() {
    
    int input[10];
    
    int remainder[10];
    
    for (int i=0; i<10; i++){
        cin>>input[i];
        
        remainder[i] = input[i]%42;
    }
    
    int cnt = 1;
    int same_cnt = 0;
    for (int i=1; i<10; i++) {
        for (int j=0; j<i; j++){
            if (remainder[i]==remainder[j]){
                same_cnt++;
                break;
            }
        }
    
    }
    
    
    cout<<10-same_cnt;
    
    
    return 0;
}

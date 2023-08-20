#include <iostream>

using namespace std;

int main() {
    int A;
    int B;
    int C;
    
    cin>>A;
    cin>>B;
    cin>>C;
    
    int num = A*B*C;
    int count[10] = {0};
    int answer;
    
    while (num>0) {
        answer = num % 10;
        num = num/10;
        
        count[answer] = count[answer] + 1;
    }

    
    for (int i=0; i<(sizeof count/sizeof count[0]); i++){
        cout<<count[i]<<endl;    
    }
    
    
    return 0;
}

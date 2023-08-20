// DP[K][N] = DP[K-1][0] + DP[K-1][1] + .... + DP[K-1][N]

#include <iostream>

using namespace std;

int main()
{
  
  int N, K= 0;
  
  cin>>N>>K;
  
  //dp[k][n] = k개 더해서 n 나오는 경우의 수
  long dp[201][201]={0};
  
  for(int n = 0; n <= N; n++) {
        dp[1][n]=1; //0,1,2,3,...N
  }
  
  for(int k = 2; k <= K; k++) {
      for(int n = 0; n <= N; n++) {
          for(int l = 0; l <= n; l++) {
              dp[k][n] += dp[k-1][l];
          }
            dp[k][n] %= 1000000000;
      }
  }
  
  cout<<(dp[K][N]);
}

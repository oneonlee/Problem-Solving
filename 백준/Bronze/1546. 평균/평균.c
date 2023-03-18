#include <stdio.h>
#include <stdlib.h>

int main()
{
    int N, subject;
	scanf("%d", &N);

	int max_score = 0;
    float t=0;
    
	for (int i = 0; i < N; i++) {
		scanf("%d", &subject);
		t += subject;
		if (subject > max_score) {
			max_score = subject;
		}
	}
	
	printf("%.2f", t/N/max_score*100);

    return 0;
}
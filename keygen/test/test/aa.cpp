#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char a[15] = { 95, -74, 72, 85, -80, 68, -94, 71, 65, -82, -69, -75, 0, 0 };
	char e[20] = { 0, };
	for (int b = 0x00; b <= 0xff; b++) {
		for (int c = 0x00; c <= 0xff; c++) {
			for (int i = 0; i < 15; i += 3) {
				e[i] = a[i] ^ b;
				e[i + 1] = a[i + 1] ^ 'E';
				e[i + 2] = a[i + 2] ^ c;
				e[i] += 80;
				e[i + 1] += 80;
				e[i + 2] += 80;
				e[i] %= 256;
				e[i + 1] %= 256;
				e[i + 2] %= 256;
			}
			printf("%s\n", e);
			memset(e, 0, 20);
		}
	}
	getchar();
}
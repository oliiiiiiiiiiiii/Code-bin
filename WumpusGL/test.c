// Prototype for WumpusGL!

#include <stdio.h>
#include "WumpusGL.h"

int main()
{
	char stuff[] = "111110101010101001";
	render(stuff);

	char stuff2file[] = "1010010101010101001\n <-- File Test -->";
	render2file(stuff2file, "your_file_name");
}

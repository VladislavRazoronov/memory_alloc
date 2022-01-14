#include <iostream>
#include <unistd.h>

int main(int argc, char* argv[]){
	if(argc < 3){
		return 0;
	}
	while(true){
		void* memory = malloc(std::stoi(std::string(argv[1])));
		sleep(std::stoi(std::string(argv[2])));
		free(memory);
	}
	return 0;
}

poc: main.o victim.o
	g++ -o poc main.o victim.o

main.o: main.cpp
	g++ -Wall -fexceptions -O2 -std=c++11 -c main.cpp -o main.o

victim.o: victim.cpp
	g++ -Wall -fexceptions -O2 -std=c++11 -c victim.cpp -o victim.o


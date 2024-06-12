# Building and running test files (play)

NAME := runthis
DEFAULT_FILE := play
FLAGS := -std=c++11 -02 -Wall
COMPILER = g++

all: py

py:
	@python3 $(DEFAULT_FILE).py

cpp:
	$(COMPILER) $(FLAGS) (DEFAULT_FILE).cpp -o $(NAME)

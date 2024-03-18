COMPILER = gcc
FLAGS = -Wall -Werror -Wextra -fsanitize=address

vector:
	@$(COMPILER) $(FLAGS) -o vector vector.c
	@./vector

clean:
	@rm vector

re: clean vector

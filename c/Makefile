COMPILER = gcc
FLAGS = -Wall -Werror -Wextra -fsanitize=address
COMPILE = @$(COMPILER) $(FLAGS) -o $@.out $@.c
RUN = ./$@.out

vector:
	$(COMPILE) && $(RUN)

linkedlist:
	$(COMPILE) && $(RUN)

clean:
	@rm *.out

re: clean

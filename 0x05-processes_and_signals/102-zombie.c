#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sched.h>

/**
 * infinite_while - A function that runs an infinite loop.
 *
 * Return: Always 0.
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main - Entry point of the program.
 *
 * Return: Always 0.
 */
int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();

		if (child_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
			sleep(1);
		}
		else if (child_pid == 0)
		{
			exit(0);
		}
		else
		{
			perror("Fork failed");
			exit(EXIT_FAILURE);
		}
	}

	infinite_while();

	return (0);
}

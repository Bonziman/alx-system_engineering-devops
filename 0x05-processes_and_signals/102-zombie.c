#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * main - program entry point
 * Return: ntg
 */
int main(void)
{
	int i;

	for (i = 0; i < 5; ++i)
	{
		pid_t child_pid = fork();

		if (child_pid == -1)
		{
			perror("Fork failed");
			exit(EXIT_FAILURE);
		}
		if (child_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
		}
		else
		{
			sleep(2);
			exit(EXIT_SUCCESS);
		}
	}
}
/**
 * infinite_while - just an infinite loop
 * Return: ntg
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

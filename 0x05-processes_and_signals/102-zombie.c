#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>
#include <unistd.h>
/**
 * infinite_while- for an infinite loop
 * Return: always 0 success
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
 * main- for 5 zombie processes
 * Return: always 0 success
 */
int main(void)
{
	pid_t pid;
	char num = 0;

	while (num < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			num++;
		}
		else
		{
			exit(0);
		}
	}
	infinite_while();
	return (EXIT_SUCCESS);
}


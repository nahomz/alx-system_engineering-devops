#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
  * to_infinity - create an infinite loop.
  *
  * Return: always 0.
  */
int to_infinity(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
  * main - creates 5 zombie preocesses.
  *
  * Return: NAIN.
  */
int main(void)
{
	unsigned int i;
	pid_t zombie;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		if (!zombie)
			return (0);
		printf("Zombie process created, PID: %d\n", zombie);
	}

	to_infinity();
	return (0);
}

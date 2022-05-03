#include "lists.h"

/**
 * is_palindrome - checks if list is palindrome
 * @head: list
 * Return: 0 for no, 1 for yes
 */

int is_palindrome(listint_t **head)
{
	int array[2048];
	listint_t *current = *head;
	int i, j = 0;

	if (!head)
		return(-1);

	if (*head == NULL)
		return (1);

	for (i = 0; current->next != NULL; i++)
	{
		if (i >= 2048)
			return (-1);

		array[i] = current->n;
		current = current->next;
	}
	array[i] = current->n;

	for (j = 0; j < i; j++, i--)
	{
		if (array[j] != array[i])
			return (0);
	}
	return (1);
}

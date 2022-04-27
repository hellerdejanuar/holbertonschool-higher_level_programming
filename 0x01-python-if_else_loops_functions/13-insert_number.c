#include "lists.h"

/**
 * insert_node - inserts a node in a sorted single linked list
 * @head: pointer to list
 * @number: number
 * Return: pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	if (head == NULL)
	{
		new->next = NULL;
		head = &new;
	}

	if (head != NULL)
	{
		current = *head;
		if (current->n < number)
		{
			for (; current->next != NULL; current = current->next)
			{
				if (current->next->n > number)
				{
					break;
				}
			}
		}

		new->next = current->next;
		current->next = new;
	}

	new->n = number;

	return (new);
}

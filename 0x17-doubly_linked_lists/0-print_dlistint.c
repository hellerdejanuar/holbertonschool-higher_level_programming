#include "lists.h"
/**
 * print_dlistint - prints all te elements of a dlistint_t list
 * @h: list
 * Return number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	int cn;

	for (cn = 0; h->next != NULL; cn++)
	{
		printf("%d\n", h->n);
		h = h->next;
	}
	printf("%d\n", h->n);
	cn++;
	return (cn);
}

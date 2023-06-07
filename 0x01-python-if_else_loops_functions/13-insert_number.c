#include "list.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}

	new->n = number;
	new->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		listint_t *current = *head;
		while (current->next != NULL && number >= current->next->n)
		{
			current = current->next;
		}

		new->next = current->next;
		current->next = new;
	}
	return (new);
}

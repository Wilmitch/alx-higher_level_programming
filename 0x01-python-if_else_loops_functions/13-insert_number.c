#include "lists.h"
#include <stdlib.h>
#include <unistd.h>

/**
 * insert_node - this will insert a number to an ordered linked list.
 * @head: address of head pointer or double pointer to the linked list.
 * @number: number to be inserted in the new node.
 *
 * Return: address of the inserted node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new = NULL;
	listint_t *temp = NULL;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (current && current->n < number)
		{
			temp = current;
			current = current->next;
		}
		temp->next = new;
		new->next = current;
	}

	return (new);
}

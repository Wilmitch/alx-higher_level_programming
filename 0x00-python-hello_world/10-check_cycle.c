#include "lists.h"

/**
 * check_cycle - This will check if there is a cycle in the linked list.
 * @list: node in the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *i = list;

	if (!list)
		return (0);

	list = list->next;
	while (list)
	{
		if (i == list)
			return (1);
		if (!(list->next) || !(list->next->next))
			return (0);
		i = i->next;
		list = list->next->next;
	}
	return (0);
}

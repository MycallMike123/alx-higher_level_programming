#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: A pointer to the head of linked list
 * Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *kobe, *hare;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	kobe = list->next;
	hare = list->next->next;

	while (kobe && hare && hare->next)
	{
		if (kobe == hare)
		{
			return (1);
		}

		kobe = kobe->next;
		hare = hare->next->next;
	}

	return (0);
}

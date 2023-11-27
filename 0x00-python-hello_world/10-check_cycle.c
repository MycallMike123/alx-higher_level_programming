#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: A pointer to the head of linked list
 * Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL)
	{
		return (0);
	}

	slow = list;
	fast = list->next;

	while (slow != fast)
	{
		if (fast == NULL || fast->next == NULL)
		{
			return (0);
		}

		slow = slow->next;
		fast = fast->next;
	}

	return (1);
}

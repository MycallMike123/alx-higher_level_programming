#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Address of the head (linked list)
 * @number: Number to insert
 * Return: Address of the new node, NULL otherwise
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current_node, *prev_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	current_node = *head;
	prev_node = NULL;

	while (current_node != NULL && current_node->n < number)
	{
		prev_node = current_node;
		current_node = current_node->next;
	}

	prev_node->next = new_node;
	new_node->next = current_node;

	return (new_node);
}

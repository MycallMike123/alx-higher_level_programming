#include "lists.h"
#include <stdio.h>

int compare_lists(listint_t *head1, listint_t *head2);
void reverse_list(listint_t **head);

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to the head of the LL
 * Return: 1 if palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *kobe = *head;
	listint_t *hare = *head;
	listint_t *prev_kobe = *head;
	listint_t *second_half;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (hare != NULL && hare->next != NULL)
	{
		hare = hare->next->next;
		prev_kobe = kobe;
		kobe = kobe->next;
	}

	if (hare != NULL)
		kobe = kobe->next;

	second_half = kobe;
	prev_kobe->next = NULL;
	reverse_list(&second_half);

	is_palindrome = compare_lists(*head, second_half);
	reverse_list(&second_half);
	prev_kobe->next = second_half;

	return (is_palindrome);
}

/**
 * compare_lists - Compares two linked lists
 * @head1: Pointer to the head of 1st LL
 * @head2: Pointer to the head of 2nd LL
 * Return: 1 if the linked lists are equal, 0
 */

int compare_lists(listint_t *head1, listint_t *head2)
{
	while (head1 != NULL && head2 != NULL)
	{
		if (head1->n != head2->n)
		{
			return (0);
		}

		head1 = head1->next;
		head2 = head2->next;
	}

	return (1);
}

/**
 * reverse_list - Reverses a linked list
 * @head: Pointer to the head of the LL
 */

void reverse_list(listint_t **head)
{
	listint_t *prev_node = NULL;
	listint_t *current_node = *head;
	listint_t *next = NULL;

	while (current_node != NULL)
	{
		next = current_node->next;
		current_node->next = prev_node;
		prev_node = current_node;
		current_node = next;
	}

	*head = prev_node;
}

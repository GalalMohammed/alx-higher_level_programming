#ifndef LISTS_H
#define LISTS_H

#include <stddef.h>

/**
  * struct listint_s - singly linked list
  * @n: int
  * @next: points to the next node
  *
  * Description: singly linked list node structure
  */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/**
  * struct listp_s - singly linked list
  * @p: pointer
  * @next: points to the next node
  *
  * Description: singly linked list node structure
  */
typedef struct listp_s
{
	const listint_t *p;
	struct listp_s *next;
} listp_t;

int _putchar(char);
size_t print_listint(const listint_t *);
size_t print_listint_safe(const listint_t *);
size_t listint_len(const listint_t *);
listint_t *add_nodeint(listint_t **, const int);
listp_t *add_nodep(listp_t **, const listint_t *);
listint_t *add_nodeint_end(listint_t **, const int);
void free_listint(listint_t *);
size_t free_listint_safe(listint_t **);
void free_listint2(listint_t **);
int pop_listint(listint_t **);
listint_t *get_nodeint_at_index(listint_t *, unsigned int);
int sum_listint(listint_t *);
listint_t *insert_node(listint_t **, int);
int delete_nodeint_at_index(listint_t **, unsigned int);
listint_t *reverse_listint(listint_t **);

#endif /* ifndef LISTS_H */

// Implements a dictionary's functionality

#include <stdbool.h>

#include "dictionary.h"

// impelement a hash-table as the dictionary
// a node of the linked-list
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// hash table - the array of linked lists
node *hashtable[HASHTABLE_SIZE];

/* Hash function: credit to
    https://www.reddit.com/r/cs50/comments/1x6vc8/pset6_trie_vs_hashtable/cf9nlkn
*/

int hash_it(char *needs_hashing)
{
    unsigned int hash = 0;
    for (int i = 0, n = strlen(needs_hashing); i < n; i++)
    {
        hash = (hash << 2) ^ needs_hashing[i];
    }
    return hash % HASHTABLE_SIZE;
}

// global variable for tracking dictionary size
unsigned int word_count = 0;
// global varibale to load and unload
bool loaded = false;

// Returns true if word is in dictionary else false
// by finding in a hashtable
bool check(const char *word)
{
    int word_len = strlen(word);
    char word_copy[word_len + 1];

    for (int i = 0; i < word_len; ++i)
    {
        word_copy[i] = tolower(word[i]);
    }

    word_copy[word_len] = '\0';

    // cursor at the head
    int h = hash_it(word_copy);
    node *cur = hashtable[h];

    while (cur != NULL)
    {
        if (strcmp(cur->word, word_copy) == 0) // find the word
        {
            return true;
        }
        else  // move the cursor
        {
            cur = cur->next;
        }
    }
    // we cannot find it
    return false;
}

// Loads dictionary into memory, returning true if successful else false
// Return  true of load successfully, false otherwise
bool load(const char *dictionary)
{
    // clear the memory - all the memory to NULL (very necessary)
    for (int i = 0; i < HASHTABLE_SIZE; ++i)
    {
        hashtable[i] = NULL;
    }

    //open file
    FILE *inptr = fopen(dictionary, "r");
    if (inptr == NULL)
    {
        printf("Could not open %s.\n", dictionary);
        return false;
    }
    // start to load
    while (true)
    {
        // new node
        node *new_node = malloc(sizeof(node));
        // always need to check if successful
        if (new_node == NULL)
        {
            printf("Out of Memory.\n");
            free(new_node);
            return false;
        }
        // now read the word
        fscanf(inptr, "%s", new_node -> word);
        new_node->next = NULL;
        // if we reaches the end of the file
        if (feof(inptr))
        {
            free(new_node);
            break; // break out of the loop
        }

        ++word_count;

        // get the hash code
        int h = hash_it(new_node->word);
        // get the head
        node *head = hashtable[h];
        // insert
        if (head == NULL)
        {
            hashtable[h] = new_node;
        }
        else
        {
            // insert at the front - it's quicker
            new_node -> next = hashtable[h];
            hashtable[h] = new_node;
        }
    }
    //close the file
    fclose(inptr);
    // change the global variable
    loaded = true;
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    if (loaded)
    {
        return word_count;
    }
    return 0;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // just clear all nodes in the hash table
    for (int i = 0; i < HASHTABLE_SIZE; ++i)
    {
        node *cur = hashtable[i];
        if (cur != NULL)  //free head to tail
        {
            node *temp = cur;
            cur = cur->next;
            free(temp);
        }
    }
    loaded = false;
    return true;
}

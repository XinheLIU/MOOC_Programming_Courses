// Declares a dictionary's functionality

#ifndef DICTIONARY_H
#define DICTIONARY_H

#include <stdbool.h>
#include <stddef.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Maximum length for a word
// (e.g., pneumonoultramicroscopicsilicovolcanoconiosis)
#define LENGTH 45
#define HASHTABLE_SIZE (16^4)

// Prototypes
// check whether a word is in a dictionary
bool check(const char *word);
//load dictionary
bool load(const char *dictionary);
//return number of words
unsigned int size(void);
//unload dictionary from memory
bool unload(void);

#endif // DICTIONARY_H

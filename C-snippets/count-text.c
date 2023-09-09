// This set of functions are kind of self explanatory but they could be of use in some projects. 

// first function, it loops through each character of a string, if it finds an alphabetical character it adds one to a variable that counts the letters and finally, it returns that variable as an int.
int count_letters(string text)
{
    int letter_counter = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            letter_counter++;
        }
    }
    return letter_counter;
}


// second function, it loops through each character of a string, if it finds a whitespace character it adds one to a variable that counts the words and finally, it returns that variable as an int.
// The variable that counts the quantity of words gets initialized with 1 so the word that ends the string also is counted and for the cases in which the user only inputs one word.

int count_words(string text)
{
    int word_counter = 1;

    for (int j = 0; j < strlen(text); j++)
    {
        if (isspace(text[j]))
        {
            word_counter++;
        }
    }
    return word_counter;
}

// third function, it loops through each character of a string, if it finds a dot, exclamation mark or question mark, it adds one to a variable that counts the sentences and finally, it returns the variable as an int.
int count_sentences(string text)
{
    int sentences_counter = 0;

    for (int k = 0; k < strlen(text); k++)
    {
        if (text[k] == '.' || text[k] == '!' || text[k] == '?')
        {
            sentences_counter++;
        }
    }
    return sentences_counter;
}